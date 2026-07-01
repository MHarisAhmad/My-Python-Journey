class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    def deposit(self, amount, description = ""):
        self.ledger.append({
            'amount': amount,
            'description': description
        })
        return f"Added {amount} in the ledger"
    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            return "Valid amount"
        else:
            return "Invalid amount"
        
        
    
    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item["amount"]
        return total
    
    def check_funds(self, amount):
        if amount < self.get_balance():
            return True
        else:
            return False
    
def create_spend_chart(categories):
    pass

person = Category("Ali")
person.deposit(500, "init")
print(person.withdraw(501,"my first withdraw check"))
