class Person:
    def __init__(self,name):
        self.name=name

class Student(Person):
    def __init__(self,name,grade):
        super().__init__(name)
        self.grade=grade

s=Student("Ali",10)
print(s.name,s.grade)


class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        super().show()
        print("B")

B().show()


class Vehicle:
    def __init__(self,brand):
        self.brand=brand

class Car(Vehicle):
    def __init__(self,brand,model):
        super().__init__(brand)
        self.model=model

print(Car("Toyota","Camry").brand)