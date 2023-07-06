# MatchCase in Python

# it is like if else but is act like else 
# understand it with a example:
# this will match the value of a in each case and which every matchs correctly it will exicute that code of that particular case not aany other 

a = int(input("Enter number form 1 to 5\n>>> "))
match a: 
    case 1:
        print("You entered One")
    case 2:
        print("You entered Two")
    case 3:
        print("You entered Three")
    case 4:
        print("You entered Four")
    case 5:
        print("You entered Five")
    case _ if a < 1:
        print("Your number less than 1")
    case _ if a > 5:
        print("Your number greater than 5")
    case _ if a == 6: # as in this case if you enter 6 this code will not exicute because 6 is greater than 5 so the above case will print as pyhton interpretor exicute code line by line.
        print("You entered Six") 