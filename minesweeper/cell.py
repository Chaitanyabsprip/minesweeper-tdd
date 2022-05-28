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
    is_explored: bool = field(default=False, init=False)

    def __post_init__(self):
        assert MINE <= self.value <= FLAG
