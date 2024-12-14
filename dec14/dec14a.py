import re

positions = []
velocities = [] 

WIDTH = 101
HEIGHT = 103

with open('input.txt') as file:
    for line in file:
        match = list(map(int, re.findall(r"-?\d+", line)))
        positions.append([match[0], match[1]])
        velocities.append([match[2], match[3]])

def step(seconds = 1): 
    for pos, vel in zip(positions, velocities):
        pos[0] = (pos[0] + seconds * vel[0]) % WIDTH
        pos[1] = (pos[1] + seconds * vel[1]) % HEIGHT

step(100)

# Quadrants:
# 1 2 
# 3 4
q1 = []
q2 = []
q3 = []
q4 = []
for pos in positions:
    if pos[0] < WIDTH // 2 and pos[1] < HEIGHT // 2:
        q1.append(pos)
    elif pos[0] > WIDTH // 2 and pos[1] < HEIGHT // 2:
        q2.append(pos)
    elif pos[0] < WIDTH // 2 and pos[1] > HEIGHT // 2:
        q3.append(pos)
    elif pos[0] > WIDTH // 2 and pos[1] > HEIGHT // 2:
        q4.append(pos)
print(f'Safety factor: {len(q1) * len(q2) * len(q3) * (len(q4))}')