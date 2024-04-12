# Exception Handling:

# Well, I see exception like it's a Portal between the error that opens a gate towards the other line of code (I think so I explain so well lmao :D).

# Basic template:

# try:
#      #statements which could generate 
#      #exception
# except:
#      #Soloution of generated exception

# So, It works with two commands try and except:

# Try: It first try the code(in which error is expected) and if we got error while trying, it skip the error and print the exception massage (if any) and move to the other line of code. Like I said, "a portal".

# Except: We use Except (i.e. print other code EXCEPT the error) so that we do not recive an error. Instead of that we can recive a massage (line no. 26) or nothing and the other remaining lines of code will proceed. Like in the following case, line no. 27 & 28.

# Try & Except:
try:
    a = input("Enter a number: ")
    print(f"The Multiplication Table of {a}:")
    for i in range(1, 11):
        print(f"{int(a)} x {i} = {int(a)*i}")
except:
    print("\nEnter a interger value, RUN again!\n") # auther's massage.
print("Some imp. line of code!") # these are remaining code.
print("End of the code!") # which does not run if we don't use exception.

# We can also handle Specific Error and Multiple Errors. As we already learned types of Error in the previous lesson.

# Handling a Specific Error:
try:
    b = int(input("Enter a integer: "))
    print(b)
    print("If you see this line it means you entered a correct value")
except ValueError as e: # we and print the massage by python by taking it as varible.
    print(f"{e} you entered wrong value, RUN again!")

# Handling Multiple Errors
try:
    n = int(input("Enter an integer: "))
    c = [0, 1]
    print(c[num])
except ValueError:
    print("Number entered is not an integer.")
except IndexError:
    print(f"There are only {len(c)} elements in the list\nYou entered {n} which is not valid, RUN again!")
    
# NOTE: In future we'll make some of the programs in which we need to handle some exceptions to make our program work :)
