from models.expense.equalExpense import EqualExpense
from models.split.splitType import SplitType


class ExpenseService:
    """
    Expense service
    """
    @staticmethod
    def add_expense(split_type, amount, paid_by, splits):
        """
        Adding expense as per the split type and calculate the split amount for each user
        :param split_type: split type (percent,equal,exact)
        :param amount: amount of expense
        :param paid_by: user who paid for expense
        :param splits: splits of amount for every yser in expense
        :return: expense
        """
        if split_type == SplitType.EQUAL.value:
            total_splits = len(splits)
            split_amount = amount//total_splits
            for split in splits:
                split.set_amount(split_amount)

            splits[0].set_amount(amount - (total_splits-1*split_amount))
            expense = EqualExpense(amount, paid_by, splits)
            return expense

        else:
            raise Exception('invalid split type')