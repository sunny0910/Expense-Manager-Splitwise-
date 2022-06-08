import unittest
from models.expense.equalExpense import EqualExpense
from models.expense.expense import Expense


class TestEqualExpense(unittest.TestCase):

    def test_validate(self):
        splits = []
        for i in range(2):
            ee = EqualExpense(None, None, [])
            splits.append(ee)
        ee = EqualExpense(10, "woody", splits)
        self.assertTrue(ee.validate())
        
        splits.append(Expense(None, None, None))
        self.assertFalse(ee.validate())


if __name__ == '__main__':
    unittest.main()
