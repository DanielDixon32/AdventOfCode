def is_update_valid(update, rules):
    update_set = set(update)
    for x, y in rules:
        if x in update_set and y in update_set:
            if update.index(x) > update.index(y):
                return False
    return True

def is_valid_order(x, y, rules):
    return (x, y) not in rules

def insertion_sort_with_rules(update, rules):
    for i in range(1, len(update)):
        key = update[i]
        j = i - 1
        while j >= 0 and is_valid_order(key, update[j], rules):
            update[j + 1] = update[j]
            j -= 1
        update[j + 1] = key
    return update

def sum_fixed_updates(input_data):
    rules_section, updates_section = input_data.split("\n\n")
    rules = [tuple(map(int, rule.split("|"))) for rule in rules_section.splitlines()]
    updates = [list(map(int, update.split(","))) for update in updates_section.splitlines()]
    
    invalid_updates = [update for update in updates if not is_update_valid(update, rules)]
    
    fixed_updates = [insertion_sort_with_rules(update, set(rules)) for update in invalid_updates]
    
    middle_pages = [update[len(update) // 2] for update in fixed_updates]
    
    return sum(middle_pages)

with open('input.txt') as file:
    input_data = file.read()

result = sum_fixed_updates(input_data)
print(result)