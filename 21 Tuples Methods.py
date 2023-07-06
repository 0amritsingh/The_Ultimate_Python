# Tuple Method In Python

# You can't chage a tuple, BUTT!! you can do it by converting it into list. Just follow the steps below:-
# Step 1: Make a Tuple
# Step 2: Convert it into list
# Step 3: Do changes ( you can even apply list methods in that also )
# Step 4: Convert in into tuple again
# And there you go

tup = (12, 2, 23, 5, 12, 64, 6, 2, 27, 3, 8, 1, 2, 46) # Make a Tuple

con_t2l = list(tup) # convert it into list

con_t2l[3] = 45                   #         
con_t2l[8] = "hero"               #         
print(con_t2l[8].upper())         #         Make changes as
print(con_t2l[8].islower())       #         many as you can
if "hero" in con_t2l:             #         
    print("Yes There is a Hero")  #         

con_l2t = tuple(con_t2l) # Convert it again into Tuple
print(con_l2t) 

# Some Methods in Tuple

t = (0, 1 ,2 ,3 ,4 ,"five" ,4 ,3 ,2 , 1, 0)
print(t.count(4)) # It tells the total number of occurrence of the given value 
print(t.index(3)) # It locates the first occurrence of the given value by indexing
print(t.index(4, 5, 10)) # We can find the value in the given slice of the Tuple
# there are only few of them like "Boolean types", basicaly those which cannot change the tuple just give some data about tuple like isupper, isalnum, etc. But you can apply all methods of list by converting it into list as we did earliar.