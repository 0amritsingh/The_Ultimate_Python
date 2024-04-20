# Break and Continue in Python:

# Break: Exits the Loop

for i in range(1, 11):
    if (i == 5):
        break # skip all the remaining iterations and end/break/exit the loop
    print(i)
    
# If you write line 6 and 7 after line 8 it will print 5 and then break the loop. YOU ALREADY KNOW WHY :)

print("\n")

#Continue: Exits the very Itration

for j in range(1, 11):
    if (j == 5):
        continue # skips only one(as per condition) iteration and continue(from the next iteration) the loop
    print(j)
    
# So, in previous chapter we learned about while loops and emulation of do-while loop.
# Now you know that what is break statement and we are emulating do-while loop with this statement.
# The following example is the best way to understand: 

# We can do this by an infinite while loop like this-
# while ture:
#     loop body;
    
while True:
    n = int(input("Enter a positve number: ")) # this code will run the first
    print(n)
    if (n<0): # this is the loop condition, if satisfied then run agian else break(out of loop).
        break
print("Break")
 