class Solver:
    def __init__(self):
        self.grid = [
            list(map(self.change_to_int, input().split(" "))),
            list(map(self.change_to_int, input().split(" "))),
            list(map(self.change_to_int, input().split(" ")))
        ]

    def start_solving(self):
        # print_grid(grid)

        for i in range(3):
            self.check_row(i)
            self.check_column(i)

        while self.is_incomplete():
            #self.print_grid()
            for difference in range(4, 6):
                previous_grid = [x[:] for x in self.grid]
                if self.set_random_value(difference):
                    break
                else:
                    self.grid = previous_grid
        self.print_grid()

    def set_random_value(self, difference):
        for r in range(3):
            for c in range(3):
                if self.grid[r][c] == "X":
                    if c == 0:
                        if self.grid[r][1] != "X":
                            return self.set_value(r, c, self.grid[r][1] - difference)
                        elif self.grid[r][2] != "X":
                            return self.set_value(r, c, self.grid[r][2] - 2 * difference)
                        else:
                            break
                    else:
                        return self.set_value(r, c, self.grid[r][c - 1] + difference)

        for c in range(3):
            for r in range(3):
                if self.grid[r][c] == "X":
                    if r == 0:
                        if self.grid[1][c] != "X":
                            return self.set_value(r, c, self.grid[1][c] - difference)

                        elif self.grid[2][c] != "X":
                            return self.set_value(r, c, self.grid[2][c] - 2 * difference)
                        else:
                            break
                    else:
                        return self.set_value(r, c, self.grid[r - 1][c] + difference)
        return self.set_value(0, 0, 0)

    def set_value(self, row_index, column_index, value):
        self.grid[row_index][column_index] = value

        return self.check_row(row_index) and self.check_column(column_index)

    def check_row(self, row_index):
        row = self.grid[row_index]
        numberOfXs = self.get_number_of_x(row)
        if numberOfXs == 0:
            return row[1] - row[0] == row[2] - row[1]
        if numberOfXs == 1:
            if row[0] == "X":
                difference = row[2] - row[1]
                if not self.set_value(row_index, 0, row[1] - difference):
                    return False
            elif row[1] == "X":
                difference = (row[2] - row[0])
                if difference % 2 == 1:
                    return False
                if not self.set_value(row_index, 1, row[0] + int(difference / 2)):
                    return False
            else:
                difference = row[1] - row[0]
                if not self.set_value(row_index, 2, row[1] + difference):
                    return False
        return True

    def check_column(self, column_index):
        numberOfXs = self.get_number_of_x_in_column(column_index)
        if numberOfXs == 0:
            return self.grid[1][column_index] - self.grid[0][column_index] == self.grid[2][column_index] - self.grid[1][column_index]
        if numberOfXs == 1:
            if self.grid[0][column_index] == "X":
                difference = self.grid[2][column_index] - self.grid[1][column_index]
                if not self.set_value(0, column_index, self.grid[1][column_index] - difference):
                    return False
            elif self.grid[1][column_index] == "X":
                difference = (self.grid[2][column_index] - self.grid[0][column_index])
                if difference % 2 == 1:
                    return False
                if not self.set_value(1, column_index, self.grid[0][column_index] + int(difference / 2)):
                    return False
            else:
                difference = self.grid[1][column_index] - self.grid[0][column_index]
                if not self.set_value(2, column_index, self.grid[1][column_index] + difference):
                    return False
        return True

    def is_incomplete(self):
        for row in self.grid:
            for char in row:
                if char == "X":
                    return True
        return False

    def print_grid(self):
        for row in self.grid:
            for char in row:
                print(char, end=" ")
            print()

    def get_number_of_x(self, row):
        numberOfX = 0
        for char in row:
            if char == "X":
                numberOfX += 1
        return numberOfX

    def get_number_of_x_in_column(self, columnNumber):
        numberOfX = 0
        for rowIndex in range(3):
            if self.grid[rowIndex][columnNumber] == "X":
                numberOfX += 1
        return numberOfX

    def change_to_int(self, value):
        if value == "X":
            return "X"
        return int(value)


def main():
    Solver().start_solving()


if __name__ == "__main__":
    main()
