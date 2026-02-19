# *args example
def sum_all(*nums):
    print(sum(nums))

sum_all(1,2,3,4)


# **kwargs example
def show_info(**data):
    print(data)

show_info(name="Ali", age=18)


# args + kwargs
def mix(a, *args, **kwargs):
    print(a, args, kwargs)

mix(1,2,3,x=5,y=6)


# unpack list
def add(a,b,c):
    print(a+b+c)

nums=[1,2,3]
add(*nums)