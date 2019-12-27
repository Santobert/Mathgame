START = "\033[4m"
END = "\033[0m"


class Number:
    def __init__(self, number: int, crossed: bool = False):
        self.number = number
        self.crossed = crossed

        self.successor_v = None
        self.successor_h = None
        self.predecessor_v = None
        self.predecessor_h = None

    def matches(self, other) -> bool:
        if other is None:
            return False
        num_equal = self.number == other.number
        num_sum = self.number + other.number == 10
        not_crossed = not (self.crossed or other.crossed)
        return (num_equal or num_sum) and not_crossed

    def __repr__(self):
        if self.crossed:
            return START + str(self.number) + END
        else:
            return str(self.number)


class Game:
    def __init__(self):
        _initial = [
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
        self.rows = []
        self.rows.append([])
        for i in _initial:
            self.add(Number(i))

    def add(self, number: Number):
        if len(self.rows[-1]) == 9:
            self.rows.append([])
        self.rows[-1].append(number)
        i = len(self.rows) - 1
        j = len(self.rows[-1]) - 1

        pred_h = self.find_pred_horizontal(i, j)
        if pred_h is not None:
            x = pred_h[0]
            y = pred_h[1]
            self.rows[x][y].successor_h = self.rows[i][j]
            self.rows[i][j].predecessor_h = self.rows[x][y]

        pred_v = self.find_pred_vertical(i, j)
        if pred_v is not None:
            x = pred_v[0]
            y = pred_v[1]
            self.rows[x][y].successor_v = self.rows[i][j]
            self.rows[i][j].predecessor_v = self.rows[x][y]

    def find_pred_horizontal(self, row: int, col: int):
        for j in range(col - 1, -1, -1):
            if not self.rows[row][j].crossed:
                return (row, j)

        for i in range(row - 1, -1, -1):
            for j in range(len(self.rows[i]) - 1, -1, -1):
                if not self.rows[i][j].crossed:
                    return (i, j)

    def find_pred_vertical(self, row: int, col: int):
        for i in range(row - 1, -1, -1):
            if not self.rows[i][col].crossed:
                return (i, col)

    def cross(self, n: Number):
        n.crossed = True
        if n.predecessor_h is not None:
            n.predecessor_h.successor_h = n.successor_h
        if n.predecessor_v is not None:
            n.predecessor_v.successor_v = n.successor_v
        if n.successor_h is not None:
            n.successor_h.predecessor_h = n.predecessor_h
        if n.successor_v is not None:
            n.successor_v.predecessor_v = n.predecessor_v

    def move(self) -> bool:
        for i in range(0, len(self.rows)):
            for j in range(0, len(self.rows[i])):
                n = self.rows[i][j]
                match = None
                if n.matches(n.successor_h):
                    match = n.successor_h
                elif n.matches(n.successor_v):
                    match = n.successor_v

                if match is not None:
                    self.cross(n)
                    self.cross(match)
                    return True

    def check(self):
        to_add = []
        for row in self.rows:
            for n in row:
                if not n.crossed:
                    to_add.append(n.number)

        for n in to_add:
            self.add(Number(n))

    def clear_crossed_rows(self):
        to_delete = []
        for i in range(len(self.rows) - 1):
            all_crossed = True
            for n in self.rows[i]:
                if not n.crossed:
                    all_crossed = False
                    break
            if all_crossed:
                to_delete.append(i)

        for i in range(len(to_delete)):
            del self.rows[to_delete[i] - i]

    def __repr__(self):
        s = ""
        for i in range(0, len(self.rows)):
            s += f"{i}. "
            for n in self.rows[i]:
                if n.crossed:
                    s = s + START + str(n.number) + END + " "
                else:
                    s = s + str(n.number) + " "
            s += "\n"
        return s.strip()


if __name__ == "__main__":
    g = Game()
    moves = 0
    while len(g.rows) > 1:
        moves += 1
        result = True
        while result:
            result = g.move()
        g.clear_crossed_rows()
        print(f"{g}\n")
        g.check()
    print(f"{moves} moves until finished")
