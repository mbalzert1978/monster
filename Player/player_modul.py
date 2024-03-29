from abc import ABC, abstractmethod
import random

from HeroClass.hero_class import Hero


class Player(ABC):
    def __init__(self, hero_classes: dict, name=None) -> None:
        self.hero_classes = hero_classes
        self.name = name or self.get_name()
        self.hero_class = self.get_hero_class()

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_hero_class(self) -> None:
        pass

    @abstractmethod
    def get_move(self) -> None:
        pass


class RandomCPUPlayer(Player):
    def get_name(self) -> str:
        return random.choice(["Hal9000", "T-800", "ED-209", "M.A.R.K.13"])

    def get_hero_class(self) -> None:
        return self.hero_classes[random.choice(list(self.hero_classes))]()

    def get_move(self):
        return self.hero_class.actions[random.choice(list(self.hero_class.actions))]


class BetterCPUPlayer(Player):
    def get_name(self) -> str:
        return "Uther"

    def get_hero_class(self) -> None:
        return self.hero_classes["Paladin"]()

    def get_move(self):
        return self.hero_class.actions[random.choice(list(self.hero_class.actions))]


class HumanPlayer(Player):
    def get_name(self) -> str:
        return input("Please Name your Hero: ")

    def get_hero_class(self) -> Hero:
        valid = list(self.hero_classes)
        while True:
            print("Wich Hero Class want you to play? ")
            try:
                val = input(f"{', '.join(valid)} :")
                if val in valid:
                    return self.hero_classes[val]()
                raise ValueError
            except ValueError:
                print("No valid choice, try again.")

    def get_move(self):
        valid = list(self.hero_class.actions)
        while True:
            print("What do you want to do? ")
            print(f"{self.hero_class.cooldown} Rounds cooldown for specialmove")
            try:
                val = input(f"{', '.join(valid)} :")
                if val in valid:
                    return self.hero_class.actions[val]
                raise ValueError
            except ValueError:
                print("No valid choice, try again.")
