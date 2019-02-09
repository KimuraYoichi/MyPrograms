class Person:
    def __init__(self):
        self.name = 'Kimura'

kimura = Person()
same_kimura = kimura
print(kimura is same_kimura)

another_kimura = Person()
print(kimura is another_kimura)




