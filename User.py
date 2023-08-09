class User:
    def __init__(self, pin: str, balance: int):
        self.pin = pin
        self.balance = balance
        
    # def deposit(self, value: int):
    #     self.balance += value
    #     return self.balance
    
    # def withdraw(self, value: int):
    #     if self.balance >= value:
    #         self.balance -= value
    #         return self.balance
    #     else:
    #         return -1
    
    def get_balance(self):
        return self.balance
    
    def set_balance(self, value: int):
        self.balance = value
        
        
    def __eq__(self, __value: str):
        return __value == self.pin
    
    