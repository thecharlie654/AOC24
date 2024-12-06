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


for update in updates:
    for rule in rules:
        page_1 = rule[0]
        page_2 = rule[1]
        if not check_order(update, page_1, page_2):
            break
    else:
        print(f"{update} is ok")
