from enum import Enum

class orientation(Enum):
    NORTH = 0
    SOUTH = 1
    EAST = 2
    WEST = 3

def read_input():
    grid = []
    with open("input/Day6.txt") as f:
        index = 0
        for line in f.readlines():
            row = []
            for char in line:
                if char != "\n":
                    row.append(char)
            index += 1
            grid.append(row)
    return grid

def find_start_position(grid):
    for column in range(0, len(grid)):
        for row in range(0, len(grid[0])):
            if grid[column][row] == "^":
                return column, row

def move_guard(grid, position_column, position_row, guard_orientation):
    if guard_orientation == orientation.NORTH:
        # Check for obstacle
        if position_column != 0 and grid[position_column - 1][position_row] == "#":
            return position_column, position_row, orientation.EAST
        else:
            return position_column - 1, position_row, orientation.NORTH
    elif guard_orientation == orientation.EAST:
        # Check for obstacle
        if grid[position_column][position_row + 1] == "#":
            return position_column, position_row, orientation.SOUTH
        else:
            return position_column, position_row + 1, orientation.EAST
    elif guard_orientation == orientation.SOUTH:
        # Check for obstacle
        if grid[position_column + 1][position_row] == "#":
            return position_column, position_row, orientation.WEST
        else:
            return position_column + 1, position_row, orientation.SOUTH
    elif guard_orientation == orientation.WEST:
        # Check for obstacle
        if position_row != 0 and grid[position_column][position_row - 1] == "#":
            return position_column, position_row, orientation.NORTH
        else:
            return position_column, position_row - 1, orientation.WEST


if __name__ == "__main__":
    grid = read_input()
    guard_column, guard_row = find_start_position(grid)
    grid[guard_column][guard_row] = "X" # Mark starting position
    guard_orientation = orientation.NORTH
    guard_free = False
    while not guard_free:
        try:
            guard_column, guard_row, guard_orientation = move_guard(grid, guard_column, guard_row, guard_orientation)
            if guard_column < 0 or guard_row < 0:
                guard_free = True
            else:
                grid[guard_column][guard_row] = "X" # Mark square as visited. It might already be but that's fine.
        except IndexError:
            guard_free = True

    # Count Xs in grid
    spaces_covered = 0
    for column in range(0, len(grid)):
        for row in range(0, len(grid[0])):
            if grid[column][row] == "X":
                spaces_covered += 1
            print(grid[column][row], end='')
        print("")
    print(spaces_covered)