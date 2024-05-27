# Enumerate function in python

# The enumerate function is a built-in function in Python that allows you to loop over a sequence (such as a list, tuple, or string) and get the index and value of each element in the sequence at the same time. It always returns a tuple.

# simple example:
string = 'PYTHON'
for i in enumerate(string):
    print(i)

# Start indexing from 1:
tuple = ('One', 'Two', 'Three', 'Four')
for i in enumerate(tuple, start=1):
    print(i)

# Seperating tuple elements:
basket = ['apple', 'mango', 'banana', 'grapes']
for s_no, fruit in enumerate(basket, start=1):
    print(f'{s_no}. {fruit.capitalize()}')

# As you can see, the enumerate function returns a tuple containing the index and value of each element in the sequence. You can use the for loop to unpack these tuples and assign them to variables, as shown in the example above.
