from dataclasses import dataclass, field


@dataclass
class Calibration:
    target: int
    inputs: list[int]

def read_input():
    calibrations = []
    with open("input/Day7.txt") as f:
        for line in f.readlines():
            raw_calibration = line.split(":")
            raw_inputs = raw_calibration[1].split(" ")
            inputs = []
            for raw_input in raw_inputs:
                if raw_input != "":
                    inputs.append(int(raw_input))
            calibrations.append(Calibration(int(raw_calibration[0]), inputs))
    return calibrations

def fix_calibration(calibration):
    output = calc(calibration.inputs[0], calibration.inputs, 1)
    return check_answer(calibration.target, output)

# Recursively calculate all possible outputs
def calc(running_total, inputs, index):
    total_1 = running_total + inputs[index]
    total_2 = running_total * inputs[index]

    if index < len(inputs) - 1:
        index += 1
        return calc(total_1, inputs, index), calc(total_2, inputs, index)
    else:
        return total_1, total_2

# Recursively check the nested tuples of possible outputs for the target value
def check_answer(target, answers):
    for item in answers:
        if isinstance(item, tuple):
            if check_answer(target, item):
                return True
        else:
            if item == target:
                return True
    return False

if __name__ == "__main__":
    calibrations = read_input()
    total_calibration = 0
    for calibration in calibrations:
        if fix_calibration(calibration):
            total_calibration += calibration.target
    print(total_calibration)
