from brownie import FundMe
from scripts.helpful_scripts import getaccount

def fund():
  fund_me = FundMe[-1] #I'll interact with the last deployed contract
  account = getaccount()
  entrance_fee = fund_me.getEntranceFee()
  print(f"The current entry fee is {entrance_fee}")
  print("Funding")
  fund_me.fund({"from":account,"value":entrance_fee})

def withdraw():
  fund_me = FundMe[-1]
  account = getaccount
  fund_me.withdraw({"from":account})

def main():
  fund()
  withdraw()