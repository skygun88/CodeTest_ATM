import os
import sys
ROOT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(ROOT_DIR_PATH)

from ATM import ATM
from Card import Card

def main():
    # Set up the ATM
    db_path = os.path.join(ROOT_DIR_PATH, 'db.json')
    atm = ATM(db_path)
    
    # Get PIN of card and make the card object
    print('Enter the PIN of your card')
    pin = input()
    print(pin)
    card = Card(pin)
    
    if atm.insert_card(card): # Insert card. If valid, provide ATM service
        while True:
            # Get desired service from user 
            print("Choose a service (balance/deposit/withdraw/end)")
            service = input().strip().lower()
            print(service)
            if service == "balance": # balance
                balance = atm.balance()
                print(f'Balance - {balance}')
                
            elif service == "deposit": # deposit
                print("Enter the value you want to deposit")
                value = int(input())
                print(value)
                succ, new_balance = atm.deposit(value)
                if succ:
                    print(f'Deposit - {new_balance}')
                else:
                    print(f'Deposit - failed')
                    
            elif service == "withdraw": # withdraw
                print("Enter the value you want to withdraw")
                value = int(input())
                print(value)
                succ, new_balance = atm.withdraw(value)
                if succ:
                    print(f'Withdraw - {new_balance}')
                else:
                    print(f'Withdraw - not enough balance')
            
            else: # service ended
                atm.end_service()
                print('Service is ended')
                break
            
    else: # If PIN is not valid, end the service
        print('Invalid card')

if __name__ == "__main__":
    main()