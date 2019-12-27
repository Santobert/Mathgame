class Number:
    def __init__(self, number: int, crossed: bool = False):
        self.number = number
        self.crossed = crossed

    def matches(self, other) -> bool:
        num_equal = self.number == other.number
        num_sum = self.number + other.number == 10
        not_crossed = not (self.crossed or other.crossed)
        return (num_equal or num_sum) and not_crossed


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

    def cross(self, row: int, col: int):
        self.rows[row][col].crossed = True

    def move(self) -> bool:
        for i in range(0, len(self.rows)):
            for j in range(0, len(self.rows[i])):
                match = self.is_matching(i, j)
                if match:
                    self.cross(i, j)
                    self.cross(match[0], match[1])
                    return True

        return False

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

    def is_matching(self, row: int, col: int):
        number = self.rows[row][col]

        hor = self.find_neighbor_horizontal(row, col)
        if hor is not None and number.matches(self.rows[hor[0]][hor[1]]):
            return hor

        vert = self.find_neighbor_vertical(row, col)
        if vert is not None and number.matches(self.rows[vert[0]][vert[1]]):
            return vert

    def find_neighbor_horizontal(self, row: int, col: int):

        # Search in this row
        for j in range(col + 1, len(self.rows[row])):
            if not self.rows[row][j].crossed:
                return (row, j)

        # Search in the following rows
        for i in range(row + 1, len(self.rows)):
            for j in range(0, len(self.rows[i])):
                if not self.rows[i][j].crossed:
                    return (i, j)

    def find_neighbor_vertical(self, row: int, col: int):

        for i in range(row + 1, len(self.rows)):
            if col < len(self.rows[i]) and not self.rows[i][col].crossed:
                return (i, col)

    def __repr__(self):
        start = "\033[4m"
        end = "\033[0m"
        s = ""
        for i in range(0, len(self.rows)):
            s += f"{i}. "
            for n in self.rows[i]:
                if n.crossed:
                    s = s + start + str(n.number) + end + " "
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
