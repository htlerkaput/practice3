# Basic class
class Person:
    pass

p = Person()
print(p)


# Class with attribute
class Car:
    brand = "Toyota"

c = Car()
print(c.brand)


# Class with method
class Dog:
    def bark(self):
        print("Woof")

d=Dog()
d.bark()


# Multiple objects
class Student:
    def say(self):
        print("I am student")

s1=Student()
s2=Student()
s1.say()
s2.say()