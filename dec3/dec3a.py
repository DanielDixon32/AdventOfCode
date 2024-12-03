import re

input_str = ''
with open('input.txt') as file:
    input_str = file.read()

pattern = re.compile(r"mul\([0-9]+,[0-9]+\)")
operations = pattern.findall(input_str)

l1, l2 = [], []
for operation in operations:
    str1 = ''
    str2 = ''
    append1 = True
    for char in operation:
        if char == ',':
            append1 = False
        if str(char).isnumeric():
            if append1:
                str1 += char
            else:
                str2 += char
    l1.append(int(str1))
    l2.append(int(str2))

total = 0
for i in range(len(l1)):
    total += l1[i] * l2[i]
print(total)