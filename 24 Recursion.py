# Recursion in python
# Recursion is the process of defining something in terms of itself.

# Python Recursive Function
# In Python, we know that a function can call other functions. It is even possible for the function to call itself. These types of construct are termed as recursive functions.

# See a example below:

def factorial(num):
    if (num == 0 or num == 1):
        return 1
    else:
        return (num * factorial(num - 1))# # # #
                                               #
print(factorial(5))                            #
                                               #
## # # # # # # # # # # # # # # # # # # # # # # #
# How is program works:
# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1
# Output: 120
