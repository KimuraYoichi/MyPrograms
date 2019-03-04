# def alph2num(alph):
#     self.numalph = []
#     self.alff = alph
#     for ss in self.alph:
#         print(ss)
#         numalph.append(ord(ss) - ord('A') + 1)
#     return self.numalph

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


def calcrecurring(n):
    r = 1
    d =n
    qutient = []
    remainder = []
    while remainder.count(r) < 2:
        while 10*r < n:
            qutient.append(0)
            r = r * 10
        q, r = divmod(10*r, d)
        qutient.append(q)
        remainder.append(r)
    return qutient

anslist = []
maxdigit = 0
maxi = 0

for i in range(1,1000):
    if isFinite(1, i):
        print("%d は有限小数" %i)
    else:
        # print(calcrecurring(i))
        if len(calcrecurring(i)) > maxdigit:
            anslist = calcrecurring(i)
            maxdigit = len(calcrecurring(i))
            maxi = i

print(anslist)
print(maxi)













