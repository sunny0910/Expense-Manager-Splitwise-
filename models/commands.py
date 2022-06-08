from enum import Enum


class Commands(Enum):
    """
    Enums for all supported commands
    """
    MOVE_IN = "MOVE_IN"
    SPEND = "SPEND"
    DUES = "DUES"
    CLEAR_DUE = "CLEAR_DUE"
    MOVE_OUT = "MOVE_OUT"
