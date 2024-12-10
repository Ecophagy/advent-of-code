
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
                counter += len(step(grid, row, column, 0, 9))
    return counter


def step(grid, row, column, height, limit):
    peaks = []
    if height == limit:
        peaks.append((row, column))
        return peaks
    else:
        if row < len(grid) - 1 and grid[row + 1][column] == height + 1:
            out = step(grid, row + 1, column, height + 1, limit)
            for peak_location in out:
                if peak_location not in peaks:
                    peaks.append(peak_location)
        if row > 0 and grid[row - 1][column] == height + 1:
            for peak_location in step(grid, row - 1, column, height + 1, limit):
                if peak_location not in peaks:
                    peaks.append(peak_location)
        if column < len(grid[0]) - 1 and grid[row][column + 1] == height + 1:
            for peak_location in step(grid, row, column + 1, height + 1, limit):
                if peak_location not in peaks:
                    peaks.append(peak_location)
        if column > 0 and grid[row][column - 1] == height + 1:
            for peak_location in step(grid, row, column - 1, height + 1, limit):
                if peak_location not in peaks:
                    peaks.append(peak_location)
        return peaks

if __name__ == "__main__":
    grid = read_input()
    print_grid(grid)
    count = find_trails(grid)
    print(f"Total trailhead score: {count}")