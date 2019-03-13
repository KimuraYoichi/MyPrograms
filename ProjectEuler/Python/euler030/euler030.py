"""
驚くべきことに, 各桁を4乗した数の和が元の数と一致する数は3つしかない.

    1634 = 1**4 + 6**4 + 3**4 + 4**4
    8208 = 8**4 + 2**4 + 0**4 + 8**4
    9474 = 9**4 + 4**4 + 7**4 + 4**4

ただし, 1=1**4は含まないものとする. この数たちの和は 1634 + 8208 + 9474 = 19316 である.

各桁を5乗した数の和が元の数と一致するような数の総和を求めよ.
"""
ans = []
p = 5
upper = 9 ** p

for n in range(2, 100000000):
    if upper * len(str(n)) < n:
        continue
    else:
        s = str(n)
        digitpowerp = 0
        for i in range(len(s)):
            digitpowerp += int(s[i]) ** p
        if n == digitpowerp:
            ans.append(n)

print(ans)
print(sum(ans))

# [4150, 4151, 54748, 92727, 93084, 194979]
# sum 443839
