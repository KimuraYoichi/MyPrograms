"""
5000個以上の名前が書かれている46Kのテキストファイル filenames.txt を用いる. まずアルファベット順にソートせよ.

のち, 各名前についてアルファベットに値を割り振り, リスト中の出現順の数と掛け合わせることで, 名前のスコアを計算する.

たとえば, リストがアルファベット順にソートされているとすると, COLINはリストの938番目にある. またCOLINは 3 + 15 + 12 + 9 + 14 = 53 という値を持つ. よってCOLINは 938 × 53 = 49714 というスコアを持つ.

ファイル中の全名前のスコアの合計を求めよ.
"""

import csv

csv_file = open("euler022.txt", "r")
f = csv.reader(csv_file, delimiter=",")


for row in f:
    print(sorted(row))
    sortedrow = sorted(row)

# print(sortedrow)
# print(sortedrow[937])



def alph2num(alph):
    numalph = []
    for ss in alph:
        numalph.append(ord(ss) - ord('A') + 1)
    return numalph

# print(alph2num('COLIN'))
# print(sum(alph2num('COLIN')))

namenum = []

for name in sortedrow:
    namenum.append(alph2num(name))

# print(namenum)
# print(sum(namenum[1]))

ans = 0

for i in range(len(namenum)):
    ans += (sum(namenum[i]) * (i+1))

print(ans)

