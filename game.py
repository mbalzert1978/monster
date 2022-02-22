"""
Monster Game v0.1 (OO)
"""
import random
from Player.player import (
    HumanPlayer,
    RandomComputerPlayer,
    BetterComputerPlayer,
)


class MonsterGame:
    """
    Game Class
    """

    rounds = 1

    def __init__(self, print_game=False) -> None:
        self.current_winner = None
        self.print_game = print_game

    @staticmethod
    def make_move(attacker, target, print_game=True):
        """
        gets attacker move and makes the move happen
        """
        if attacker.get_move(attacker, target) == "attack":
            attack = random.choice(
                list(range(attacker.attack_min, attacker.attack_max + 1))
            )
            if print_game:
                print(
                    f"{attacker.name} hits {target.name} for {attack} damage."
                )
            target.health -= attack
            return True
        if attacker.get_move(attacker, target) == "heal":
            if print_game:
                print(f"{attacker.name} heals himself for {attacker.heal}.")
            attacker.health += attacker.heal
            return True
        return False

    @staticmethod
    def is_health_zero(player) -> bool:
        """
        checks if any player has 0 health
        """
        if player.health <= 0:
            return True
        return False

    def is_winner(self, player, target) -> bool:
        """
        checks wincondition
        """
        result = self.is_health_zero(target)
        if result:
            self.current_winner = player
        return result


def play(game, player1, player2, print_game=True):
    """Play game function"""
    shuffle_players = [player1, player2]
    random.shuffle(shuffle_players)
    attacker, target = shuffle_players[0], shuffle_players[1]
    # target = player2
    while not game.current_winner:
        if print_game:
            game.print_board(attacker, target)
        game.make_move(attacker, target, print_game)
        game.is_winner(attacker, target)
        if game.current_winner:
            if print_game:
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
    for _ in range(1000):
        # human_player = HumanPlayer()
        random_cpu = RandomComputerPlayer("random_cpu1")
        random_cpu2 = RandomComputerPlayer("random_cpu2")
        better_cpu = BetterComputerPlayer("better_cpu")
        m = MonsterGame(False)
        result = play(m, random_cpu, random_cpu2, False)
        if "random_cpu1" in result:
            CPU1WINS += 1
        if "better_cpu" in result or "random_cpu2" in result:
            CPU2WINS += 1
    print(
        f"after 1000 rounds, we see random_cpu {CPU1WINS} \
wins, and better_cpu {CPU2WINS} wins"
    )
