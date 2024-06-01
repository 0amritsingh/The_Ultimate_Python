# Map, Filter and Reduce in Pyhton:

# In Python, the map, filter, and reduce functions are built-in functions that allow you to apply a function to a sequence of elements and return a new sequence. These functions are known as higher-order functions, as they take other functions as arguments.

# ---------------------------------------------MAP---------------------------------------------
# The map function applies a function to each element in a sequence and returns a new sequence containing the transformed elements. The map function has the following syntax:

# map(function, iterable)

# The function argument is a function that is applied to each element in the iterable argument. The iterable argument can be a list, tuple, or any other iterable object.

# Here is an example of how to use the map function:
func = lambda x: x * x
lst = [i for i in range(1, 6)]

# With Map (1 line):
var = map(func, lst)
print('Map:', list(var))

# Instead of Map (4 lines):
newlst = []
for number in lst:
    newlst.append(func(number))
print('Loop:', newlst)

# ---------------------------------------------FILTER---------------------------------------------
# The filter function filters a sequence of elements based on a given predicate (a function that returns a boolean value) and returns a new sequence containing only the elements that meet the predicate. The filter function has the following syntax:

# filter(predicate, iterable)

# The predicate argument is a function that returns a boolean value and is applied to each element in the iterable argument. The iterable argument can be a list, tuple, or any other iterable object.

# Here is an example of how to use the filter function:
pred = lambda x: x > 5
lst = [i for i in range(1, 11) if i % 2 == 0]

# With Filter (1 line):
var = filter(pred, lst)
print('Filter:', list(var))

# Instead of Filter (5 lines):
newlst = []
for number in lst:
    if number > 5:
        newlst.append(number)
print('Loop:', newlst)

# ---------------------------------------------REDUCE---------------------------------------------
# The reduce function is a higher-order function that applies a function to a sequence and returns a single value. It is a part of the functools module in Python and has the following syntax:

# reduce(function, iterable)

# The function argument is a function that takes in two arguments and returns a single value. The iterable argument is a sequence of elements, such as a list or tuple.

# The reduce function applies the function to the first two elements in the iterable and then applies the function to the result and the next element, and so on. The reduce function returns the final result.

# Here is an example of how to use the reduce function:
from functools import reduce

func = lambda x, y: x + y
lst = [i for i in range(1, 11)]

var = reduce(func, lst)
print('Reduce:', var)
    