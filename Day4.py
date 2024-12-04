
def read_input():
    grid = []
    with open("input/Day4.txt") as f:
        index = 0
        for line in f.readlines():
            row = []
            for char in line:
                if char != "\n":
                    row.append(char)
            index += 1
            grid.append(row)
    return grid

def find_xmas(grid):
    xmas_found = 0
    xmas_coords = []

    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid[i][j] == "X":
                for row_increment in range(-1,2):
                    for column_increment in range(-1,2):
                        # Skip case where we are checking the same letter itself
                        if row_increment == 0 and column_increment == 0:
                            continue
                        else:
                            row = i + row_increment
                            column = j + column_increment
                            try:
                                # row or column being < 0 will read from the end of the array, so ignore those cases
                                if row >= 0 and column >= 0 and grid[row][column] == "M":
                                    row += row_increment
                                    column += column_increment
                                    if row >= 0 and column >= 0 and grid[row][column] == "A":
                                        row += row_increment
                                        column += column_increment
                                        if row >= 0 and column >= 0 and grid[row][column] == "S":
                                            xmas_found += 1
                                            for k in range(4):
                                                xmas_coords.append((i+row_increment * k,j+column_increment*k))
                            except IndexError:
                                continue
    return xmas_found, xmas_coords

def find_x_mas(grid):
    x_mas_found = 0

    # -1 to not check when the centre is on the edge of grid
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            if grid[i][j] == "A":
                try:
                    if ((grid[i - 1][j - 1] == "M" and grid[i + 1][j + 1] == "S") or
                        (grid[i - 1][j - 1] == "S" and grid[i + 1][j + 1] == "M")) and \
                        ((grid[i + 1][j - 1] == "M" and grid[i - 1][j + 1] == "S") or
                         (grid[i + 1][j - 1] == "S" and grid[i - 1][j + 1] == "M")):
                            x_mas_found += 1
                except IndexError:
                    continue
    return x_mas_found


def print_grid(grid, coords):
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if (i,j) in coords:
                print(grid[i][j], end='')
            else:
                print(".", end='')
        print("")


if __name__ == "__main__":
    input = read_input()
    count, coords = find_xmas(input)
    count = find_x_mas(input)
    print(count)
