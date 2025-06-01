# tests/test_converter.py

import unittest
from src.tracker import ExpenseTracker


class TestExpenseTracker(unittest.TestCase):
    def test_add_and_total(self):
        tracker = ExpenseTracker()
        tracker.add_expense("Обед", 250)
        tracker.add_expense("Такси", 300)
        self.assertEqual(tracker.total(), 550)

    def test_invalid_amount(self):
        tracker = ExpenseTracker()
        with self.assertRaises(ValueError):
            tracker.add_expense("Ошибка", -100)
