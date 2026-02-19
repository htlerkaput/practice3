# sort by length
words=["apple","kiwi","banana"]
print(sorted(words, key=lambda x: len(x)))


# sort tuples by second value
pairs=[(1,3),(2,1),(4,2)]
print(sorted(pairs, key=lambda x: x[1]))


# reverse sort numbers
nums=[5,2,9,1]
print(sorted(nums, key=lambda x: x, reverse=True))


# sort dict list by age
people=[{"name":"A","age":25},{"name":"B","age":20}]
print(sorted(people, key=lambda x: x["age"]))