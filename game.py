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

    def print_board(self, active_player, target):
        """
        prints the board
        """
        print(f"{self.rounds}, Rounds played ")
        print(
            f"{active_player.name}'s, remaining health: {active_player.hero_class.health}"
        )
        print(
            f"{target.name}'s, remaining health: {target.hero_class.health} "
        )

    def make_move(self, attacker, target):
        """
        gets attacker move and makes the move happen
        """
        result, is_attack = attacker.get_move()()
        if self.print_game and is_attack:
            print(f"{attacker.name} hits {target.name} for {result} damage.")
            target.hero_class.set_health(-result)
        else:
            print(f"{attacker.name} heals himself for {result}.")
            attacker.hero_class.set_health(result)

    def is_winner(self, player, target) -> bool:
        """
        checks wincondition
        """
        if target.hero_class.health <= 0:
            self.current_winner = player
            return True
        return False


def play(game, player1, player2):
    """Play game function"""
    shuffle_players = [player1, player2]
    random.shuffle(shuffle_players)
    attacker, target = shuffle_players[0], shuffle_players[1]
    del player1, player2, shuffle_players
    while not game.current_winner:
        if game.print_game:
            game.print_board(attacker, target)
        game.make_move(attacker, target)
        game.is_winner(attacker, target)
        if game.current_winner:
            if game.print_game:
                print(
                    f"{attacker.name} wins the Match.\
After {game.rounds} rounds."
                )
            return attacker.name
        attacker, target = target, attacker
        game.rounds += 1


if __name__ == "__main__":
    CPU1WINS = 0
    CPU2WINS = 0
    available_hero_classes = {"Paladin": Paladin, "Rogue": Rogue}
    human = HumanPlayer(available_hero_classes)
    random_cpu = RandomCPUPlayer(available_hero_classes)
    monster_game = MonsterGame(print_game=True)
    play(monster_game, human, random_cpu)

    # old code
    #     for _ in range(1000):
    #         # human_player = HumanPlayer()
    #         random_cpu = RandomComputerPlayer("random_cpu1")
    #         random_cpu2 = RandomComputerPlayer("random_cpu2")
    #         better_cpu = BetterComputerPlayer("better_cpu")
    #         m = MonsterGame(False)
    #         result = play(m, random_cpu, random_cpu2, False)
    #         if "random_cpu1" in result:
    #             CPU1WINS += 1
    #         if "better_cpu" in result or "random_cpu2" in result:
    #             CPU2WINS += 1
    #     print(
    #         f"after 1000 rounds, we see random_cpu {CPU1WINS} \
    # wins, and better_cpu {CPU2WINS} wins"
    #     )
