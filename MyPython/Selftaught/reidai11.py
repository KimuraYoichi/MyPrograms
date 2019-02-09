class Dog:
    def __init__(self,name,breed,owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Person:
    def __init__(self,name):
        self.name = name


yoichi = Person("Kimira Yoichi")
roku = Dog("roku","siba",yoichi)

print(roku.owner.name)
