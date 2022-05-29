from dataclasses import dataclass, field

FLAG = 9
MINE = -1


@dataclass(frozen=True)
class Position:
    x: int
    y: int

    def __post_init__(self):
        assert self.x >= 0 and self.y >= 0


@dataclass(frozen=True)
class Cell:
    value: int
    position: Position
    is_explored: bool = field(default=False)

    def __post_init__(self):
        assert MINE <= self.value <= FLAG

    def is_adjacent_to(self, cell):
        is_horizontally_adjacent = abs(cell.position.x - self.position.x) <= 1
        is_vertically_adjacent = abs(cell.position.y - self.position.y) <= 1
        return is_horizontally_adjacent and is_vertically_adjacent

    def mark_as_explored(self):
        return Cell(self.value, self.position, True)
