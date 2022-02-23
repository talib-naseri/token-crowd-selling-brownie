from doctest import script_from_examples
from brownie import CrowdSale, network
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_token_balance
from scripts.deploy_mun_token import deploy_mun_token
from scripts.deploy_crowd_sale import deploy_crowd_sale
from brownie import CrowdSale, MUNToken


def buy_token(beneficiary_account, amount=10000000000):

    # get a crowd sale contract
    if len(CrowdSale) == 0:
        rate = 12
        wallet = get_account().address
        if len(MUNToken) == 0:
            token = deploy_mun_token(100000000)
        else:
            token = MUNToken[-1]
        contract = deploy_crowd_sale(rate, wallet, token)
    else:
        contract = CrowdSale[-1]

    # show token and eth balace of user before transaction
    print('\nAFTER TX:')
    print('\tUser: ', beneficiary_account.address)
    print('\tEther Balance: ', beneficiary_account.balance())
    print('\tMunzi Balance: ', get_token_balance(
        token.address, beneficiary_account.address))
    print()

    contract.buyTokens(beneficiary_account.address, {
                       'from': beneficiary_account, 'amount': amount})

    # show token and eth balace of user after transaction
    print('\nBEFORE TX:')
    print('\tUser: ', beneficiary_account.address)
    print('\tEther Balance: ', beneficiary_account.balance())
    print('\tMunzi Balance: ', get_token_balance(
        token.address, beneficiary_account.address))
    print()


def main():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        account = get_account(index=1)
    else:
        account = get_account(
            id=input('Enter an account name in your brownie: '))

    buy_token(account)
