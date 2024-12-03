import re

def read_data():
    with open("input/Day3.txt") as f:
        return f.read()

def find_multiply_commands_naive(data):
    multiply_commands = []
    regex = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(regex, data)
    for match in matches:
        multiply_commands.append(match)
    return multiply_commands

def find_enabled_multiplies(data):
    multiply_commands = []
    regex = r"(^|do\(\))(.*?)(don't\(\)|$)" # Requires input to be on one line
    matches = re.findall(regex, data)
    for match in matches:
        multiply_commands += (find_multiply_commands_naive(match[1]))
    return multiply_commands

if __name__ == "__main__":
    data = read_data()
    multiplies = []
    commands = find_enabled_multiplies(data)
    total = 0
    for command in commands:
        total = total + int(command[0]) * int(command[1])
    print(total)
