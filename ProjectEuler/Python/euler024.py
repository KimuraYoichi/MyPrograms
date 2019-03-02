"""
順列とはモノの順番付きの並びのことである. たとえば, 3124は数 1, 2, 3, 4 の一つの順列である. すべての順列を数の大小でまたは辞書式に並べたものを辞書順と呼ぶ. 0と1と2の順列を辞書順に並べると
012 021 102 120 201 210

になる.

0,1,2,3,4,5,6,7,8,9からなる順列を辞書式に並べたときの100万番目はいくつか?

2783915460
"""

import itertools

l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
m = 1000000
i = 1

# p = itertools.permutations(l, 2)

# for v in itertools.permutations(l):
#     print(v)

for v in itertools.permutations(l):
    if i == m:
        print(v)
        break
    else:
        i += 1
