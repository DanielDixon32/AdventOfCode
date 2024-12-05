def is_update_valid(update, rules):
    update_set = set(update)
    for x, y in rules:
        if x in update_set and y in update_set:
            if update.index(x) > update.index(y):
                return False
    return True

def calculate_sum(input_data):
    rules_section, updates_section = input_data.split("\n\n")
    rules = [tuple(map(int, rule.split("|"))) for rule in rules_section.splitlines()]
    updates = [list(map(int, update.split(","))) for update in updates_section.splitlines()]
    
    
    valid_updates = [update for update in updates if is_update_valid(update, rules)]
    middle_pages = [update[len(update) // 2] for update in valid_updates]
    return sum(middle_pages)


with open('input.txt') as file:
    input_data = file.read()

result = calculate_sum(input_data)
print(result)
