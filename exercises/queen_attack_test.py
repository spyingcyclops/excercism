class Queen:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        if self.row < 0:
            raise ValueError("row not positive")
        if self.column < 0:
            raise ValueError("column not positive")
        if self.column > 7:
            raise ValueError("column not on board")
        if self.row > 7:
            raise ValueError("row not on board")

    def can_attack(self, another_queen):
        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError("Invalid queen position: both queens in the same square")

        return (
            (
                abs(self.row - self.column)
                == abs(another_queen.row - another_queen.column)
            )
            or (
                abs(self.row - another_queen.row)
                == abs(self.column - another_queen.column)
            )
            or (self.row == another_queen.row)
            or (self.column == another_queen.column)
        )


w = Queen(2, 2)
b = Queen(3, 1)

print(Queen.can_attack(w, b))
