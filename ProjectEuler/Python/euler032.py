"""
すべての桁に 1 から n が一度だけ使われている数をn桁の数がパンデジタル (pandigital) であるということにしよう:
例えば5桁の数 15234 は1から5のパンデジタルである.
7254 は面白い性質を持っている. 39 × 186 = 7254 と書け, 掛けられる数, 掛ける数, 積が1から9のパンデジタルとなる.
掛けられる数/掛ける数/積が1から9のパンデジタルとなるような積の総和を求めよ.

HINT: いくつかの積は, 1通り以上の掛けられる数/掛ける数/積の組み合わせを持つが1回だけ数え上げよ.
"""
candiatelist = []
anslist = []
productlist = []
for n in range(1, 10000):
    for m in range(1, 10000):
        if len(str(n)) + len(str(m)) + len(str(n * m)) == 9:
            candiatelist.append([n, m, n * m])

for candiate in candiatelist:
    canstr = str(candiate[0]) + str(candiate[1]) + str(candiate[2])
    canlist = sorted([int(x) for x in list(canstr)])
    if canlist == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        anslist.append(candiate)

print(anslist)
for can in anslist:
    productlist.append(can[2])

print(list(set(productlist)))
print(sum(list(set(productlist))))

# [5346, 5796, 6952, 7852, 4396, 7632, 7254]
# 45228