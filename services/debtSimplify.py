class DebtSimplify:
    """
    Debt Simplify service
    """

    def __init__(self):
        """
        self.graph - store adjacency matrix
        self.new_graph - To run simplify debt logic and get a new simplified graph
        self.user_name_to_vertex - map to store user name to graph vertex number
        self.vertex_to_user_name - map to store graph vertex number to user name
        """
        self.graph = []
        self.new_graph = None
        self.user_name_to_vertex_number = {}
        self.vertex_to_user_name = {}

    def add_node(self, val):
        """
        Adding a node to graph
        :param val: node val (username)
        :return: None
        """
        self.user_name_to_vertex_number[val] = len(self.graph)
        self.vertex_to_user_name[len(self.graph)] = val
        self.graph.append([0 for _ in range(len(self.graph))])
        for i, nei in enumerate(self.graph):
            self.graph[i].append(0)

    def add_edge(self, u, v, weight):
        """
        Add edge from u to v
        :param u: paid_by user
        :param v: paid_to user
        :param weight: amount
        :return: None
        """
        vertex_number_u = self.user_name_to_vertex_number[u]
        vertex_number_v = self.user_name_to_vertex_number[v]
        self.graph[vertex_number_u][vertex_number_v] = weight

    def get_min_net_amount(self, amounts):
        """
        get minimum amount from list of net amounts
        :param amounts: net amounts for each user
        :return: index of minimum new amount
        """
        min_index = 0
        for i in range(1, len(self.graph)):
            if amounts[i] < amounts[min_index]:
                min_index = i

        return min_index

    def get_max_net_amount(self, amounts):
        """
        get maximum amount from list of net amounts
        :param amounts: net amounts for each user
        :return: index of maximum new amount
        """
        max_index = 0
        for i in range(1, len(self.graph)):
            if amounts[i] > amounts[max_index]:
                max_index = i

        return max_index

    def min_cash_flow_recur(self, amount):
        """
        Recursive function to apply minimum cash flow algo for simplifying debt payments
        :param amount: new amounts for all users
        :return: None
        """
        # max_credit = paid_to
        max_credit = self.get_max_net_amount(amount)
        # max_debit = paid_by
        max_debit = self.get_min_net_amount(amount)

        if amount[max_credit] == 0 and amount[max_debit] == 0:
            return 0

        m = min(-amount[max_debit], amount[max_credit])
        amount[max_credit] -= m
        amount[max_debit] += m

        self.new_graph[max_debit][max_credit] = m

        self.min_cash_flow_recur(amount)

    def simplify_debt(self):
        """
        Function to simplify debt payments by applying minimum cash flow algorithm
        :return: None
        """
        n = len(self.graph)
        net_amounts = [0 for _ in range(n)]

        for p in range(n):
            for i in range(n):
                net_amounts[p] += (self.graph[i][p] - self.graph[p][i])

        self.new_graph = [[0 for _ in range(len(self.graph))] for _ in range(len(self.graph))]
        self.min_cash_flow_recur(net_amounts)
        self.graph = self.new_graph
        self.new_graph = None

    def get_balance_sheet_for_user(self, user_name):
        """
        Get balance sheet for a user from graph after applying simplify debt
        :param user_name: user_name
        :return: map of user to balance
        """
        vertex_number = self.user_name_to_vertex_number[user_name]
        balance_sheet = {}
        for i in range(len(self.graph[vertex_number])):
            balance_sheet[self.vertex_to_user_name[i]] = self.graph[vertex_number][i]

            if self.graph[vertex_number][i] == 0 and self.graph[i][vertex_number] != 0:
                balance_sheet[self.vertex_to_user_name[i]] = -self.graph[i][vertex_number]

        return balance_sheet
