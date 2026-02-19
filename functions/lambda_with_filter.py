nums=[1,2,3,4,5,6]

# even numbers
print(list(filter(lambda x: x%2==0, nums)))


# >3
print(list(filter(lambda x: x>3, nums)))


# strings longer than 3
words=["cat","elephant","dog"]
print(list(filter(lambda w: len(w)>3, words)))


# remove empty strings
lst=["hi","","hello",""]
print(list(filter(lambda x: x!="", lst)))