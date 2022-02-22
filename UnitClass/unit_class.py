"""
UnitClass modul
"""


class UnitClass:
    """
    base Class
    """

    def __init__(self) -> None:
        pass


class Paladin(UnitClass):
    """
    Paladin Class with heal
    """

    def __init__(self) -> None:
        super().__init__()
        self.attack_min: int = 10
        self.attack_max: int = 10
        self.health: int = 100
        self.heal: int = 16

    def __str__(self) -> str:
        return "Paladin"


class Rogue(UnitClass):
    """
    Rogue Class no special so far
    """

    def __init__(self) -> None:
        super().__init__()
        self.attack_min: int = 5
        self.attack_max: int = 30
        self.health: int = 100

    def __str__(self) -> str:
        return "Rogue"


class Monster(UnitClass):
    """
    Base Monster Class
    """

    def __init__(self) -> None:
        super().__init__()
        self.attack_min: int = 10
        self.attack_max: int = 20
        self.health: int = 100
