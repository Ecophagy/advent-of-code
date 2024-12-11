from tqdm import tqdm

def read_input():
    stones = {}
    with open("input/Day11.txt") as f:
        for stone_string in f.read().split(" "):
            stone = int(stone_string)
            if stone in stones:
                stones[stone] += 1
            else:
                stones[stone] = 1
    return stones

def blink(stones):
    new_stones = {}
    for stone, count in stones.items():
        # Determine new stone(s) to add
        new_stone_list = []
        if stone == 0:
            new_stone_list.append(1)
        elif len(str(stone))  % 2 == 0:
            stone_string = list(str(stone))
            midpoint = int(len(stone_string)/2)
            for stone_string_list in [stone_string[:midpoint], stone_string[midpoint:]]:
                stone_string = ""
                for char in stone_string_list:
                    stone_string += char
                new_stone_list.append(int(stone_string))
        else:
            new_stone_list.append(stone * 2024)

        # Add one of these stones for each time it appears in the input
        for i in range(count):
            for new_stone in new_stone_list:
                if new_stone in new_stones:
                    new_stones[new_stone] += 1
                else:
                    new_stones[new_stone] = 1
    return new_stones


if __name__ == "__main__":
    stones = read_input()
    blinks = 75 # 25 for Part 1
    for i in tqdm(range(blinks)):
        stones = blink(stones)
    total_stones = 0
    for key, value in stones.items():
        total_stones += value
    print(f"Number of stones: {total_stones}")
