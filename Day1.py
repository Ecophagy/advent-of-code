
def read_list():
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
    return left_list, right_list

# Part 1 Solution
def list_difference(left_list, right_list):
    total_difference = 0
    for i in range(0, len(left_list)):
        difference = abs(left_list[i] - right_list[i])
        total_difference += difference

    print(total_difference)

# Part 2 Solution
def list_similarity(left_list, right_list):
    similarity_score = 0
    for left_number in left_list:
        for right_number in right_list:
            if left_number == right_number:
                similarity_score = similarity_score + left_number
            elif right_number > left_number:
                # Lists are sorted, so no need to keep checking
                break
    print(similarity_score)



if __name__ == "__main__":
    left_list, right_list = read_list()
    list_difference(left_list, right_list)
    list_similarity(left_list, right_list)