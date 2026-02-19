nums = [1,2,3,4]

# multiply each by 2
result = list(map(lambda x: x*2, nums))
print(result)


# square numbers
print(list(map(lambda x: x*x, nums)))


# string lengths
words=["hi","hello","python"]
print(list(map(lambda w: len(w), words)))


# convert to float
nums=["1","2","3"]
print(list(map(lambda x: float(x), nums)))