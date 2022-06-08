import sys
from services.expenseManager import ExpenseManager
from models.commands import Commands
from models.split.splitType import SplitType
from models.split.equalSplit import EqualSplit
from models.user import User


class Driver:

    @staticmethod
    def main(input_file_path=None):
        if not input_file_path:
            input_file_path = sys.argv[1]

        expense_manager = ExpenseManager()

        with open(input_file_path) as input_file:
            all_lines = input_file.readlines()

        for line in all_lines:
            if line[-1] == '\n':
                line = line[:-1]
            commands = line.split(" ")
            command_type = commands[0]

            # DUES command
            if command_type == Commands.DUES.value:
                user_name = commands[1]
                if user_name not in expense_manager.user_map:
                    print("MEMBER_NOT_FOUND")
                else:
                    expense_manager.show_balance_for_user(user_name)

            # MOVE IN command
            elif command_type == Commands.MOVE_IN.value:
                if len(expense_manager.user_map) == 3:
                    print("HOUSEFUL")
                else:
                    user = User(commands[1])
                    expense_manager.add_user(user)
                    print("SUCCESS")

            # MOVE OUT command
            elif command_type == Commands.MOVE_OUT.value:
                user = commands[1]
                res = expense_manager.remove_user(user)
                print(res)

            # SPEND command
            elif command_type == Commands.SPEND.value:
                if len(expense_manager.user_map) < 2:
                    print("MEMBER_NOT_FOUND")
                    continue

                amount = int(commands[1])
                paid_by = commands[2]
                number_of_users = len(commands) - 2
                # considering the default split type, for new split type we can accept split type in command
                split_type = SplitType.EQUAL.value
                splits = []

                # different split types can be added here
                if split_type == SplitType.EQUAL.value:
                    for i in range(number_of_users):
                        user_name = commands[2+i]
                        user = expense_manager.user_map.get(user_name)
                        if user:
                            s = EqualSplit(user)
                            splits.append(s)

                    if len(splits) == number_of_users:
                        expense_manager.add_expense(split_type, paid_by, amount, splits)
                        print("SUCCESS")
                    else:
                        print("MEMBER_NOT_FOUND")
                else:
                    print("INVALID_SPLIT_TYPE")

            # CLEAR DUES command
            elif command_type == Commands.CLEAR_DUE.value:
                paid_by = commands[1]
                paid_to = commands[2]
                amount = int(commands[3])
                res = expense_manager.due_paid(paid_by, paid_to, amount)
                print(res)

            else:
                print("INVALID_COMMAND")


if __name__ == '__main__':
    path = "./myInput.txt"
    Driver.main()
