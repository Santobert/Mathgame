from mathgame.lists import GameLists
from mathgame.numbers import GameNumbers


initial = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    1,
    1,
    1,
    2,
    1,
    3,
    1,
    4,
    1,
    5,
    1,
    6,
    1,
    7,
    1,
    8,
]

if __name__ == "__main__":
    # g = GameLists(initial)
    g = GameNumbers(initial)
    moves = 0
    checks = 0
    while len(g.rows) > 1:
        checks += 1
        result = True
        while result:
            result = g.move()
            if result:
                moves += 1
        g.clear_crossed_rows()
        print(f"{g}\n")
        g.check()
    print(f"{moves} moves and {checks} checks until finished")
