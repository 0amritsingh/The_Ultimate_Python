# Comment 
# You Know this is a comment
#--------------------------------------------------------------------------------
#Escape Sequesces
print("I want a new line\nYeah, we got it.")
# \n is a escape sequesce that can "create a new line". Basicaly to avoid error as if we do in the the actuall code.
print("I want double \"colons\"")
print('I want single \'colons\'')
# \" or \' is a escape sequence that creates double colons in the very stings
#--------------------------------------------------------------------------------
# We can use single and double colons to write a sting.
# And can replace them with our conviance
print('"Double Colons"')
print("'Single Colons'")
#--------------------------------------------------------------------------------
# You can write multiple stings in one print statement
print("Wassup!", "Homie", "can you gemmie", 10, "bucks")
#--------------------------------------------------------------------------------
# Perameters of print statement
# sep is use to seperate the multiple stings (space default seperator).
# But if you want to seperate them with a character, use sep="" after comma
print(1, 2, 3, sep=".")
# end is another perameter that is use to print the next statement in same or previous line
print(1, 2, end=" ")
print(3)