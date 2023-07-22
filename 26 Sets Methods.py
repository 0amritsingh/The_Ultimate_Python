# Sets Methods in Python

# These are some of the most common methods of sets:

# Union and Update:
seta = {1,2,3,4,5}
setb = {4,5,6,7,8}
print(seta.union(setb)) # A∪B (It will add all elements of seta in setb)
seta.update(setb) # this will update my seta make a new set which shows A∪B
print(seta) # and now if we print seta it can be seen updated

# Intersection and Intersection Update:
seta = {1,2,3,4,5}
setb = {4,5,6,7,8}
print(seta.intersection(setb)) # A∩B (It will has only those elements which are common in both sets)
seta.intersection_update(setb) # this will update my seta make a new set which shows A∩B
print(seta) # and now if we print seta it can be seen updated

# Symmetric Difference and Symmetric Difference Update:
seta = {1,2,3,4,5}
setb = {4,5,6,7,8}
print(seta.symmetric_difference(setb)) # AΔB (It will has only those elements which are uncommon in both sets)
seta.symmetric_difference_update(setb) # this will update my seta make a new set which shows AΔB
print(seta) # and now if we print seta it can be seen updated

# Difference and Difference Update:
seta = {1,2,3,4,5}
setb = {4,5,6,7,8}
print(seta.difference(setb)) # A-B (It will has only those elements which belongs only to seta. The elements which are common in both and all the elements of setb will not be taken)
seta.difference_update(setb) # this will update my seta make a new set which shows A-B
print(seta) # and now if we print seta it can be seen updated\
    
# Some other methods of sets

# isdisjoint:
# Means:- Two sets are said to be disjoint sets if they have no element in common. Equivalently, two disjoint sets are sets whose intersection is the empty set. 
seta = {1,2,3,4,5}
setb = {4,5,6,7,8}
print(seta.isdisjoint(setb))
# In this case both sets have common elements so the output is FALSE.

# issuperset:
# Means:- set A is considered as the superset of B, if all the elements of set B are the elements of set A
setx = {1,2,3,4,5,6}
seta = {1,2,3}
setb = {4,5,6}
setc = {7,8,9}
print(setx.issuperset(seta))
print(setx.issuperset(setb))
print(setx.issuperset(setc))
# In this case setx is a superset containing 6 elements and set a and b are subset of setx as they contain elements that belongs to setx, but setc do not contain any elements that belongs to setx so the output for setc is FALSE.

# issubset:
# Means:- Set A is said to be a subset of Set B if all the elements of Set A are also present in Set B
setx = {1,2,3,4,5,6}
seta = {1,2,3}
setb = {4,5,6}
setc = {7,8,9}
print(seta.issubset(setx))
print(setb.issubset(setx))
print(setc.issubset(setx))
# In this case setx is a superset containing 6 elements and set a and b are subset of setx as they contain elements that belongs to setx, but setc do not contain any elements that belongs to setx so the output for setc is FALSE.

# add:
# Means:- If you want to add a single item to the set use the add() method.
seta = {1,2,3,4}
seta.add(5) # it will updates the seta
print(seta) # it will returns the seta

# update:
# Means:- If you want to add more than one item, simply create another set or any other iterable object(list, tuple, dictionary), and use the update() method to add it into the existing set.
seta = {1,2,3,4}
setb = {5,6,7,8}
seta.update(setb) # this will update my seta make a new set.
print(seta)

# Remove and Discard:
# Means:- We can use remove() and discard() methods to remove items form list. The main difference between remove and discard is that, if we try to delete an item which is not present in set, then remove() raises an error, whereas discard() does not raise any error.
seta = {1,2,3,4,5}
seta.remove(5)
print(seta)
seta = {1,2,3,4,5}
seta.discard(5)
print(seta)

seta = {1,2,3,4,5}
# seta.remove(6)# this will thow error
# print(seta)
seta = {1,2,3,4,5}
seta.discard(6)
print(seta)

# Pop:
# Means:- This method removes the last item of the set but the catch is that we don’t know which item gets popped as sets are unordered. However, you can access the popped item if you assign the pop() method to a variable.
seta = {0,2,4,6,8}
popped_item = seta.pop()
print(seta, popped_item)

# del:
# Means:- del is not a method, rather it is a keyword which deletes the set entirely.
seta = {1,2,3,4,5}
del seta
# print(seta)
# This will thow an error as in line no. we deleted the seta so it will not be exicuted

# What if we don’t want to delete the entire set, we just want to delete all items within that set?
# In that case we will use clear() method.

# Clear:
# This method clears all items in the set and prints an empty set.
seta = {12,34,56,78,90}
seta.clear()
print(seta)

# Check if item exists:
# You can also check if an item exists in the set or not
seta = {5,3.4,"OK",True}
if "OK" in seta:
    print(f"Yes 'OK' is in the set")
else:
    print("No their is no 'OK' in this set")
