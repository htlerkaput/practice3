class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    pass

d=Dog()
d.speak()


class Parent:
    def show(self):
        print("Parent")

class Child(Parent):
    pass

Child().show()


class Vehicle:
    def move(self):
        print("Moving")

class Car(Vehicle):
    pass

Car().move()


class A:
    x=5

class B(A):
    pass

print(B().x)