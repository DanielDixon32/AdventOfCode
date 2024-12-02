def is_safe(row):
    inc = [row[i + 1] - row[i] for i in range(len(row) - 1)]
    return set(inc) <= {1, 2, 3} or set(inc) <= {-1, -2, -3}

reports = []
with open('dec2/input.txt') as file:
    for line in file:
        reports.append([int(x) for x in line.split()])
        
good_reports = 0
for report in reports:
    if is_safe(report):
        good_reports += 1

print(good_reports)