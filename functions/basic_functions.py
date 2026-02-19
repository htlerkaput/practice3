# Example 1 — simple function
def greet():
    print("Hello!")

greet()


# Example 2 — function with parameter
def greet_name(name):
    print("Hello,", name)

greet_name("Alex")


# Example 3 — function returning value
def square(x):
    return x * x

print(square(5))


# Example 4 — function calling another function
def double(x):
    return x * 2

def process(n):
    return double(n) + 1

print(process(4))