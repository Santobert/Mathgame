from random import randint
from typing import List

from mathgame.lists import GameLists
from mathgame.numbers import GameNumbers


def generate(highest: int = 18) -> List[int]:
    if highest > 99:
        raise Exception("Max values above 99 are not supported")

    result = []
    for i in range(1, highest + 1):
        mod = i % 10
        div = i // 10

        if mod == 0:
            continue

        if div != 0:
            result.append(div)

        result.append(mod)

    return result


def random(length: int = 25) -> List[int]:
    result = []
    for i in range(0, length):  # pylint: disable=unused-variable
        result.append(randint(1, 9))
    return result


if __name__ == "__main__":
    initial = generate()
    # initial = random()

    # game = GameLists(initial)
    game = GameNumbers(initial)
    print(f"Initial setup:\n{game}\nStart:")

    moves = 0
    checks = 0
    while len(game.rows) > 1:
        current_moves = 0
        moved = True
        while moved:
            moved = game.move()
            if moved:
                current_moves += 1
                print("|", end="")
            else:
                print()
        crossed_rows = game.clear_crossed_rows()
        added_numbers = game.check()
        checks += 1
        moves += current_moves

        # print(f"{g}\n")
        print(
            f"Round {checks}; "
            + f"Numbers {added_numbers*2} (-{current_moves * 2}/+{added_numbers}); "
            + f"Rows {len(game.rows)} (-{crossed_rows})"
        )

    print(f"---\n{moves} moves and {checks} rounds until finished")
