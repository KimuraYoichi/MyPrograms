import numpy as np

inputList = []
inputRoute = []


def flatten(nested_list):
    """2重のリストをフラットにする関数  ついでに int 化"""
    return [int(e) for inner_list in nested_list for e in inner_list]


# 三角数の読み込み
with open('euler018.csv', 'r') as f:
    for row in f:
        inputList.append(row.split())

g = flatten(inputList)

# g = np.loadtxt('euler018.csv', delimiter=' ', dtype='int')
# print(g)

# 探索されてルートを読み込み

routes = np.loadtxt('euler018_1.log', delimiter=' ', dtype='int')

sum = 0
sumlist = []

for rt in routes:
    for i in range(len(rt)):
        sum += g[rt[i]]
    sumlist.append(sum)
    sum = 0

print(sumlist)
print(max(sumlist))
