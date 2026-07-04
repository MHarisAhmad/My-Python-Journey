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
    # Calculate total withdrawals for each category
    spent = []

    for category in categories:
        total = 0
        for item in category.ledger:
            if item["amount"] < 0:
                total += -item["amount"]
        spent.append(total)

    total_spent = sum(spent)

    # Calculate percentages rounded down to nearest 10
    percentages = []
    for amount in spent:
        percent = int((amount / total_spent) * 100)
        percentages.append((percent // 10) * 10)

    # Build chart
    output = "Percentage spent by category\n"

    for i in range(100, -1, -10):
        output += f"{i:>3}|"
        for percent in percentages:
            if percent >= i:
                output += " o "
            else:
                output += "   "
        output += " \n"

    # Horizontal line
    output += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Category names vertically
    names = [category.name for category in categories]
    max_length = max(len(name) for name in names)

    for i in range(max_length):
        output += "     "
        for name in names:
            if i < len(name):
                output += name[i] + "  "
            else:
                output += "   "
        output += "\n"

    # Remove final newline
    return output.rstrip("\n")


food = Category("Food")
veg = Category("Vegetables")
food.deposit(5000, "Deposit: 1")
food.withdraw(200, "Withdraw: 1")
food.transfer(500, veg)
veg.withdraw(200, "Withdraw_01")
print(create_spend_chart([food, veg]))
