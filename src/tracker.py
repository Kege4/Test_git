# tracker.py

from src.models import Expense


class ExpenseTracker:
    def __init__(self):
        self.expenses: list[Expense] = []

    def add_expense(self, name: str, amount: float):
        self.expenses.append(Expense(name, amount))

    def total(self) -> float:
        return sum(e.amount for e in self.expenses)

    def show(self):
        for e in self.expenses:
            print(f"{e.name}: {e.amount:.2f} руб.")
