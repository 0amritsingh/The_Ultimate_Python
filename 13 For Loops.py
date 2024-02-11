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
# 3. Step: range[(start: int), (stop: int), (step: int)]
z = range(1, 11, 2) # in this it will print value after a jump
for k in z:
    print(k) # in this case ther is a step of 2 it means 2-1=1 it will skip one(only) interger between two adjicant intergers like "1234" then "13" it skipped 2 and 4 i.e "1 [2] 3 [4]". Now lt's sppose there a step of 3 means 3-1=2 then it will skip two(only) interger between two adjicant intergers like "1234" then "14" it skipped 2 and 3 i.e "1 [2] [3] 4"
