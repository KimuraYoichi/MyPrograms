import csv

with open('euler067.csv') as f:
    reader = csv.reader(f, delimiter=" ")
    il = [row for row in reader]

l = []
l = [[int(v) for v in row] for row in il]
# print(l)

for k in range(1, 100):
    i = 100 - k
    wl = []
    for j in range(len(l[i - 1])):
        l[i - 1][j] += max(l[i][j], l[i][j + 1])
        # print(l[i-1][j])
        wl.append(l[i - 1][j])
    # print(wl)
    l[i - 1] = wl

print(l[0])
