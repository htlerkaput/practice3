# Positional argument
def power(base, exp):
    print(base ** exp)

power(2, 3)


# Default argument
def greet(name="Guest"):
    print("Hi", name)

greet()
greet("Sam")


# Keyword arguments
def info(name, age):
    print(name, age)

info(age=20, name="John")


# Mixed
def order(item, qty=1):
    print(item, qty)

order("apple")
order("banana", 5)