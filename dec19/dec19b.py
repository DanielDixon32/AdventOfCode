with open('input.txt') as file:
    content = file.read()

content = content.split('\n\n')
blocks = set(content[0].split(', '))
patterns = content[1].splitlines()

count = 0
def ways_to_form_pattern(pattern, blocks, memory):
    # return memorized results
    if pattern in memory:
        return memory[pattern]
    
    # empty string always valid
    if not pattern:
        memory[pattern] = 1
        return memory[pattern]
    
    result = 0
    for j in range(1, len(pattern) + 1):
        # take the fist j characters as a prefix
        substr = pattern[:j]
        if substr in blocks:
            # check suffix (valid prefix + valid suffix => valid string)
            result += ways_to_form_pattern(pattern[j:], blocks, memory)
            
    # store result
    memory[pattern] = result
    return result

memory = {}
for pattern in patterns:
    count += ways_to_form_pattern(pattern, blocks, memory)

print(count)