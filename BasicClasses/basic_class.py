"""
Class modul
"""
from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class BaseClass(ABC):
    """
    base Class
    """

    attack_min: int
    attack_max: int
    health: int

    @abstractmethod
    def special_ability(self):
        """Class specialability"""
