class A:
    def methodA(self):
        print("A")

class B:
    def methodB(self):
        print("B")

class C(A,B):
    pass

c=C()
c.methodA()
c.methodB()


class Fly:
    def fly(self):
        print("Flying")

class Swim:
    def swim(self):
        print("Swimming")

class Duck(Fly,Swim):
    pass

d=Duck()
d.fly()
d.swim()


class X:
    x=5
class Y:
    y=10

class Z(X,Y):
    pass

z=Z()
print(z.x,z.y)


class Parent1:
    def greet(self):
        print("Hello")

class Parent2:
    def bye(self):
        print("Bye")

class Child(Parent1,Parent2):
    pass

Child().greet()
Child().bye()
