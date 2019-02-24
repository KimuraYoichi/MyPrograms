# import numpy as np
#
# filename = 'euler013.csv'
# raw_data = open( filename, 'r' )
# data = np.loadtxt( raw_data, delimiter=" " )
#
# print(type(data))
# print(data)


import csv

int1 = []
int2 = []
int3 = []
int4 = []
int4 = []
int5 = []

with open('euler013.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        rowstr1 = row[0]
        int1.append(int(rowstr1[0:10]))
        int2.append(int(rowstr1[10:20]))
        int3.append(int(rowstr1[20:30]))
        int4.append(int(rowstr1[30:40]))
        int5.append(int(rowstr1[40:50]))

kur1 = (sum(int5) // 10 ** 10)
kur2 = ((sum(int4)) + kur1) // 10 ** 10
kur3 = ((sum(int3)) + kur2) // 10 ** 10
kur4 = ((sum(int2)) + kur3) // 10 ** 10
ans = sum(int1) + kur4

print(ans)
print(str(ans)[0:10])