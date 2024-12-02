

if __name__ == "__main__":
    left_list = []
    right_list = []
    with open("input/Day1.txt") as f:
        lines = f.readlines()
        for line in lines:
            left, right = line.split("   ")
            left_list.append(int(left))
            right_list.append(int(right))

    left_list.sort()
    right_list.sort()

    total_difference = 0
    for i in range(0, len(left_list)):
        difference = abs(left_list[i] - right_list[i])
        total_difference += difference

    print(total_difference)