l1 = []
l2 = []
with open('dec1/input.txt') as file:
    for line in file:
        text = line.split("   ")
        l1.append(int(text[0]))
        l2.append(int(text[1]))

l1.sort()
l2.sort()

diff = 0
for i in range(len(l1)):
    diff += abs(l1[i] - l2[i])
    
print(diff)