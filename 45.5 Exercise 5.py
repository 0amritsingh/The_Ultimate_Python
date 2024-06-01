# Snake Water Gun Game in Python

import random

print('\nSnake Water Gun') # Starter Screen
# Take: 0 - Snake, 1 - Water, 2 - Gun
items = ['Snake🐍', 'Water💧', 'Gun🔫']
results = ['Draw!🙂', 'You Win!😁', 'You Lose!😥']

            # Python's Choice 
            #       0          1          2 
condition =[[results[0], results[1], results[2]], # 0 Player's Choice 
            [results[2], results[0], results[1]], # 1 Player's Choice 
            [results[1], results[2], results[0]]] # 2 Player's Choice 

i = int(input(f'\n[1] {items[0]}\n[2] {items[1]}\n[3] {items[2]}\n>>> ')) - 1    # Player's Input
j = random.randint(0,2) - 1                                                      # Python's Input

output = f'\nPlayer Choose: {items[i]}\nPython Choose: {items[j]}\nResult: {condition[i][j]}\n' # Output Template

def play():
    print(output) if condition[i] == condition[j] or condition[i] != condition[j] else print()

play()
    