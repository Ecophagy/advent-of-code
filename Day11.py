
def read_input():
    stones = []
    with open("input/Day11.txt") as f:
        for stone in f.read().split(" "):
            stones.append(int(stone))
    return stones

def blink(stones):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone))  % 2 == 0:
            stone_string = list(str(stone))
            midpoint = int(len(stone_string)/2)
            for stone_string_list in [stone_string[:midpoint], stone_string[midpoint:]]:
                stone_string = ""
                for char in stone_string_list:
                    stone_string += char
                new_stones.append(int(stone_string))
        else:
            new_stones.append(stone * 2024)
    return new_stones


if __name__ == "__main__":
    stones = read_input()
    for i in range(25):
        stones = blink(stones)
    print(f"Number of stones: {len(stones)}")
