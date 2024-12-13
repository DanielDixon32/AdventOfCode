def step(rocks):
    new_rocks = []
    for curr in rocks:
        if curr == 0:
            new_rocks.append(1)
        else:
            digits = len(str(curr))
            if digits % 2 == 0:
                str_curr = str(curr)
                mid = digits // 2
                left = int(str_curr[:mid])
                right = int(str_curr[mid:])
                new_rocks.append(left)
                new_rocks.append(right)
            else:
                new_rocks.append(curr * 2024)
    return new_rocks

with open('input.txt') as file:
    content = file.read()

rocks = list(map(int, content.split()))

for _ in range(25):
    rocks = step(rocks)

print(len(rocks))
