class Player:
    """
    player class
    attributes:
    attack_min
    attack_max
    health
    heal
    """

    cpu_names = ["Hal9000", "T-800", "ED-209", "M.A.R.K.13"]
    available_player_classes = [Paladin, Rogue]
    available_cpu_classes = [Paladin, Rogue, Monster]

    def __init__(self) -> None:
        self.attack_min = None
        self.attack_max = None
        self.health = None
        self.heal = None

    def get_move(self, player, target) -> None:
        """
        interface get_move
        """

    def set_attributes(self, class_) -> None:
        """
        sets attributes in class
        """
        self.attack_min = class_.attack_min
        self.attack_max = class_.attack_max
        self.health = class_.health
        self.heal = class_.heal if hasattr(class_, "heal") else None


class RandomComputerPlayer(Player):
    """
    computerplayer class who picks random
    """

    def __init__(self, name: str = None) -> None:
        super().__init__()
        self.name = random.choice(self.cpu_names) if not name else name
        self.choose_class()

    def choose_class(self) -> None:
        """
        CPU chooses random class
        """
        self.set_attributes(random.choice(self.available_cpu_classes)())

    def get_move(self, player, target=None) -> int:
        return (
            "attack"
            if player.heal is None or self.health >= 100
            else random.choice(["attack", "heal"])
        )


class BetterComputerPlayer(Player):
    """
    hopefully a better CPU player
    """

    def __init__(self, name: str = None) -> None:
        super().__init__()
        self.name = random.choice(self.cpu_names) if not name else name
        self.choose_class()

    def choose_class(self) -> None:
        """
        always chooses paladin class for selfheal
        """
        self.set_attributes(Paladin())

    def get_move(self, player, target=None) -> int:
        return (
            "heal" if player.health <= 35 and target.health >= 10 else "attack"
        )


class HumanPlayer(Player):
    """
    Human player class
    and print statements to explain the game
    """

    def __init__(self) -> None:
        super().__init__()
        self.name = input("Tell me the Name of your Hero: ")
        self.choose_class()

    def choose_class(self) -> None:
        """
        lets the player choose a class
        """
        user_input = self.get_input(
            list(range(1, len(self.available_player_classes) + 1)),
            "What Class you want to play?",
            "Paladin(1), Rogue(2): ",
        )
        self.set_attributes(self.available_player_classes[user_input - 1]())

    @staticmethod
    def get_input(valid: list, decorator: str, question: str) -> int:
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

    def get_move(self, player, target=None) -> int:
        return self.get_input(
            ["attack", "heal"],
            "What do you want to do?",
            "attack or heal: " if player.heal is not None else "attack: ",
        )
