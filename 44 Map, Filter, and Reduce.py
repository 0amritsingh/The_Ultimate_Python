# MAP
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

# FILTER
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

# REDUCE
from functools import reduce

func = lambda x, y: x + y
lst = [i for i in range(1, 11)]

var = reduce(func, lst)
print('Reduce:', var)
