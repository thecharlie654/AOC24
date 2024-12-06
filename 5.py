# Part 1

def check_order(update, page_1, page_2):
    page_1_index = get_index(update, page_1)
    page_2_index = get_index(update, page_2)
    if page_1_index is not False and page_2_index is not False:
        if page_1_index < page_2_index:
            return True
        else:
            return False
    else:
        return True

def get_index(list, target):
    if target not in list:
        return False
    return list.index(target)

with open("input.txt") as f:
    lines = str(f.read()).strip().split("\n\n")
    rules = [list(map(int, rule.strip().split("|"))) for rule in lines[0].split("\n")]
    updates = [list(map(int, pages.strip().split(","))) for pages in lines[1].split("\n")]


part_1 = 0
for update in updates:
    for rule in rules:
        page_1 = rule[0]
        page_2 = rule[1]
        if not check_order(update, page_1, page_2):
            break
    else:
        part_1 += update[len(update) // 2]

print(f"{part_1=}")

# Part 2

def check_order(update, page_1, page_2):
    page_1_index = get_index(update, page_1)
    page_2_index = get_index(update, page_2)
    if page_1_index is not False and page_2_index is not False:
        if page_1_index < page_2_index:
            return True
        else:
            return False
    else:
        return True

def get_index(list, target):
    if target not in list:
        return False
    return list.index(target)

def correct_order(update, rules):
    for rule in rules:
        page_1 = rule[0]
        page_2 = rule[1]
        if not check_order(update, page_1, page_2):
            index_1 = get_index(update, page_1)
            index_2 = get_index(update, page_2)
            temp = update[index_1]
            update[index_1] = update[index_2]
            update[index_2] = temp
    for rule in rules:
        page_1 = rule[0]
        page_2 = rule[1]
        if not check_order(update, page_1, page_2):
            update = correct_order(update, rules)
    else:
        return update


with open("input.txt") as f:
    lines = str(f.read()).strip().split("\n\n")
    rules = [list(map(int, rule.strip().split("|"))) for rule in lines[0].split("\n")]
    updates = [list(map(int, pages.strip().split(","))) for pages in lines[1].split("\n")]


part_2 = 0
for update in updates:
    for rule in rules:
        page_1 = rule[0]
        page_2 = rule[1]
        if not check_order(update, page_1, page_2):
            update = correct_order(update, rules)
            part_2 += update[len(update) // 2]

print(f"{part_2=}")