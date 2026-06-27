class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    def deposit(self, amount, description = ''):
        self.ledger.append({'amount': amount, 'description': description})
    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False
    def get_balance(self):
        total = 0
        for entry in self.ledger:
            total += entry['amount']
        return total
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True
        
    

def create_spend_chart(categories):
    pass