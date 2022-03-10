from abc import ABC, abstractmethod
from dataclasses import dataclass
from pyclbr import Function
import random


@dataclass
class BaseHero(ABC):
    attack_min: int
    attack_max: int
    health: int
    cooldown: int

    actions: dict[str, Function]

    def get_attack(self) -> tuple:
        """returns the attack value"""
        self.cooldown -= 1
        return (
            random.choice(list(range(self.attack_min, self.attack_max + 1))),
            True,
        )

    def set_health(self, change) -> None:
        """sets health"""
        if self.health + change > 100:
            self.health = 100
            return
        if self.health + change <= 0:
            self.health = 0
            return
        self.health += change


class Healer(BaseHero, ABC):
    selfheal: int

    @abstractmethod
    def get_heal(self) -> int:
        """returns heal value"""


class Damagedealer(BaseHero, ABC):
    special_damage: int

    @abstractmethod
    def get_special(self) -> tuple:
        """returns special attack value"""


@dataclass
class Paladin(Healer):
    attack_min: int = 10
    attack_max: int = 15
    health: int = 100
    selfheal: int = 20
    cooldown: int = 2
    actions: dict = None

    def __init__(self) -> None:
        self.actions = {
            "attack": self.get_attack,
            "use selfheal": self.get_heal,
        }

    def get_heal(self) -> tuple:
        """returns heal value"""
        if not self.cooldown:
            self.cooldown = 2
            return (self.selfheal, False)
        self.cooldown -= 1
        return (self.selfheal - 15, False)


@dataclass
class Rogue(Damagedealer):
    attack_min: int = 8
    attack_max: int = 20
    health: int = 100
    special_damage: int = 30
    cooldown: int = 2
    actions: dict = None

    def __init__(self) -> None:
        self.actions = {
            "attack": self.get_attack,
            "use special": self.get_special,
        }

    def get_special(self) -> tuple:
        """uses special if available"""
        if not self.cooldown:
            self.cooldown = 2
            return (self.special_damage, True)
        self.cooldown -= 1
        return (self.get_attack()[0], True)
