from dataclasses import dataclass


@dataclass
class Dimension:
    number_of_columns: int
    number_of_rows: int

    def __post_init__(self):
        assert self.number_of_columns > 0 and self.number_of_rows > 0

    def get_number_of_cells(self):
        return self.number_of_rows * self.number_of_columns
