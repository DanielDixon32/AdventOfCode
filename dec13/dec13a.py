import numpy as np
import re

machines = []
with open("input.txt") as file:
    lines = file.read().strip().split("\n\n")
    for block in lines:
        match = list(map(int, re.findall(r"-?\d+", block)))
        machines.append({
            "a_x": match[0],
            "a_y": match[1],
            "b_x": match[2],
            "b_y": match[3],
            "p_x": match[4],
            "p_y": match[5]
        })
        
total_cost = 0
total_prizes = 0

for machine in machines:
    # Solve as a L.C. of button1 and button2:
    A = np.array([
        [machine["a_x"], machine["b_x"]],
        [machine["a_y"], machine["b_y"]]
    ])
    B = np.array([machine["p_x"], machine["p_y"]])
    
    try:
        solution = np.linalg.solve(A, B)
        x, y = solution
        
        # round to get rid of floating point errors
        x = round(x)
        y = round(y)
        if (
            0 <= x <= 100 and 0 <= y <= 100 and
            np.allclose(np.dot(A, [x, y]), B)
        ):
            total_cost += 3 * x + y
            total_prizes += 1

    except np.linalg.LinAlgError:
        # Skip unsolveable systems
        continue

print("Total prizes:", total_prizes)
print("Total cost:", total_cost)