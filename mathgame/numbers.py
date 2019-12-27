from typing import Optional, Tuple

from . import AGame, Number
from .const import LINE_LENGTH


class GameNumbers(AGame):
    def add(self, i: int):
        number = Number(i)

        if len(self.rows[-1]) == LINE_LENGTH:
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

    def cross(self, number: Number):
        number.crossed = True
        if number.predecessor_h is not None:
            number.predecessor_h.successor_h = number.successor_h
        if number.predecessor_v is not None:
            number.predecessor_v.successor_v = number.successor_v
        if number.successor_h is not None:
            number.successor_h.predecessor_h = number.predecessor_h
        if number.successor_v is not None:
            number.successor_v.predecessor_v = number.predecessor_v

    def move(self) -> bool:
        for i in range(0, len(self.rows)):
            for j in range(0, len(self.rows[i])):
                num = self.rows[i][j]
                match = None
                if num.matches(num.successor_h):
                    match = num.successor_h
                elif num.matches(num.successor_v):
                    match = num.successor_v

                if match is not None:
                    self.cross(num)
                    self.cross(match)
                    return True

        return False

    def find_pred_horizontal(self, row: int, col: int) -> Optional[Tuple[int, int]]:
        for j in range(col - 1, -1, -1):
            if not self.rows[row][j].crossed:
                return (row, j)

        for i in range(row - 1, -1, -1):
            for j in range(len(self.rows[i]) - 1, -1, -1):
                if not self.rows[i][j].crossed:
                    return (i, j)

        return None

    def find_pred_vertical(self, row: int, col: int) -> Optional[Tuple[int, int]]:
        for i in range(row - 1, -1, -1):
            if not self.rows[i][col].crossed:
                return (i, col)

        return None
