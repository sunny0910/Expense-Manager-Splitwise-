import unittest
from models.expense.expense import Expense


class TestExpense(unittest.TestCase):

    def test_get_amount(self):
        e = Expense(5, "woody", [])
        self.assertEqual(e.get_amount(), 5)

    def test_set_amount(self):
        e = Expense(5, "woody", [])
        self.assertTrue(e.set_amount(5))

    def test_get_paid_by(self):
        e = Expense(5, "woody", [])
        self.assertEqual(e.get_paid_by(), "woody")

    def test_set_paid_by(self):
        e = Expense(5, "woody", [])
        self.assertTrue(e.set_paid_by("woody"))

    def test_get_splits(self):
        e = Expense(5, "woody", [])
        self.assertEqual(e.get_splits(), [])

    def test_set_splits(self):
        e = Expense(5, "woody", [])
        self.assertTrue(e.set_splits([]))


if __name__ == '__main__':
    unittest.main()
