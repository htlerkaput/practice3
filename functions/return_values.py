# Return single value
def add(a, b):
    return a + b

print(add(3, 4))


# Return multiple values
def calc(a, b):
    return a+b, a*b

s, m = calc(2,3)
print(s, m)


# Return boolean
def is_even(n):
    return n % 2 == 0

print(is_even(10))


# Return list
def squares(n):
    return [i*i for i in range(n)]

print(squares(5))