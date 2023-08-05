# Dictionary Methods in Python

# 1. update():
# The update() method updates the value of the key provided to it if the item already exists in the dictionary, else it creates a new key-value pair.
a = {1: "Alice", 2: "Anny", 3: "Charli", 4: "David"}
a2 = {5: "Franklin", 6: "John"}
a.update(a2)
print(a)

# 2. clear():
# The clear() method removes all the items from the list.
b = {1: "Alice", 2: "Anny", 3: "Charli", 4: "David"}
b.clear()
print(b)

# pop():
# The pop() method removes the key-value pair whose key is passed as a parameter.
c = {1: "Alice", 2: "Anny", 3: "Charli", 4: "David"}
c.pop(2)
print(c)

# popitem():
# The popitem() method removes the last key-value pair from the dictionary.
d = {1: "Alice", 2: "Anny", 3: "Charli", 4: "David"}
d.popitem()
print(d)

# del:
# we can also use the del keyword to remove a dictionary item.
e = {1: "Alice", 2: "Anny", 3: "Charli", 4: "David"}
del e[3]
print(e)
# If key is not provided, then the del keyword will delete the dictionary entirely.
e2 = {1: "Alice", 2: "Anny", 3: "Charli", 4: "David"}
del e2
print(e2)
