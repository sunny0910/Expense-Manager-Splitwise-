from models.expense.expense import Expense


class EqualExpense(Expense):
    """
    An expense where all users are equally splitting the amount
    """
    def __init__(self, amount, paid_by, splits):
        super().__init__(amount, paid_by, splits)

    def validate(self):
        for split in self.get_splits():
            if type(split) != EqualExpense:
                return False

        return True
    
    def __eq__(self, other):
        return self._amount == other.get_amount() and self._paid_by == other.get_paid_by() \
               and self._splits == other.get_splits()
