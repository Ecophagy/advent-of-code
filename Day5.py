import math

def parse_rules():
    rules = {}
    with open("input/Day5_rules.txt") as f:
        for line in f.readlines():
            rule = line.split("|")
            key = int(rule[0])
            value = int(rule[1])
            if key in rules:
                rules[key].append(value)
            else:
                rules[key] = [value]
    return rules

def parse_updates():
    updates = []
    with open("input/Day5_updates.txt") as f:
        for line in f.readlines():
            update = []
            for char in line.split(","):
                update.append(int(char))
            updates.append(update)
    return updates

def validate_update(rules, update):
    index = 0
    for page in update:
        if page in rules:
            for i in range(0,index):
                if update[i] in rules[page]:
                    return False
        index += 1
    return True

def calculate_middle_page_sum(valid_updates):
    middle_page_sum = 0
    for update in valid_updates:
        middle_index = math.floor(len(update)/2.0)
        middle_page_sum += update[middle_index]
    return middle_page_sum

def fix_update(rules, update):
    while not validate_update(rules, update):
        index = 0
        for page in update:
            if page in rules:
                for i in range(0, index):
                    if update[i] in rules[page]:
                        # Move item one spot earlier in list
                        update.insert(index - 1, update.pop(index))
            index += 1
    return update


if __name__ == "__main__":
    rules = parse_rules()
    updates = parse_updates()
    valid_updates = []
    invalid_updates = []
    for update in updates:
        if validate_update(rules, update):
            valid_updates.append(update)
        else:
            invalid_updates.append(update)

    middle_page_sum = calculate_middle_page_sum(valid_updates)
    print(f"Middle sum of valid updates: {middle_page_sum}")

    fixed_updates = []
    for update in invalid_updates:
        fixed_updates.append(fix_update(rules, update))
    print(f"Middle sum of fixed invalid updates: {calculate_middle_page_sum(fixed_updates)}")
