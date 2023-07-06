# List in Python

l = [3, 4, 5, 6.1, 7.2, "sring", True, False]

print(l) # prints whole l
print(len(l)) # lenth of l
print(type(l)) # type of l

# indexing list
print(l[0])
print(l[3])
print(l[5])
print(l[7])

# slicing list like string
print(l[3:6]) # prints from 3 to 6-1=5
print(l[:6]) # python take 0 as default
print(l[3:]) # python take 8(last) as default
print(l[:]) # prints whole l

# checking elements of list
if 7.2 in l:
    print("Yes")
else:
    print("No")

# same with the sting
# checking character in the string
if "am" in "amrit":
    print("Yes")
else:
    print("No")
    
# List Comprehention

lst = [i for i in range(10)] # supose we need to make a list of 1000 ints so we'll not just set to typw all 1000 int we use loops in the very list.
print(lst)

lst = [i+2 for i in range(10)] # we can change i with our convience
print(lst)

lst = [i for i in range(10) if i == 2] # we can give condition also
print(lst)
