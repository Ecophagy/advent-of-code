
def read_input():
    with open("input/Day9_example.txt") as f:
        return f.read()

def uncompress(disk_map):
    id = 0
    file = True
    disk = []
    for char in disk_map:
        if file:
            for i  in range(int(char)):
                disk.append(id)
            id += 1
        else:
            for i  in range(int(char)):
                disk.append(".")
        file = not file
    return disk

# Part 1
# By heck this is slow
def frag(disk):
    for i in range(len(disk)):
        if disk[i] == ".":
            for j in reversed(range(len(disk))):
                if j < i:
                    break
                if disk[j] != ".":
                    disk[i] = disk[j]
                    disk[j] = "."
                    break
    return disk

# Part 2
def defrag(disk):
    j = len(disk) - 1
    while j >= 0:
        if disk[j] != ".":
            file_index = j
            while disk[file_index] == disk[j]:
                file_index -= 1
            # File is between j-file_index and j
            file_size = j - file_index

            # Find gap from front
            for i in range(len(disk)):
                if disk[i] == ".":
                    gap_index = i
                    while gap_index < len(disk) and disk[gap_index] == ".":
                        gap_index += 1
                    # Gap is between i and i+gap_index
                    gap_size = gap_index - i

                    # Is the gap big enough?
                    if gap_size >= file_size:
                        fill_index = i
                        for k in range(file_index + 1, j + 1):
                            disk[fill_index] = disk[k]
                            disk[k] = "."
                            fill_index += 1
                            j -= file_size - 1
                        break
            j -= 1
    return disk


def calculate_checksum(disk):
    checksum = 0
    for i in range(len(disk)):
        if disk[i] != ".":
            checksum += int(disk[i]) * i
    return checksum


if __name__ == "__main__":
    disk_map = read_input()
    uncompressed_disk = uncompress(disk_map)
    #fragged_disk = frag(uncompressed_disk)
    defragged_disk = defrag(uncompressed_disk)
    print(defragged_disk)
    print(f"Checksum: {calculate_checksum(defragged_disk)}")
