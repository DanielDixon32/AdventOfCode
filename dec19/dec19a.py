with open('input.txt') as file:
    content = file.read()

content = content.split('\n\n')
blocks = set(content[0].split(', '))
patterns = content[1].splitlines()

def can_form_pattern(pattern, blocks):
    # empty string always valid
    if not pattern:
        return True
    
    for j in range(1, len(pattern) + 1):
        # take the fist j characters as a prefix
        substr = pattern[:j]
        if substr in blocks:
            # check suffix (valid prefix + valid suffix => valid string)
            if can_form_pattern(pattern[j:], blocks):
                return True
    
    return False

count = 0
for pattern in patterns:
    if can_form_pattern(pattern, blocks):
        count += 1
print(count)