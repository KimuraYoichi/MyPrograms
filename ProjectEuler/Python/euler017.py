"""
順列による解き方
http://kashiyuki.hatenablog.com/entry/2017/03/05/230423


import math

m = 20

n = math.factorial(m*2)//(math.factorial(m) * math.factorial(m))

print(n)
"""



"""
すべての経路を探索する。

マス目　　頂点の数
2*2       9
3*3      16
4*4      25

20*20    441

20*20のマス目は421個のノードを持つ。421個のノードの隣接リスト（有向）を作成して、そのルートを検索する。

nが21の倍数の場合は、[n+1,m]

nが最終行（n=20)の場合は、[n,m+1}

n,m  == 21 の場合は　[]

それ以外は、

(n,m)番目の頂点は、[n,m＋1] [n+1,m]の2つの隣接ノードを持つ。0 ≦ n,m ≦　20

(n,m)番目の頂点の番号は　21n+m+1  start (0,0) とする。

"""
masu = 3 # マス目の数

# a_list=[[1,3], [4,2], [5], [4,6], [5,7], [8], [7], [8], [],]
a_list = []
for n in range((masu + 1) ** 2 + 1):
    if n == (masu + 1) ** 2:            # 終端は[]
        a_list.append([])
    elif n > (masu + 1) * masu:         # 最終行は下に行けない。
        a_list.append([n + 1])
    elif n > 0 and n % (masu + 1) == masu:        # エッジは下にしか行けない
        a_list.append([n + masu + 1])
    else:                               # 右と下に行ける。
        a_list.append([n + 1, n + masu + 1])

# print(len(a_list))
# print(a_list)


def search(goal, path):
    n = path[-1]
    if n == goal:
        print(path)
    else:
        for x in a_list[n]:
            if x not in path:
                path.append(x)
                search(goal, path)
                path.pop()


search((masu+1)*(masu+1)-1, [0])




