"""
二分木の隣接リストの作成

　ｎ段目　開始数　[int((n+1)*(n+2)/2)+(m-1), int((n+1)*(n+2)/2+m)]
　　　　　ｍは、1から段数+2　までの個数
　最終行は、すべて　[] となる。

"""

a_list = []
for n in range(15):
    for m in range(1, n + 2):
        if n == 14:
            a_list.append([])
        else:
            a_list.append([int((n + 1) * (n + 2) / 2) + (m - 1), int((n + 1) * (n + 2) / 2 + m)])

# print(a_list)

"""
二分木の隣接リストの全ルートの検索　

search(goal, path)　---->  search(119, [0])

最初から、119の番号のノードまでの経路を出力

この部分をプログラム内部でため込んで次に使いたい。その方法は？？？

"""


def search(goal, path):
    n = path[-1]
    if n == goal:
        print(path)      # この部分をプログラム内部でため込んで次に使いたい。その方法は？？？
    else:
        for x in a_list[n]:
            if x not in path:
                path.append(x)
                search(goal, path)
                path.pop()


for n in range(105, 120):
    search(n, [0])
