import random
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Callable


@dataclass
class Hero(ABC):
    attack_min: int = 10
    attack_max: int = 15
    health: int = 100
    cooldown: int = 2

    def __post_init__(self) -> None:
        self.actions: dict[str, Callable] = {
            "attack": self.get_attack,
            "special": self.get_special,
        }

    def get_attack(self) -> int:
        """returns the attack value"""
        self.cooldown -= 1
        return random.choice(list(range(self.attack_min, self.attack_max + 1)))

    @abstractmethod
    def get_special(self) -> int:
        """returns special value"""
        ...

    def set_health(self, value: int) -> None:
        """sets health"""
        if self.health + value > 100:
            self.health = 100
            return
        if self.health + value <= 0:
            self.health = 0
            return
        self.health += value


@dataclass
class Paladin(Hero):
    selfheal: int = 20

    def __post_init__(self) -> None:
        self.actions = {
            "attack": self.get_attack,
            "special": self.get_special,
        }

    def get_special(self) -> int:
        """returns heal value"""
        if self.cooldown:
            self.cooldown -= 1
            return 0
        self.cooldown = 2
        return self.selfheal


@dataclass
class Rogue(Hero):
    attack_min: int = 8
    attack_max: int = 20
    special_damage: int = 30
    cooldown: int = 2

    def __post_init__(self) -> None:
        self.actions = {
            "attack": self.get_attack,
            "special": self.get_special,
        }

    def get_special(self) -> int:
        """uses special if available"""
        if self.cooldown:
            self.cooldown -= 1
            return 0
        self.cooldown = 2
        return self.special_damage
