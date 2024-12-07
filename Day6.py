from dataclasses import dataclass
from enum import Enum

class orientation(Enum):
    NORTH = 0
    SOUTH = 1
    EAST = 2
    WEST = 3

@dataclass
class Collision:
    obstacle_row: int
    obstacle_column: int
    collision_orientation: orientation

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
    for row in range(0, len(grid)):
        for column in range(0, len(grid[0])):
            if grid[row][column] == "^":
                return row, column

def step_guard(grid, position_row, position_column, guard_orientation):
    if guard_orientation == orientation.NORTH:
        # Check for obstacle
        if position_row != 0 and grid[position_row - 1][position_column] == "#":
            return position_row, position_column, orientation.EAST, Collision(position_row - 1, position_column, orientation.NORTH)
        else:
            return position_row - 1, position_column, orientation.NORTH, None

    elif guard_orientation == orientation.EAST:
        # Check for obstacle
        if grid[position_row][position_column + 1] == "#":
            return position_row, position_column, orientation.SOUTH, Collision(position_row, position_column + 1, orientation.EAST)
        else:
            return position_row, position_column + 1, orientation.EAST, None

    elif guard_orientation == orientation.SOUTH:
        # Check for obstacle
        if grid[position_row + 1][position_column] == "#":
            return position_row, position_column, orientation.WEST, Collision(position_row + 1, position_column, orientation.SOUTH)
        else:
            return position_row + 1, position_column, orientation.SOUTH, None

    elif guard_orientation == orientation.WEST:
        # Check for obstacle
        if position_column != 0 and grid[position_row][position_column - 1] == "#":
            return position_row, position_column, orientation.NORTH, Collision(position_row, position_column - 1, orientation.WEST)
        else:
            return position_row, position_column - 1, orientation.WEST, None


def move_guard(grid, guard_row, guard_column, guard_orientation):
    guard_free = False
    collisions = []
    while not guard_free:
        try:
            guard_row, guard_column, guard_orientation, collision = step_guard(grid, guard_row, guard_column, guard_orientation)
            if collision is not None:
                if collision in collisions:
                    # We have hit this obstacle from this direction before, so the guard must be stuck in a loop
                    guard_free = False
                    break
                else:
                    collisions.append(collision)
            if guard_column < 0 or guard_row < 0:
                guard_free = True
            else:
                grid[guard_row][guard_column] = "X"  # Mark square as visited. It might already be but that's fine.
        except IndexError:
            guard_free = True
    return guard_free


if __name__ == "__main__":
    grid = read_input()
    start_guard_row, start_guard_column = find_start_position(grid)
    grid[start_guard_row][start_guard_column] = "X" # Mark starting position

    # Part 1
    guard_row = start_guard_row
    guard_column = start_guard_column
    guard_orientation = orientation.NORTH
    if move_guard(grid, guard_row, guard_column, guard_orientation):
        # Guard escaped!
        # Count Xs in grid
        spaces_covered = 0
        for count_row in range(0, len(grid)):
            for count_column in range(0, len(grid[0])):
                if grid[count_row][count_column] == "X":
                    spaces_covered += 1
        print(f"Guard escaped! Spaces covered: {spaces_covered}")

    # Part 2
    loops = 0
    for row in range(0, len(grid)):
        for column in range(0, len(grid[0])):
            if column == start_guard_column and row == start_guard_row:
                # We can't put an obstacle at the guard's starting location
                continue
            else:
                if grid[row][column] == "#":
                    # Skip existing obstacles, since this will not change the map and add a loop
                    continue
                else:
                    grid[row][column] = "#"
                    guard_row = start_guard_row
                    guard_column = start_guard_column
                    guard_orientation = orientation.NORTH

                    if move_guard(grid, guard_row, guard_column, guard_orientation):
                        # Guard escaped!
                        print(f"Guard escaped!")
                    else:
                        # Guard stuck in loop
                        loops += 1
                        print("Guard stuck in loop")
                    # Remove the obstacle we tried
                    grid[row][column] = "."

    print(f"Total loops: {loops}")

