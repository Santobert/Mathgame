from typing import List, Optional

from .const import END, START, SUM


class Number:
    def __init__(self, number: int, crossed: bool = False):
        self.number = number
        self.crossed = crossed

        self.successor_v: Optional[Number] = None
        self.successor_h: Optional[Number] = None
        self.predecessor_v: Optional[Number] = None
        self.predecessor_h: Optional[Number] = None

    def matches(self, other: Optional["Number"]) -> bool:
        if other is None:
            return False
        num_equal = self.number == other.number
        num_sum = self.number + other.number == SUM
        not_crossed = not (self.crossed or other.crossed)
        return (num_equal or num_sum) and not_crossed

    def __repr__(self) -> str:
        if self.crossed:
            return START + str(self.number) + END
        return str(self.number)


class AGame:
    def __init__(self, initial: List[int]):
        self.rows: List[List[Number]] = []
        self.rows.append([])

        for i in initial:
            self.add(i)

    def add(self, i: int):
        raise NotImplementedError()

    def check(self):
        to_add = []
        for row in self.rows:
            for num in row:
                if not num.crossed:
                    to_add.append(num.number)

        for i in to_add:
            self.add(i)

    def clear_crossed_rows(self):
        to_delete = []
        for i in range(len(self.rows) - 1):
            all_crossed = True
            for num in self.rows[i]:
                if not num.crossed:
                    all_crossed = False
                    break
            if all_crossed:
                to_delete.append(i)

        for i in range(len(to_delete)):
            del self.rows[to_delete[i] - i]

    def move(self) -> bool:
        raise NotImplementedError()

    def __repr__(self) -> str:
        result = ""
        for i in range(0, len(self.rows)):
            result += f"{i}. "
            for num in self.rows[i]:
                if num.crossed:
                    result = result + START + str(num.number) + END + " "
                else:
                    result = result + str(num.number) + " "
            result += "\n"
        return result.strip()
