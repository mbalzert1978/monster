from dataclasses import dataclass
from BasicClasses.basic_class import BaseClass


@dataclass
class Paladin(BaseClass):
    """
    Paladin Class with heal
    """

    class_name: str = "Paladin"
    attack_min: int = 10
    attack_max: int = 15
    health: int = 100
    heal: int = 16

    def special_ability(self):
        self.health += self.heal


@dataclass
class Rogue(BaseClass):
    """
    Rogue Class no special so far
    """

    class_name: str = "Rogue"
    attack_min: int = 10
    attack_max: int = 15
    health: int = 100

    def special_ability(self):
        pass
