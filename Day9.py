
def read_input():
    with open("input/Day9.txt") as f:
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

def calculate_checksum(disk):
    checksum = 0
    for i in range(len(disk)):
        if disk[i] != ".":
            checksum += int(disk[i]) * i
    return checksum


if __name__ == "__main__":
    disk_map = read_input()
    uncompressed_disk = uncompress(disk_map)
    fragged_disk = frag(uncompressed_disk)

    print(f"Checksum: {calculate_checksum(fragged_disk)}")
