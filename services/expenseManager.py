from services.expense import ExpenseService
from services.debtSimplify import DebtSimplify


class ExpenseManager:
    """
    Expense Manager service
    """
    # constant variable to turn on/off simplify debt feature
    SIMPLIFY_DEBT = True

    def __init__(self):
        """
        self.user_map - To store username to user object
        self.balance_sheet - To show who owes how much and who gets back how much
        self.expenses - To store expenses in case of categorising them in future
        self.graph - To apply implementation of simplify debt(if turned on)
        """
        self.user_map = {}
        self.balance_sheet = {}
        self.expenses = []
        self.graph = DebtSimplify()

    def add_user(self, user):
        """
        Adds user to the expense manager
        :param user: user object
        :return: None
        """
        self.user_map[user.get_name()] = user
        self.balance_sheet[user.get_name()] = {}
        self.graph.add_node(user.get_name())

    def add_expense(self, split_type, paid_by, amount, splits):
        """
        Adds expense to the expense manager
        :param split_type: type of split - equal, exact, percent
        :param paid_by: user who paid for expense
        :param amount: total amount of expense
        :param splits: splits as per split type
        :return: None
        """
        expense = ExpenseService.add_expense(split_type, amount, paid_by, splits)
        self.expenses.append(expense)

        for split in splits:
            paid_to = split.get_user().get_name()
            if paid_to not in self.balance_sheet[paid_by]:
                self.balance_sheet[paid_by][paid_to] = 0

            self.balance_sheet[paid_by][paid_to] += split.get_amount()

            if paid_by not in self.balance_sheet[paid_to]:
                self.balance_sheet[paid_to][paid_by] = 0

            self.balance_sheet[paid_to][paid_by] -= split.get_amount()

            if ExpenseManager.SIMPLIFY_DEBT and paid_to != paid_by:
                self.graph.add_edge(paid_to, paid_by, split.get_amount())

        if ExpenseManager.SIMPLIFY_DEBT:
            self.graph.simplify_debt()
            self._refresh_balance_sheet()

    def _refresh_balance_sheet(self):
        """
        Refresh balance sheet after applying simplify debt feature
        :return: None
        """
        for user in self.balance_sheet:
            balance_sheet = self.graph.get_balance_sheet_for_user(user)
            self.balance_sheet[user] = balance_sheet

    def show_balance_for_user(self, user):
        """
        Show balance due for user
        :param user: Username
        :return: output in descending order of amount and if amount is same - ascending order of name
        """
        output = []
        if self.balance_sheet[user]:
            for user1, balance in self.balance_sheet[user].items():
                if user1 == user:
                    continue

                output.append((balance if balance >= 0 else 0, user1))

        output.sort(key=lambda x: (x[0], x[1]), reverse=True)
        i = 1
        while i < len(output):
            if output[i][0] == output[i-1][0]:
                j = i
                while j < len(output) and output[j][0] == output[j-1][0]:
                    j += 1
                ai = output[i-1:j].copy()
                ai.sort(key=lambda x: x[1])
                output = output[:i-1] + ai + output[j:]
                i = j
            i += 1

        for (bal, user) in output:
            print("%s %s" % (user, bal))

    def due_paid(self, paid_by, paid_to, amount):
        """
        Paid balance due to a user
        :param paid_by: user paying the amount
        :param paid_to: user getting paid
        :param amount: amount of transaction
        :return: Updated balance
        """
        if len(self.user_map) < 2:
            return "MEMBER_NOT_FOUND"

        if amount > self.balance_sheet[paid_by][paid_to] > 0:
            return "INCORRECT_PAYMENT"

        self.balance_sheet[paid_by][paid_to] -= amount
        self.balance_sheet[paid_to][paid_by] += amount
        return self.balance_sheet[paid_by][paid_to]

    def remove_user(self, user):
        """
        MOVE_OUT function.
        Remove user if all expenses settled, if not settled, return failure
        :param user: user_name
        :return: message [SUCCESS/FAILURE]
        """
        if user not in self.balance_sheet:
            return "MEMBER_NOT_FOUND"

        dues_left = False
        for flatmate, bal in self.balance_sheet[user].items():
            if bal != 0:
                dues_left = True
                break

        return "FAILURE" if dues_left else "SUCCESS"
