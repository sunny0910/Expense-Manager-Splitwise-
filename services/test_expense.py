import unittest
from models.expense.equalExpense import EqualExpense
from models.split.splitType import SplitType
from services.expense import ExpenseService
from models.split.equalSplit import EqualSplit


class TestExpenseService(unittest.TestCase):

    def test_add_expense(self):
        splits_input = [EqualSplit("woody"), EqualSplit("bo")]
        splits_output = splits_input.copy()
        output = EqualExpense(100, "wood", splits_output)
        amount = 100//2
        for s in output.get_splits():
            s.set_amount(amount)
        self.assertNotEqual(ExpenseService.add_expense(SplitType.EQUAL.value, 100, "mood", splits_input), output)


if __name__ == '__main__':
    unittest.main()
