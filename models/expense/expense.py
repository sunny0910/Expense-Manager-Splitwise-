class Expense:
    def __init__(self, amount, paid_by, splits):
        self._amount = amount
        self._paid_by = paid_by
        self._splits = splits

    def get_amount(self):
        return self._amount

    def set_amount(self, amount):
        self._amount = amount
        return True

    def get_paid_by(self):
        return self._paid_by

    def set_paid_by(self, user):
        self._paid_by = user
        return True

    def get_splits(self):
        return self._splits

    def set_splits(self, splits):
        self._splits = splits
        return True
