# Constructor
class Person:
    def __init__(self,name):
        self.name=name

p=Person("Ali")
print(p.name)


# Two attributes
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

pt=Point(2,3)
print(pt.x,pt.y)


# Default value
class User:
    def __init__(self,name="Guest"):
        self.name=name

print(User().name)


# Computed attribute
class Circle:
    def __init__(self,r):
        self.area=3.14*r*r

print(Circle(2).area)