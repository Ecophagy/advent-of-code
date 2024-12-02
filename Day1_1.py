
def read_list():
    left_list = []
    right_list = []
    with open("input/Day1.txt") as f:
        lines = f.readlines()
        for line in lines:
            left, right = line.split("   ")
            left_list.append(int(left))
            right_list.append(int(right))

    return left_list, right_list

# Part 1 Solution
def list_difference(left_list, right_list):
    left_list.sort()
    right_list.sort()

    total_difference = 0
    for i in range(0, len(left_list)):
        difference = abs(left_list[i] - right_list[i])
        total_difference += difference

    print(total_difference)


if __name__ == "__main__":
    left_list, right_list = read_list()
    list_difference(left_list, right_list)