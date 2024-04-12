# Exception Handling:

# Well, I see exception like it's a portal between the error that opens a gate towards the other line of code (I think so I explain so well lmao :D).

# Basic template:

# try:
#      #statements which could generate 
#      #exception
# except:
#      #Soloution of generated exception

# So, It works with two cammands try and except:

# Try: try first try the code(in which error is expected) and if we got error while trying, it skip the error and print the exception massage(if any) and move to the other line of code. Like I said like a portal.

# Except: we use except(i.e. print other code EXCEPT the error) we do not recive an error. Instead of it we can recive a massage(line no. 18) or nothing and the other remaining line of code will proceed. Like in the following, case line no. 19 & 20.

# Try & Except:
try:
    num = input("Enter a number: ")
    print(f"The Multiplication Table of {num}:")
    for i in range(1, 11):
        print(f"{int(num)} x {i} = {int(num)*i}")
except:
    print("\nEnter a interger value, RUN again!\n") # auther's massage.
print("Some imp. line of code!") # these are remaining code.
print("End of the code!") # which does not run if we don't use exception.

# We can also hand Specific Error and Multiple Errors. As we already learned types of Error in the previous lesson ngl.

# Handling a Specific Error:
try:
    a = int(input("Enter a integer: "))
    print(a)
    print("If you see this line it means you entered a correct value")
except ValueError as b: # we and print the massage by python by taking it as varible.
    print(f"{b} you entered wrong value, RUN again!")

# Handling Multiple Errors
try:
    num = int(input("Enter an integer: "))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")
except IndexError:
    print(f"There are only {len(a)} elements in the list\nYou entered {num} which is not valid, RUN again!")
    
# NOTE: In future we'll make some of the programs in which we need to handle some exceptions to make our program work :)