"""
Problem 67 「最大経路の和 その2」 †

以下の三角形の頂点から下まで移動するとき, その数値の合計の最大値は23になる.
3
7 4
2 4 6
8 5 9 3

この例では 3 + 7 + 4 + 9 = 23

100列の三角形を含んでいる15Kのテキストファイル triangle.txt (右クリックして, 『名前をつけてリンク先を保存』)の上から下まで最大合計を見つけよ.

注：これは, Problem 18のずっと難しいバージョンです.
全部で299 通りの組み合わせがあるので, この問題を解決するためにすべてのルートをためすことは可能でありません！
あなたが毎秒1兆本の(1012)ルートをチェックすることができたとしても, 全てをチェックするために200億年以上かかるでしょう.
解決するための効率的なアルゴリズムがあります. ;o)
"""


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
