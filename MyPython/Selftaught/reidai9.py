class Orange:
    def __init__(self,w,c):
        self.weight = w
        self.color = c
        print("Created")

or1 = Orange(10,"dark orange")
print(or1)
print(or1.weight)
print(or1.color)

or1.color ="light orange"
or1.weight = 20

print(or1)
print(or1.weight)
print(or1.color)


