class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Woof")

Dog().speak()


class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self,s):
        self.s=s
    def area(self):
        return self.s*self.s

print(Square(4).area())


class Employee:
    def salary(self):
        return 1000

class Manager(Employee):
    def salary(self):
        return 2000

print(Manager().salary())


class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B overrides A")

B().show()
