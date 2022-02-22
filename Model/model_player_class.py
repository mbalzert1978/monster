"""
UnitClass modul
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Model(ABC):
    """
    base Class
    """

    attack_min: int
    attack_max: int
    health: int
    special_cooldown: int = 0

    @abstractmethod
    def __str__(self) -> str:
        """function to print own value"""


@dataclass
class Paladin(Model):
    """
    Paladin Class with heal
    """

    attack_min: int = 10
    attack_max: int = 15
    health: int = 100
    heal: int = 16

    def heal_self(self):
        """can heal himself"""
        self.health += self.heal
        self.special_cooldown = 3

    def __str__(self) -> str:
        return "Paladin"


@dataclass
class Rogue(Model):
    """
    Rogue Class no special so far
    """

    attack_min: int = 5
    attack_max: int = 20
    health: int = 100

    def extra_attack(self):
        """can extra attack"""
        # implement
        pass

    def __str__(self) -> str:
        return "Rogue"


@dataclass
class Monster(Model):
    """
    Base Monster Class
    """

    attack_min: int = 10
    attack_max: int = 15
    health: int = 100

    def bite(self):
        """monster bites"""
        # implement
        pass
