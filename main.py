import os
import sys
import json

ROOT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(ROOT_DIR_PATH)

from ATM import ATM
from Card import Card

if __name__ == "__main__":
    atm = ATM()
    card = Card(pin='bear230809')
    
    print(atm.curr_account)
    if atm.insert_card(card):
        print(atm.curr_account)
        print(atm.balance())
    else:
        print('No account for the card')