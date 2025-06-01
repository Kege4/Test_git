import unittest
from src.main import create_task

class TestTaskCreation(unittest.TestCase):

    def test_create_task_valid_data(self):
        task = create_task("Buy milk", "2 liters of milk")
        self.assertEqual(task["title"], "Buy milk")
        self.assertEqual(task["description"], "2 liters of milk")

    def test_create_task_missing_title(self):
        with self.assertRaises(ValueError):
            create_task("", "No title")

if __name__ == '__main__':
    unittest.main()