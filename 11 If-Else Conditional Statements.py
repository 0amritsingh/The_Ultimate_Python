# If Else Conditional Statemnts in Python

# Conditional Operators for if-else:
# <, >, <=, >=, ==, !=

# these are of four types: 
# if-else:

a = int(input("Enter 1 to print first message\nEnter 2 to print second message\n>>> "))
if(a == 1):
    print("Hey! How you're you?")
else:
    print("Wassup Homie! How you doin' bro?")

# if-else-elif:

b = int(input("Enter 1 to print first message\nEnter 2 to print second message\nEnter 3 to print third message\n>>> "))
if(b == 1):
    print("Hey! How you're you?")
elif(b == 2):
    print("YO! buddy let's go there.")
elif(b == 3):
    print("you can put infinite elif :)")
else:
    print("ERROR! you entered invailed number.")

# nesked if-else

c= int(input("Meet Jhon the Shopkeeper:\n1. Hey!       2.Fuck off!\n>>> "))
if(c==1):
    print("Hello! can I help you?\n")
    c=int(input("1. Do you have chocolate       2.Get the fuck out of my way.\n>>> "))
    if(c==1):
        print("Yes, I have....\nHere you go. Only $9")
        c=int(input("1. Here... Thank you so much.       2.*Leave room withour giving money*\n>>> "))
        if(c==1):
            print("Must welcome... Come again!")
        elif(c==2):
            print("Hey! motherfucker you Stealing my Chocolate.\n*calling 199*")
        else:
            print("Invailed Input. Try again")
    elif(c==2):
        print("go to hell you bastured")
    else:
        print("Invailed Input. Try again")
elif(c==2):
    print("Who do you think you are. MotherFucker!!\n")
else:
    print("Invailed Input. Try again")