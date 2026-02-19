# Simple lambda
square = lambda x: x*x
print(square(5))


# Two arguments
add = lambda a,b: a+b
print(add(2,3))


# Conditional lambda
check = lambda x: "even" if x%2==0 else "odd"
print(check(7))


# Lambda inside print
print((lambda x: x+10)(5))