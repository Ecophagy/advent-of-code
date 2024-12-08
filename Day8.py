
def read_input():
    grid = []
    with open("input/Day8.txt") as f:
        index = 0
        for line in f.readlines():
            row = []
            for char in line:
                if char != "\n":
                    row.append(char)
            index += 1
            grid.append(row)
    return grid

def draw_grid(grid):
    for count_row in range(0, len(grid)):
        for count_column in range(0, len(grid[0])):
            print(grid[count_row][count_column], end="")
        print("")

# Place antinode inside grid.
# Returns location of antinode, whether it is placed in an emptty space or covering an antenna
# Returns None is antinode location is invalid (outside the grid) or an antinode is already there (to avoid counting duplicates)
def add_antinode(grid, row, column):
    antinode_location = None
    if 0 <= row < len(grid) and 0 <= column < len(grid[0]):
        if grid[row][column] == ".":
            grid[row][column] = "#" # Add antinode to emtpy square
            antinode_location = row, column
        elif grid[row][column] != "#":
            antinode_location = row, column # Antinode covers existing antenna
    return antinode_location


def find_and_place_antinodes(grid, antinodes):
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if grid[row][column] != "." and grid[row][column] != "#":
                # This cell contains an antenna
                frequency = grid[row][column]
                # Find all matching frequency antennae
                for pair_row in range(len(grid)):
                    for pair_column in range(len(grid[0])):
                        if pair_row != row and pair_column != column: # Ignore self
                            if grid[pair_row][pair_column] == frequency:
                                row_difference  = pair_row - row
                                column_difference = pair_column - column
                                # Part 1 antinode locations
                                antinode_locations = [(row - row_difference, column - column_difference),
                                                      (pair_row + row_difference, pair_column + column_difference)]

                                # Part 2 node locations
                                # Are at every space along the line that passes between the two antenna locations
                                resonant_antinode_locations = []

                                # Line one way
                                base_row = pair_row
                                base_column = pair_column
                                while 0 <= base_row < len(grid) and 0 <= base_column < len(grid[0]):
                                    base_row += row_difference
                                    base_column += column_difference
                                    resonant_antinode_locations.append((base_row, base_column))

                                # Line the other way
                                base_row = pair_row
                                base_column = pair_column
                                while 0 <= base_row < len(grid) and 0 <= base_column < len(grid[0]):
                                    base_row -= row_difference
                                    base_column -= column_difference
                                    resonant_antinode_locations.append((base_row, base_column))

                                # Add and count antinodes
                                for location in resonant_antinode_locations:
                                    antinode = add_antinode(grid, location[0], location[1])
                                    if antinode is not None and antinode not in antinodes:
                                        antinodes.append(antinode)


if __name__ == "__main__":
    grid = read_input()

    antinodes = []
    find_and_place_antinodes(grid, antinodes)

    draw_grid(grid)
    print(f"Antinodes: {len(antinodes)}")
