"""
単位分数とは分子が1の分数である. 分母が2から10の単位分数を10進数で表記すると次のようになる.

    1/2 = 0.5
    1/3 = 0.(3)
    1/4 = 0.25
    1/5 = 0.2
    1/6 = 0.1(6)
    1/7 = 0.(142857)
    1/8 = 0.125
    1/9 = 0.(1)
    1/10 = 0.1

0.1(6)は 0.166666... という数字であり, 1桁の循環節を持つ. 1/7 の循環節は6桁ある.

d < 1000 なる 1/d の中で小数部の循環節が最も長くなるような d を求めよ.

A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10	= 	0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.


ある分数を、既約分数になるまで約分して、その分母を素因数分解し、
２と５だけから出来ていれば、有限小数になります。
"""

from fractions import Fraction


# 有限小数かどうか判定する関数
def isFinite(num, den):
    fra = Fraction(num, den)  # 既約分数にする
    den = fra.denominator  # 既約分数の分母を得る
    while den % 2 == 0:  # 2で割れるところまで割る
        den //= 2
    while den % 5 == 0:  # 5で割れるところまで割る
        den //= 5
    return den == 1


# 循環小数かどうか判定する関数
def isRecurring(num, den):
    return not isFinite(num, den)


# 同じあまりが出てくるまで割り算を実施しその商をリスト形式で渡す。
def calcrecurring(n):
    r = 1
    d = n
    qutient = []
    remainder = []
    while remainder.count(r) < 2:
        while 10 * r < n:
            qutient.append(0)
            r = r * 10
        q, r = divmod(10 * r, d)
        qutient.append(q)
        remainder.append(r)
    return qutient


anslist = []
maxdigit = 0
maxi = 0

for i in range(1, 1000):
    if isFinite(1, i):
        print("%d は有限小数" % i)  # 有限小数は計算しない
    else:
        # print(calcrecurring(i))
        if len(calcrecurring(i)) > maxdigit:
            anslist = calcrecurring(i)
            maxdigit = len(calcrecurring(i))
            maxi = i

print(anslist)
print(maxi)

print(len(calcrecurring(983)))
