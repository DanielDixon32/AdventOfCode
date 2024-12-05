content = []
with open('input.txt') as file:
    for line in file:
        content.append(line.strip())

def checkValidPos(i, j):
    occurrences = 0
    directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1),
    ]
    
    for di, dj in directions:
        adjacent_str = ""
        for step in range(len('MXAS')):
            ni, nj = i + di * step, j + dj * step
            if 0 <= ni < len(content) and 0 <= nj < len(content[ni]):
                adjacent_str += content[ni][nj]
            else:
                break
        if adjacent_str == "XMAS" or adjacent_str == "SAMX":
            occurrences += 1

    return occurrences

occurrences = 0
for i in range(len(content)):
    for j in range(len(content[i])):
        if content[i][j] == 'X':
            occurrences += checkValidPos(i, j)

print(occurrences)
