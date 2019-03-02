"""フィボナッチ数列は以下の漸化式で定義される:
Fn = Fn-1 + Fn-2, ただし F1 = 1, F2 = 1.

最初の12項は以下である.

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

12番目の項, F12が3桁になる最初の項である.

1000桁になる最初の項の番号を答えよ.

"""

# def fibonacci(n):
#     fibo = fibonacci(n-1)
#     for i in range(n):
#         if i <= 1:
#             result = i
#             yield result
#         else:
#             previous = next(fibo)
#             result = result + previous
#             yield result
#
# for i in fibonacci(10):
#     print(i, end=' ')


def fibonacci1(n):
    a, b = 1, 1
    for i in range(n):
        yield [i, a]
        a, b = b, b+a

for n in fibonacci1(1000000000000):
    if len(str(n[1])) == 1000:
        print(n, end = ' ')
        break
