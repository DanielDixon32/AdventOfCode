import re

positions = []
velocities = []
writes = 0

'''
Robots cycle in the x-direction every 101 steps since WIDTH is prime.
Robots cycle in the y-direction every 103 steps since HEIGHT is prime.

LCM(WIDTH, HEIGHT) = WIDTH * HEIGHT since both are prime.

Upper bound on iterations: WIDTH * HEIGHT iterations before we start to examine redundant arrangements.
'''
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

def compute_safety_factor():
    # Quadrants:
    # 1 2 
    # 3 4
    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0
    
    for pos in positions:
        if pos[0] < WIDTH // 2 and pos[1] < HEIGHT // 2:
            q1 += 1
        elif pos[0] > WIDTH // 2 and pos[1] < HEIGHT // 2:
            q2 += 1
        elif pos[0] < WIDTH // 2 and pos[1] > HEIGHT // 2:
            q3 += 1
        elif pos[0] > WIDTH // 2 and pos[1] > HEIGHT // 2:
            q4 += 1
    
    return q1 * q2 * q3 * q4

def print_image(writes):
    image = ''
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if [x, y] in positions:
                image += '#'
            else:
                image += ' '
        image += '\n'
    with open(f'out{writes}.txt', 'w') as output:
        output.write(image)
        print(f'Writes: {writes}\n')

for i in range(WIDTH * HEIGHT):
    min = 10**10
    step()
    safety_factor = compute_safety_factor()
    
    if safety_factor < 1.2*10**8:
        print(f'Iteration: {i + 1}')
        print(f'Safety Factor: {safety_factor}')
        writes += 1
        print_image(writes)
        