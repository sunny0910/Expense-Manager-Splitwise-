from enum import Enum


class SplitType(Enum):
    """
    Enum for all supported type of split expenses
    """
    EXACT = 'EXACT'
    EQUAL = 'EQUAL'
    PERCENT = 'PERCENT'
