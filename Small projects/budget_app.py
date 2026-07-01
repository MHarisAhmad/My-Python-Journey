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
    
    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item["amount"]
        return total
    
def create_spend_chart(categories):
    pass


