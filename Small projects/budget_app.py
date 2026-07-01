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
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False
        
    def transfer(self, amount, destination):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {destination.name}")
            destination.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False
        
        
    
    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item["amount"]
        return total
    
    def check_funds(self, amount):
        if amount <= self.get_balance():
            return True
        else:
            return False
    
    def __str__(self):
        output = ""

    # Title
        output += self.name.center(30, "*") + "\n"

    # Transactions
        for item in self.ledger:
            description = item["description"][:23]
            amount = f"{item['amount']:.2f}"

            output += f"{description:<23}{amount:>7}\n"

    # Total
        output += f"Total: {self.get_balance():.2f}"

        return output
    
def create_spend_chart(categories):
    pass

person = Category("Ali")
second = Category("Ahmad")
person.deposit(500, "First")
person.withdraw(200, "First withdraw")
person.transfer(200, second)
print(person)

second.transfer(100, person)
print(second)