from dataclasses import dataclass
import re

@dataclass
class Position:
    X: int
    Y: int

@dataclass
class Machine:
    button_a : Position
    button_b: Position
    prize_location: Position

def read_input():
    machines = []
    with open("input/Day13.txt") as f:
        lines = f.readlines()
        for i in range(0, len(lines), 4):
            button_regex = r"X\+(\d+), Y\+(\d+)"
            matches = re.findall(button_regex, lines[i])
            button_a_position = Position(int(matches[0][0]), int(matches[0][1]))
            matches = re.findall(button_regex, lines[i + 1])
            button_b_position = Position(int(matches[0][0]), int(matches[0][1]))
            prize_regex = r"X=(\d+), Y=(\d+)"
            matches = re.findall(prize_regex, lines[i + 2])
            prize_location = Position(int(matches[0][0]), int(matches[0][1]))
            machines.append(Machine(button_a_position, button_b_position, prize_location))
    return machines

if __name__ == "__main__":
    machines = read_input()
    print(machines)