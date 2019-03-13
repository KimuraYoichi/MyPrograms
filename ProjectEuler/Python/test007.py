import itertools
n = 1234567890

l = [int(x) for x in list(str(n))]

c_list = itertools.combinations(l, 2)

for c in c_list:
    # print(c)
    sub1 = str(n)[0:c[0]]
    sub2 = str(n)[c[0]:c[1]]
    print(sub1)
    print(sub2)



# for candiate in result:
#     c_list = list(itertools.combinations(candiate[2], 3))  # 入れ替える位置を組み合わせで決定する。
#     for cl in c_list:
#         # print(cl)
#         # print(candiate)
#         if judge8(changedigt(candiate[0], cl)):
#             result1.append(candiate[0])