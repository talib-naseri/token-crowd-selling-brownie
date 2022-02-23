from scripts.helpful_scripts import get_account, get_crowd_sale_info
from scripts.deploy_mun_token import deploy_mun_token
from brownie import CrowdSale, MUNToken, interface
from web3 import Web3


def deploy_crowd_sale(rate, wallet, token):
    account = get_account()
    crowd_sale = CrowdSale.deploy(int(rate), wallet, token, {'from': account})
    crowd_sale.tx.wait(1)

    # transfer tokens to crowd sale
    interface.IERC20(token).transfer(crowd_sale.address,
                                     interface.IERC20(token).totalSupply(), {'from': account})

    print('Crowd Sale token deployed!')

    return crowd_sale


def main():
    rate = int(input('Enter the rate per ETH/BNB: '))
    wallet = get_account().address
    if len(MUNToken) == 0:
        token = deploy_mun_token(100000000)
    else:
        token = MUNToken[-1]

    contract = deploy_crowd_sale(rate, wallet, token.address)
    get_crowd_sale_info(contract)
