from models.split.split import Split


class EqualSplit(Split):
    """
    Type of split where amount gets equally split amount participating users
    """
    def __init__(self, user):
        super().__init__(user)
