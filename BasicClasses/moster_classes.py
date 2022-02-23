from dataclasses import dataclass
from BasicClasses.basic_class import BaseClass


@dataclass
class Monster(BaseClass):
    """
    Base Monster Class
    """

    class_name: str = "Morghul"
    attack_min: int = 10
    attack_max: int = 15
    health: int = 150

    def special_ability(self):
        pass
