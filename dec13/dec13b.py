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
            "p_x": match[4] + 10**13,
            "p_y": match[5] + 10**13
        })
        
total_cost = 0
total_prizes = 0
       
for machine in machines:
    x1 = machine["a_x"]
    x2 = machine["b_x"]
    y1 = machine["a_y"]
    y2 = machine["b_y"]
    b1 = machine["p_x"]
    b2 = machine["p_y"]
    
    c1 = (b2 * x2 - b1 * y2) // (y1 * x2 - y2 * x1)
    c2 = (b1 - c1 * x1) // x2
    
    if (c1 * x1 + c2 * x2 == b1) and (c1 * y1 + c2 * y2 == b2):
        total_cost += 3 * c1 + c2
        total_prizes += 1

print("Total prizes:", total_prizes)
print("Total cost:", total_cost)