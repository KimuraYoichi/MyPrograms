"""
2**15 = 32768 であり, 各位の数字の和は 3 + 2 + 7 + 6 + 8 = 26 となる.

同様にして, 2**1000 の各位の数字の和を求めよ.

注: Problem 20 も各位の数字の和に関する問題です。解いていない方は解いてみてください。

"""

i = 2 ** 1000

i_str = str(i)

digitList = []

for s in range(len(i_str)):
    digitList.append(int(i_str[s:s + 1]))

print(digitList)
print(sum(digitList))
