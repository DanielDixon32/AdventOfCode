import re

input_str = ''
with open('input.txt') as file:
    input_str = file.read()

instructions = re.findall(r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)', input_str)

total = 0
count = True
for instruction in instructions:
    if instruction == "do()":
        enabled = True
    elif instruction == "don't()":
        enabled = False
    else:
        if enabled:
            val1, val2 = map(int, re.findall(r'\d+', instruction))
            total += val1 * val2

print(total)