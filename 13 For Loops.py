# For Loops in Python
# String in Loops:
x = "python"
for i in x:
    print(i)
# String acts as an array, loops take it all charaters as a object.
print("\n")
# List in Loops:
y = ["red", "green", "blue", "yellow"]
for j in y:
    print(j)
# List acts as an array, loops take it all charaters as element.
print("\n")
# Range in Loops:
# 1. Stop: range[(start: 0), (stop: int)]
z = range(10)
for k in z:
    print(k)
# It always starts form zero and stops at the given int
print("\n")
# 2. Start: range[(start: int), (stop: int)]
z = range(1, 11)
for k in z:
    print(k)
# It start with a given integer (X) and stop at given integer (Y-1)
print("\n")
# 3. Step: range
z = range(1, 11, 2)
for k in z:
    print(k)