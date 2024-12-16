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

def brute_force_solver(machine):
    # Find all possible solutions for X location
    x_solutions = []
    for i in range(101):
        for j in range(101):
            if i * machine.button_a.X + j * machine.button_b.X == machine.prize_location.X:
                x_solutions.append((i, j))

    # Find all possible solutions for Y location
    y_solutions = []
    for i in range(101):
        for j in range(101):
            if i * machine.button_a.Y + j * machine.button_b.Y == machine.prize_location.Y:
                y_solutions.append((i, j))

    # Find which X and Y solutions are both valid
    matching_solutions = []
    for solution in x_solutions:
        if solution in y_solutions:
            matching_solutions.append(solution)

    if not matching_solutions:
        # No solutions, so prize is not accessible
        return None
    else:
        # Find minimal cost solution
        min_solution = None
        for solution in matching_solutions:
            value = solution[0] * 3 + solution[1]
            if min_solution is None or value < min_solution:
                min_solution = value
        return min_solution

if __name__ == "__main__":
    machines = read_input()
    tokens = 0
    for machine in machines:
        solution = brute_force_solver(machine)
        if solution is not None:
            tokens += solution
    print(f"Total token: {tokens}")