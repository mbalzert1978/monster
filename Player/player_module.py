"""
player modul
"""
import random
from abc import ABC, abstractmethod
from typing import Any
from BasicClasses.player_classes import Paladin, Rogue
from BasicClasses.moster_classes import Monster
from BasicClasses.basic_class import BaseClass


class Player(ABC):
    """
    player class
    attributes:
    attack_min
    attack_max
    health
    heal
    """

    available_player_classes = [Paladin, Rogue]
    available_cpu_classes = [Paladin, Rogue, Monster]

    @abstractmethod
    def chose_class(self) -> None:
        """chose base class or CPU class"""

    @abstractmethod
    def make_move(self, attacker, target) -> None:
        """
        interface get_move
        """


class RandomComputerPlayer(Player):
    """
    computerplayer class who picks random
    """

    cpu_names = ["Hal9000", "T-800", "ED-209", "M.A.R.K.13"]

    def __init__(self, name: str = None) -> None:
        super().__init__()
        self.name = random.choice(self.cpu_names) if not name else name
        self.player_class = self.choose_class()

    def choose_class(self) -> BaseClass:
        """
        CPU chooses random class
        """
        return random.choice(self.available_cpu_classes)()

    def make_move(self, attacker, target=None):
        pass
        # return (
        #     "attack"
        #     if attacker.heal is None or self.health >= 100
        #     else random.choice(["attack", "heal"])
        # )


class BetterComputerPlayer(Player):
    """
    hopefully a better CPU player
    """

    cpu_name = "Uhter"

    def __init__(self, name: str = None) -> None:
        super().__init__()
        self.name = self.cpu_name if not name else name
        self.player_class = self.choose_class()

    def choose_class(self) -> None:
        """
        always chooses paladin class for selfheal
        """
        return Paladin()

    def make_move(self, attacker, target=None) -> str:
        return (
            "heal"
            if attacker.health <= 35 and target.health >= 10
            else "attack"
        )


class HumanPlayer(Player):
    """
    Human player class
    and print statements to explain the game
    """

    def __init__(self) -> None:
        super().__init__()
        self.name = input("Tell me the Name of your Hero: ")
        self.player_class = self.choose_class()

    def choose_class(self) -> None:
        """
        lets the player choose a class
        """
        valid = [class_.class_name for class_ in self.available_player_classes]

        user_input = self.get_input(
            valid=valid,
            decorator="What Class you want to play?",
            question=f"{', '.join(valid)}: ",
        )
        return eval(user_input)()

    @staticmethod
    def get_input(valid: list, decorator: str, question: str) -> Any:
        """
        checks user input and returns user input as int
        """
        while True:
            print(decorator)
            try:
                val = input(question)
                if val in valid:
                    return val
                raise ValueError
            except ValueError:
                print("No valid choice, try again.")

    def make_move(self, attacker, target=None) -> int:
        pass
        # return self.get_input(
        #     ["attack", "heal"],
        #     "What do you want to do?",
        #     "attack or heal: " if player.heal is not None else "attack: ",
        # )
