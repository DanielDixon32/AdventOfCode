from collections import defaultdict

def step_with_hashmap(rocks_map, cache):
    new_rocks_map = defaultdict(int)
    for stone, count in rocks_map.items():
        if stone in cache:
            results = cache[stone]
        else:
            if stone == 0:
                results = [1]
            else:
                digits = len(str(stone))
                if digits % 2 == 0:
                    str_stone = str(stone)
                    mid = digits // 2
                    left = int(str_stone[:mid])
                    right = int(str_stone[mid:])
                    results = [left, right]
                else:
                    results = [stone * 2024]
            cache[stone] = results

        for result in results:
            new_rocks_map[result] += count
    return new_rocks_map


with open('input.txt') as file:
    content = file.read()

rocks_map = defaultdict(int)
for rock in map(int, content.split()):
    rocks_map[rock] += 1

cache = {}
for step in range(75):
    rocks_map = step_with_hashmap(rocks_map, cache)
total_stones = sum(rocks_map.values())
print(total_stones)
