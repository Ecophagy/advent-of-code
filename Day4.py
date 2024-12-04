
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
    print_grid(input, coords)
    print(count)
