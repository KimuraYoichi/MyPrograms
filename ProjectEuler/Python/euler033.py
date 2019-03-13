"""
Problem 33 「桁消去分数」

49/98は面白い分数である.「分子と分母からそれぞれ9を取り除くと, 49/98 = 4/8 となり, 簡単な形にすることができる」
と経験の浅い数学者が誤って思い込んでしまうかもしれないからである.
(方法は正しくないが，49/98の場合にはたまたま正しい約分になってしまう．)

我々は 30/50 = 3/5 のようなタイプは自明な例だとする.

このような分数のうち, 1より小さく分子・分母がともに2桁の数になるような自明でないものは, 4個ある.

その4個の分数の積が約分された形で与えられたとき, 分母の値を答えよ.

"""

from fractions import Fraction

ans = []
ans1 = []

for n in range(10, 100):
    if n % 10 != 0:
        for m in range(1, 100):
            if n // 10 == m // 10 and m % 10 != 0 and Fraction(n, m) == Fraction(n % 10, m % 10):
                ans.append([n, m])
            elif n // 10 == m % 10 and m // 10 != 0 and Fraction(n, m) == Fraction(n % 10, m // 10):
                ans.append([n, m])
            elif n % 10 == m // 10 and m % 10 != 0 and Fraction(n, m) == Fraction(n // 10, m % 10):
                ans.append([n, m])
            elif n % 10 == m % 10 and m // 10 != 0 and Fraction(n, m) == Fraction(n // 10, m // 10):
                ans.append([n, m])

for l in ans:
    if l[0] != l[1] and l[0] < l[1]:
        ans1.append(l)

print(ans1)
product = 1

for l1 in ans1:
    product *= Fraction(l1[0], l1[1])

print(product)

# [[16, 64], [19, 95], [26, 65], [49, 98]]
# 1/100

