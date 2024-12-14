
class Region:
    def __init__(self, type):
        self.type = type
        self.perimeter = 0
        self.coordinates = []

def read_input():
    grid = []
    with open("input/Day12.txt") as f:
        for line in f.readlines():
            row = []
            for char in line.rstrip():
                row.append(char)
            grid.append(row)
    return grid


def find_region(grid, row, column, region):
    region.coordinates.append((row, column))

    if row == 0 or grid[row - 1][column] != region.type:
        region.perimeter += 1
    else:
        if (row - 1, column) not in region.coordinates:
            region = find_region(grid, row - 1, column, region)

    if row >= len(grid) - 1 or grid[row + 1][column] != region.type:
        region.perimeter += 1
    else:
        if (row + 1, column) not in region.coordinates:
            region = find_region(grid, row + 1, column, region)

    if column >= len(grid[0]) - 1 or grid[row][column + 1] != region.type:
        region.perimeter += 1
    else:
        if (row, column + 1) not in region.coordinates:
            region = find_region(grid, row, column + 1, region)

    if column == 0 or grid[row][column - 1] != region.type:
        region.perimeter += 1
    else:
        if (row, column - 1) not in region.coordinates:
            region = find_region(grid, row, column - 1, region)

    return region

# Part 1
def calculate_cost(regions):
    cost = 0
    for region in regions:
        cost += len(region.coordinates) * region.perimeter
    return cost

# Part 2
def calculate_bulk_cost(regions):
    cost = 0
    for region in regions:
        # Sides == Corners
        corners = 0
        for row, column in region.coordinates:
            # Convex Corners: two diagonally adjacent cells are the same, but NOT the same as the cell in question
            if (row + 1, column) not in  region.coordinates and (row, column + 1) not in  region.coordinates:
                corners += 1
            if (row + 1, column) not in region.coordinates and (row, column - 1) not in region.coordinates:
                corners += 1
            if(row - 1, column) not in region.coordinates and (row, column + 1) not in region.coordinates:
                corners += 1
            if (row - 1, column) not in region.coordinates and (row, column - 1) not in region.coordinates:
                corners += 1

            # Concave Corners: two diagonally adjacent cells are the same, AND exactly one cell adjacent to both is the same as the cell in question, and the other it NOT
            # To avoid double counting, we only check in one diagonal direction
            if (row + 1, column + 1) in region.coordinates and (row + 1, column) in region.coordinates and (row, column + 1) not in region.coordinates:
                corners += 1
            if (row + 1, column + 1) in region.coordinates and (row, column + 1) in region.coordinates and (row + 1, column) not in region.coordinates:
                corners += 1
            if (row -1, column + 1) in region.coordinates and (row - 1, column) in region.coordinates and (row, column + 1) not in region.coordinates:
                corners += 1
            if (row - 1, column + 1) in region.coordinates and (row, column + 1) in region.coordinates and (row - 1, column) not in region.coordinates:
                corners += 1

        cost += len(region.coordinates) * corners
    return cost

if __name__ == "__main__":
    grid = read_input()
    regions = []
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            region_found = False
            for region in regions:
                if (row, column) in region.coordinates:
                    region_found = True
                    break
            if not region_found:
                regions.append(find_region(grid, row, column, Region(grid[row][column])))
    print(f"regular cost: {calculate_cost(regions)}")
    print(f"Bulk cost: {calculate_bulk_cost(regions)}")
