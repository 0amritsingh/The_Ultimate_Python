# List Methods in Python:

l = [2, 23, 46,1 ,2 ,3 ,34 ,6 ,15 ,2 ,5 ,6]
print(l) # This will print list simply

l.sort() # This will short the list in assending order
print(l)

l.sort(reverse = True) # This will short the list in dessending order
print(l)

l.append(5) # This will add a element in the end of the list and uptade the list by making a copy of the original one.
print(l)

l.reverse() # Obviously this will reverse the list
print(l)

print(l.index(3)) # This will give the indexing of the particular element of list

print(l.count(2)) # This will count occurance of a particular element in the list

print(l.copy()) # this will duplicate your current list

l.insert(3, 999) # This will help you to insert any element in the very list at a particular index. "listname.insert(index, element to be insert)"
print(l)

# What if you want to add multiple elements in the list, for this you have to make a new list of those elements and use the following menthod
m = [444, 555, 666, 777]
l.extend(m) # this lines says- extend m in l
print(l)

# So, this is besicly the concatinating two list. but by using extend() the original list will change, if we want to concatinate two or ever more list together by making a new list (it will not effect to the orignal list) we can simply do this: 
k = l + m # k is completely a new list it it.
print(k)
