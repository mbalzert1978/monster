"""
Monster Game v0.1 (OO)
"""
import random

from HeroClass.hero_class import Paladin, Rogue
from Player.player_modul import Player, HumanPlayer, RandomCPUPlayer


class MonsterGame:
    """
    Game Class
    """

    rounds = 1

    def __init__(self, print_game: bool = False) -> None:
        self.current_winner: Player = None
        self.print_game = print_game

    def print_board(self, attack: Player, target: Player):
        """
        prints the board
        """
        print(f"{self.rounds}, Rounds played ")
        print(f"{attack.name}'s, remaining health: {attack.hero_class.health}")
        print(
            f"{target.name}'s, remaining health: {target.hero_class.health} "
        )

    def make_move(self, attack: Player, target: Player) -> None:
        """
        gets attacker move and makes the move happen
        """
        result, is_attack = attack.get_move()()
        if is_attack:
            if self.print_game:
                print(f"{attack.name} hits {target.name} for {result} damage.")
            target.hero_class.set_health(-result)
            return
        if self.print_game:
            print(f"{attack.name} heals himself for {result}.")
        attack.hero_class.set_health(result)

    def is_winner(self, attack: Player, target: Player) -> bool:
        """
        checks wincondition
        """
        if target.hero_class.health <= 0:
            self.current_winner = attack
            return True
        return False


def play(game, player1, player2):
    """Play game function"""
    attacker, target = shuffle_players([player1, player2])
    del player1, player2
    while not game.current_winner:
        if game.print_game:
            game.print_board(attacker, target)
        game.make_move(attacker, target)
        game.is_winner(attacker, target)
        attacker, target = target, attacker
        game.rounds += 1
    if game.print_game:
        print(
            f"{attacker.name} wins the Match.\
After {game.rounds} rounds."
        )
    return attacker.name


def shuffle_players(player_list) -> list[Player]:
    random.shuffle(player_list)
    return player_list[0], player_list[1]


if __name__ == "__main__":
    CPU1WINS = 0
    CPU2WINS = 0
    available_hero_classes = {"Paladin": Paladin, "Rogue": Rogue}
    # human = HumanPlayer(available_hero_classes)
    # random_cpu = RandomCPUPlayer(available_hero_classes)
    # monster_game = MonsterGame(print_game=True)
    # play(monster_game, human, random_cpu)

    # old code
    for _ in range(1000):
        # human_player = HumanPlayer()
        random_cpu = RandomCPUPlayer(
            name="random_cpu1", hero_classes=available_hero_classes
        )
        random_cpu2 = RandomCPUPlayer(
            name="random_cpu2", hero_classes=available_hero_classes
        )
        # better_cpu = BetterComputerPlayer("better_cpu")
        m = MonsterGame(False)
        result = play(m, random_cpu, random_cpu2)
        if "random_cpu1" in result:
            CPU1WINS += 1
        if "better_cpu" in result or "random_cpu2" in result:
            CPU2WINS += 1
    print(
        f"after 1000 rounds, we see random_cpu {CPU1WINS} \
wins, and better_cpu {CPU2WINS} wins"
    )
