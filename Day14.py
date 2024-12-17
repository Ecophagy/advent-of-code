from dataclasses import dataclass
import re
import math

@dataclass
class Position:
    column: int
    row: int

@dataclass
class Robot:
    position: Position
    velocity: Position

GRID_HEIGHT = 103
GRID_WIDTH = 101

def read_input():
    robots = []
    with open("input/Day14.txt") as f:
        robot_regex = r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)"
        matches = re.findall(robot_regex, f.read())
        for match in matches:
            # NOTE: Inputs are X, Y where X is horizontal velocity (i.e. columns) and Y is vertical (rows)
            robot_position = Position(int(match[0]), int(match[1]))
            robot_velocity = Position(int(match[2]), int(match[3]))
            robots.append(Robot(robot_position, robot_velocity))
    return robots

def move_robot(robot):
    new_position_row = robot.position.row + robot.velocity.row
    if new_position_row < 0:
        new_position_row = new_position_row + GRID_HEIGHT
    elif new_position_row >= GRID_HEIGHT:
        new_position_row = new_position_row - GRID_HEIGHT

    new_position_column = robot.position.column + robot.velocity.column
    if new_position_column < 0:
        new_position_column = new_position_column + GRID_WIDTH
    elif new_position_column >= GRID_WIDTH:
        new_position_column = new_position_column - GRID_WIDTH

    robot.position = Position(new_position_column, new_position_row)
    return robot

def calculate_safety_factor(robots):
    quadrants = []
    quadrants.append(calculate_quadrant_safety_factor(0, math.floor(GRID_HEIGHT/2), 0, math.floor(GRID_WIDTH/2), robots))
    quadrants.append(calculate_quadrant_safety_factor(0, math.floor(GRID_HEIGHT/2), math.ceil(GRID_WIDTH/2), GRID_WIDTH, robots))
    quadrants.append(calculate_quadrant_safety_factor(math.ceil(GRID_HEIGHT/2), GRID_HEIGHT, 0, math.floor(GRID_WIDTH/2), robots))
    quadrants.append(calculate_quadrant_safety_factor(math.ceil(GRID_HEIGHT/2), GRID_HEIGHT, math.ceil(GRID_WIDTH/2), GRID_WIDTH, robots))

    safety_factor = 1
    for quadrant in quadrants:
        safety_factor = safety_factor * quadrant

    return safety_factor

def calculate_quadrant_safety_factor(lower_limit_row, upper_limit_row, lower_limit_column, upper_limit_column, robots):
    robot_count = 0
    for row in range(lower_limit_row, upper_limit_row):
        for column in range(lower_limit_column, upper_limit_column):
            for robot in robots:
                if robot.position.row == row and robot.position.column == column:
                    robot_count += 1
    return robot_count

def draw_grid(robots):
    for row in range(GRID_HEIGHT):
        for column in range(GRID_WIDTH):
            robot_count = 0
            for robot in robots:
                if robot.position.row == row and robot.position.column == column:
                    robot_count += 1
            if robot_count > 0:
                print(robot_count, end='')
            else:
                print(".", end='')
        print("")

if __name__ == "__main__":
    robots = read_input()
    for i in range(100):
        for r in range(len(robots)):
            robots[r] = move_robot(robots[r])
    print(calculate_safety_factor(robots))
