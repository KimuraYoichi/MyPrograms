"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

"""

import math

i_str = str(math.factorial(100))

digitList = []

for s in range(len(i_str)):
    digitList.append(int(i_str[s:s + 1]))

print(digitList)
print(sum(digitList))
