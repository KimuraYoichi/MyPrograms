n = 1000000
furui = list(range(2, n + 1))
furui1 = list(furui)

for i in furui:
    if i == 2:
        continue
    else:
        for j in range(2, int(i ** 0.5) + 2):
            if i % j == 0:
                furui1.remove(i)
                break
print(furui1)
