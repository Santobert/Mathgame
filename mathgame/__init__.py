from .const import END, START


class ANumber:
    def __init__(self, number: int, crossed: bool):
        self.number = number
        self.crossed = crossed

    def __repr__(self):
        if self.crossed:
            return START + str(self.number) + END
        else:
            return str(self.number)


class AGame:
    def __init__(self):
        self.rows = []
        self.rows.append([])

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
