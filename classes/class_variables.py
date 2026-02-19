class Dog:
    species="Canine"   # class variable

    def __init__(self,name):
        self.name=name   # instance variable

d1=Dog("Bob")
d2=Dog("Max")

print(d1.species, d2.species)
print(d1.name, d2.name)


# change class variable
Dog.species="Animal"
print(d1.species)


# change instance variable
d1.name="Rocky"
print(d1.name)


# show difference
print(Dog.species)