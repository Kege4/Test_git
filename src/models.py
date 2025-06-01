# models.py

class Expense:
    def __init__(self, name: str, amount: float):
        if amount < 0:
            raise ValueError("Amount must be positive")
        self.name = name
        self.amount = amount
