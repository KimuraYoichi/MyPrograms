from fractions import Fraction

# Fractionインスタンスを生成します
a = Fraction(1,3)

# a の値を表示します
print(a)

# 0.125 を分数に変換します
a = Fraction(0.125)

print(a)

x = Fraction(19,33)

# 分子を取得します
a = x.numerator

# 分母を取得します
b = x.denominator

print(a, b)

# 1/2 + 1/3
a = Fraction(1,2) + Fraction(1,3)

# 1/2 - 1/3
b = Fraction(1,2)-Fraction(1,3)

# (1/2)×(1/3)
c = Fraction(1,2)*Fraction(1,3)

# (1/2)÷(1/3)
d = Fraction(1,2)/Fraction(1,3)

print(a, b, c, d)

# 円周率の値を呼びだします
from math import pi

# 円周率の値を分数に変換します
x = Fraction(pi)

# 円周率の近似分数を取得します
f_pi = x.limit_denominator(1000)

print(f_pi)

# 円周率の値を呼びだします
from math import pi
from fractions import Fraction

# 円周率の値を分数に変換します
x = Fraction(pi)

# 円周率の近似分数を取得します
f_pi = x.limit_denominator(10)

print(f_pi)


x = 0
m = 0

for ct in range(20):
    m += 1
    x += Fraction(1, m)

# print(x)

print(float(x))

print(Fraction(1, 3) == Fraction(6, 18))

