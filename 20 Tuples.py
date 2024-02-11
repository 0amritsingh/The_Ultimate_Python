# Tubles in Python

# Tuples are Immutable and List is mutable.
# Tuples are like list and butt they can not change (tuple[0] = 34, this code will thorw error), yess we can do indexing and slicing in tuples.

t = (1, 2, 3, 4, 5) # We can make a tuple of multiple elements obviously
print(type(t), t)
# But what if we need to create a single element tuple
t2 = (1)
print(type(t2), t2) # Yess, pyhton confuses this with int, to fix this make a comma to tell python that it is a tuple
t3 = (1,)
print(type(t3), t3)

# indexing and slicing of a tuple
tup = (1, 3, 34, 4.65, "hack", False)
print(tup)
print(len(tup))
print(tup[0])
print(tup[3])
print(tup[4])
print(tup[-4])
print(tup[4:7])
print(tup[2:])
print(tup[:3])

# also check by applying conditon
if "hack" in tup:
    print("Yess hack is present in the tuple.")

