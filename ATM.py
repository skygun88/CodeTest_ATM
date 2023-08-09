'''
ATM.py - Code for ATM class
'''
import os
import sys
import json
from typing import Dict

ROOT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(ROOT_DIR_PATH)
from Card import Card

class ATM:
    def __init__(self, db_path: str):
        self.db_path: str = db_path
        self.db: Dict[str, int]  = self.read_db(self.db_path)
            
        self.curr_account = None
    
    # Insert credit card and check whether PIN is valid or not
    def insert_card(self, card: Card):
        pin: str = card.get_pin()
        if self.check_pin(pin):
            self.curr_account = pin
            return True
        else:
            return False
    
    # End the ATM service of current user
    def end_service(self):
        self.curr_account = None

    # Check whether current PIN is valide or not
    def check_pin(self, pin: str):
        return True if self.db.get(pin, None) != None else False
            
    # Get the balance of the current user
    def balance(self):
        return self.db[self.curr_account]

    # Deposit the desired value
    def deposit(self, value: int):
        balance: int = self.balance()
        new_balance: int = balance + value
        self.update_balance(new_balance)
        return True, new_balance
    
    # Withdraw the desired value
    def withdraw(self, value: int):
        balance: int = self.balance()
        if value > balance:
            return False, -1
        else:
            new_balance: int = balance - value
            self.update_balance(new_balance)
            return True, new_balance
    
    # Update current user's balance
    def update_balance(self, new_balance: int):
        self.db[self.curr_account] = new_balance
        self.update_db(self.db_path, self.db)
    
    # Update DB in both memory and file
    def update_db(self, db_path: str, db: Dict[str, int]):
        with open(db_path, "w") as f:
            json.dump(db, f, indent=4)
            f.close()
    
    # Read Database which contains User information (PIN, Blance)
    def read_db(self, db_path: str):
        with open(db_path, 'r') as f:
            db: dict = json.load(f)
            f.close()
        return db
    