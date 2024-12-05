content = []
with open('input.txt') as file:
    for line in file:
        content.append(line)

def checkXMAS(i, j):
    d1_m = (i - 1, j - 1)
    d1_s = (i + 1, j + 1)
    
    d2_m = (i - 1, j + 1)
    d2_s = (i + 1, j - 1)

    if (
        0 <= d1_m[0] < len(content) and 0 <= d1_m[1] < len(content[d1_m[0]]) and
        0 <= d1_s[0] < len(content) and 0 <= d1_s[1] < len(content[d1_s[0]]) and
        0 <= d2_m[0] < len(content) and 0 <= d2_m[1] < len(content[d2_m[0]]) and
        0 <= d2_s[0] < len(content) and 0 <= d2_s[1] < len(content[d2_s[0]])
    ):
        diagonal1 = content[d1_m[0]][d1_m[1]] + content[i][j] + content[d1_s[0]][d1_s[1]]
        diagonal2 = content[d2_m[0]][d2_m[1]] + content[i][j] + content[d2_s[0]][d2_s[1]]
        
        if (
            (diagonal1 == "MAS" or diagonal1 == "SAM") and
            (diagonal2 == "MAS" or diagonal2 == "SAM")
        ):
            return 1

    return 0


occurrences = 0
for i in range(len(content)):
    for j in range(len(content[i])):
        if content[i][j] == 'A':
            occurrences += checkXMAS(i, j)

print(occurrences)
