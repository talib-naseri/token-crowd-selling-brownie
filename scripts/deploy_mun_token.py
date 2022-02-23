from scripts.helpful_scripts import get_account
from brownie import MUNToken
from web3 import Web3


def deploy_mun_token(total_supply):
    account = get_account()

    mun_token = MUNToken.deploy(Web3.toWei(
        int(total_supply), 'ether'), {'from': account})
    mun_token.tx.wait(1)

    print('Munzi Token deployed!')
    return mun_token


def main():
    total_supply = int(input('Enter the total supply of the token: '))
    deploy_mun_token(total_supply)
