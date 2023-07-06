# Funcation Arguments in Python:

# 1. Default Arguements: 
def into(a = 4, b = 5):
    print("The multiple of", a, "and", b, "is", a*b)
    
into() # In this case you have already giving value of 'a' and 'b' which is knows as default values.
# If you give values again while calling the funcation then python will 'ignores' the default values.
into(9, 2) # In this way it give importance to these values

into(7) # So, in this case the value of 'a' will change and the value of 'b' stay default.
into(b = 2) # Same with the 'b' and 'a' remains default.

# 2. Keyword argument:

# In this you can give arguements by using particular variable.
into(a = 6, b = 3) 
into(b = 3, a = 2) # And obvealy you don't need to worry about the order of the variables.

# 3. Required Arguement: 

# let's take another one 
def add(a, b, c = 3):
    print("The sum of", a, ", ", b, "and", c, "is", a + b + c)
    
add(5, 4) # well 'a' and 'b' are required arguements which user have to define otherwise the code will throw error

# Variable lenght Aruguement:

# its basicly using 'tuple' and 'dict' as an arguement in a funcation
# we'll see it in future and come back and code an example for it.