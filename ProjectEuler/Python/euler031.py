"""
イギリスでは硬貨はポンド£とペンスpがあり，一般的に流通している硬貨は以下の8種類である.

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

以下の方法で£2を作ることが可能である．

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

これらの硬貨を使って£2を作る方法は何通りあるか?
"""
ans = 0

ans = 0
anslist = []
for n200 in range(2):
    if n200 * 200 == 200:
        ans += 1
        anslist.append([n200])
        break
    if n200 * 200 > 200:
        break
    for n100 in range(3):
        if n200 * 200 + n100 * 100 == 200:
            ans += 1
            anslist.append([n200, n100])
            break
        if n200 * 200 + n100 * 100 > 200:
            break
        for n50 in range(5):
            if n200 * 200 + n100 * 100 + n50 * 50 == 200:
                anslist.append([n200, n100, n50])
                ans += 1
                break
            if n200 * 200 + n100 * 100 + n50 * 50 > 200:
                break
            for n20 in range(11):
                if n200 * 200 + n100 * 100 + n50 * 50 + n20 * 20 == 200:
                    ans += 1
                    anslist.append([n200, n100, n50, n20])
                    break
                if n200 * 200 + n100 * 100 + n50 * 50 + n20 * 20 > 200:
                    break
                for n10 in range(21):
                    if n200 * 200 + n100 * 100 + n50 * 50 + n20 * 20 + n10 * 10 == 200:
                        ans += 1
                        anslist.append([n200, n100, n50, n20, n10])
                        break
                    if n200 * 200 + n100 * 100 + n50 * 50 + n20 * 20 + n10 * 10 > 200:
                        break
                    for n5 in range(41):
                        if n200 * 200 + n100 * 100 + n50 * 50 + n20 * 20 + n10 * 10 + n5 * 5 == 200:
                            ans += 1
                            anslist.append([n200, n100, n50, n20, n10, n5])
                            break
                        if n200 * 200 + n100 * 100 + n50 * 50 + n20 * 20 + n10 * 10 + n5 * 5 > 200:
                            break
                        for n2 in range(101):
                            if n200 * 200 + n100 * 100 + n50 * 50 + n20 * 20 + n10 * 10 + n5 * 5 + n2 * 2 == 200:
                                ans += 1
                                anslist.append([n200, n100, n50, n20, n10, n5, n2])
                                break
                            if n200 * 200 + n100 * 100 + n50 * 50 + n20 * 20 + n10 * 10 + n5 * 5 + n2 * 2 > 200:
                                break
                            ans += 1

print(ans)
print(anslist)

# 73682

