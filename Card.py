'''
Card.py - Code for Card class
'''
class Card:
    def __init__(self, pin: str):
        self.pin = pin
        
    def get_pin(self):
        return self.pin