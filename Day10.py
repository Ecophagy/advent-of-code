
def read_input():
    grid = []
    with open("input/Day10.txt") as f:
        index = 0
        for line in f.readlines():
            row = []
            for char in line:
                if char != "\n":
                    row.append(int(char))
            index += 1
            grid.append(row)
    return grid

def print_grid(grid):
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            print(grid[i][j], end='')
        print("")

def find_trails(grid):
    counter = 0
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if grid[row][column] == 0:
                counter += len(step_part_2(grid, row, column, 0, 9))
    return counter


# Part 1: Find each head that a trailhead can reach by recursively walking paths until we reach the limit.
# We need to track which heads we have reached from a trailhead because we ONLY count how many peaks we can reach
# Not how many different routes there are to get there
def step_part_1(grid, row, column, height, limit):
    peaks = []
    if height == limit:
        peaks.append((row, column))
        return peaks
    else:
        if row < len(grid) - 1 and grid[row + 1][column] == height + 1:
            for peak_location in step_part_1(grid, row + 1, column, height + 1, limit):
                if peak_location not in peaks:
                    peaks.append(peak_location)
        if row > 0 and grid[row - 1][column] == height + 1:
            for peak_location in step_part_1(grid, row - 1, column, height + 1, limit):
                if peak_location not in peaks:
                    peaks.append(peak_location)
        if column < len(grid[0]) - 1 and grid[row][column + 1] == height + 1:
            for peak_location in step_part_1(grid, row, column + 1, height + 1, limit):
                if peak_location not in peaks:
                    peaks.append(peak_location)
        if column > 0 and grid[row][column - 1] == height + 1:
            for peak_location in step_part_1(grid, row, column - 1, height + 1, limit):
                if peak_location not in peaks:
                    peaks.append(peak_location)
        return peaks

# Part 2: This time we DO care about the different routes, so just remove the "if already visited" check
# Could be simplified by having an int counter instead of an array, but this keeps the API the same.
# This was the original algorithm - solving part 2 first is a new experience!
def step_part_2(grid, row, column, height, limit):
    peaks = []
    if height == limit:
        peaks.append((row, column))
        return peaks
    else:
        if row < len(grid) - 1 and grid[row + 1][column] == height + 1:
            for peak_location in step_part_2(grid, row + 1, column, height + 1, limit):
                peaks.append(peak_location)
        if row > 0 and grid[row - 1][column] == height + 1:
            for peak_location in step_part_2(grid, row - 1, column, height + 1, limit):
                peaks.append(peak_location)
        if column < len(grid[0]) - 1 and grid[row][column + 1] == height + 1:
            for peak_location in step_part_2(grid, row, column + 1, height + 1, limit):
                peaks.append(peak_location)
        if column > 0 and grid[row][column - 1] == height + 1:
            for peak_location in step_part_2(grid, row, column - 1, height + 1, limit):
                peaks.append(peak_location)
        return peaks


if __name__ == "__main__":
    grid = read_input()
    count = find_trails(grid)
    print(f"Total trailhead score: {count}")