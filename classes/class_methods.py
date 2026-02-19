class Math:
    def add(self,a,b):
        return a+b

m=Math()
print(m.add(2,3))


class Counter:
    def __init__(self):
        self.count=0
    def inc(self):
        self.count+=1

c=Counter()
c.inc()
print(c.count)


class Printer:
    def show(self,text):
        print(text)

Printer().show("Hello")


class Check:
    def even(self,n):
        return n%2==0

print(Check().even(4))