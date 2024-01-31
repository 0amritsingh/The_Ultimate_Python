# List Methods in Python:

l = [1,2,3,4,5]
print(len(l)) # This will print the lenth of list


l = [5,4,6,7,8,2,3,1,0,9]
l.sort() # This will short the list in assending order
print(l)


l = [5,4,6,7,8,2,3,1,0,9]
l.sort(reverse = True) # This will short the list in dessending order
print(l)


l = [1,2,3,4]
l.append(5) # This will add a element in the end of the list and uptade the list by making a copy of the original one.
print(l)


l = [1,2,3,4,5,6,7,8,9,10]
l.reverse() # Obviously this will reverse the list
print(l)


l = [1,2,3,4,5] # indexing for element: [0=1, 1=2, *2=3*, 3=4, 4=5]
print(l.index(3)) # This will give the indexing of the particular element of list


l = [1,2,2,2,3,2,4,2,5,2]
print(l.count(2)) # This will count occurance of a particular element in the list


l = ["duplicate", "this", "list"]
print(l.copy()) # this will duplicate your current list


l = [1,2,3,4]
l.insert(3, 999) # This will help you to insert any element in the very list at a particular index. "listname.insert(index, element to be insert)"
print(l)


# What if you want to add multiple elements in the list, for this you have to make a new list of those elements and use the following menthod
l = [111,222,333]
m = [444, 555, 666]
l.extend(m) # this lines says- extend m in l
print(l)
# NOTE: So, this is besicly the concatinating two list. but by using extend() the original list will change, if we want to concatinate two or ever more list together by making a new list (it will not effect to the orignal list) we can simply do this: 
k = l + m # k is completely a new list it it.
print(k)


l = [1,2,3,4,5,3]
l.remove(3) # remove the first occurance of the given item
print(l)
# ***simple program on remove funcaiton***
l = [0,2, 1,2, 2,2, 3,2, 4,2, 5,2]
while (2 in l):
    l.remove(2)
    # print(l)
    # print ^this to see the whole working of loop
print(l)
 
 
l = [1,2,3,4,5]
l.pop() # Remove the last element of the list (only if no argument is given)
print(l)
l = [1,2,3,4,5]
l.pop(0) # by giving index as argument it will remove only that particular element
print(l)
l = [1,2,3,4,5]
x = l.pop(3) # we can store the removed element
print(x) # we can print the removed element
