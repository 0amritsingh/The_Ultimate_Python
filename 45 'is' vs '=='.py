# 'is' vs '==' or COMPARISON OPERATORS in Python

# "is" exact location of a object in memory
# "==" as compared to the object 

# values which are immutable returns true in every case

a = 4 #int is immutable
b = 4

print('Integer (is):',a is b)
print('Integer (==):',a == b)

a = (1, 2, 5) #tuple is immutable
b = (1, 2, 5)

print('Tuple (is):',a is b)
print('Tuple (==):',a == b)

a = {1, 2, 5} #lists are un-immutable
b = {1, 2, 5}

print('List (is):',a is b)
print('List (==):',a == b)
