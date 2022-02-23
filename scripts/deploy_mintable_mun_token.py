from scripts.helpful_scripts import get_account
from brownie import MUNTokenMintable
from web3 import Web3


def deploy_mun_token_mintable(total_supply):
    account = get_account()

    mun_token_mintable = MUNTokenMintable.deploy(Web3.toWei(
        int(total_supply), 'ether'), {'from': account})
    mun_token_mintable.tx.wait(1)

    print('Munzi Token deployed!')
    return mun_token_mintable


def main():
    total_supply = int(input('Enter the total supply of the token: '))
    deploy_mun_token_mintable(total_supply)
