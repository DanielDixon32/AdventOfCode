l1 = []
l2 = []
with open('dec1/input.txt') as file:
    for line in file:
        text = line.split("   ")
        l1.append(int(text[0]))
        l2.append(int(text[1]))


counts = {}
for val in l2:
    if val in counts:
        counts[val] += 1 
    else:
        counts[val] = 1 
        
similarity_score = 0
for val in l1:
    if val in counts:
        similarity_score += val * counts[val]

print(similarity_score)