from typing import Optional, Tuple

from . import AGame, Number
from .const import LINE_LENGTH


class GameLists(AGame):
    def add(self, i: int):
        number = Number(i)

        if len(self.rows[-1]) == LINE_LENGTH:
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

    def is_matching(self, row: int, col: int) -> Optional[Tuple[int, int]]:
        number = self.rows[row][col]

        hor = self.find_neighbor_horizontal(row, col)
        if hor is not None and number.matches(self.rows[hor[0]][hor[1]]):
            return hor

        vert = self.find_neighbor_vertical(row, col)
        if vert is not None and number.matches(self.rows[vert[0]][vert[1]]):
            return vert

        return None

    def find_neighbor_horizontal(self, row: int, col: int) -> Optional[Tuple[int, int]]:
        for j in range(col + 1, len(self.rows[row])):
            if not self.rows[row][j].crossed:
                return (row, j)

        for i in range(row + 1, len(self.rows)):
            for j in range(0, len(self.rows[i])):
                if not self.rows[i][j].crossed:
                    return (i, j)

        return None

    def find_neighbor_vertical(self, row: int, col: int) -> Optional[Tuple[int, int]]:
        for i in range(row + 1, len(self.rows)):
            if col < len(self.rows[i]) and not self.rows[i][col].crossed:
                return (i, col)

        return None
