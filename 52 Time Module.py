import time
import random

# time.time() - this mehtod will give you the no. of seconds from 1 jan 1970 to now. from this you can check how much time your code has taken to execute.
'''
init = time.time()
for i in range(101):
    print(i)
print(time.time() - init)
'''

# time.sleep() - this will delay the exicuation of the code 
'''
x = int(input('Patience cheaker, enter no.: '))
print(f'your massege will print after {x} seconds')
time.sleep(x)
famous_quotes = [
    "Be yourself; everyone else is already taken. – Oscar Wilde",
    "Two things are infinite: the universe and human stupidity; and I'm not sure about the universe. – Albert Einstein",
    "So many books, so little time. – Frank Zappa",
    "A room without books is like a body without a soul. – Marcus Tullius Cicero",
    "In three words I can sum up everything I've learned about life: it goes on. – Robert Frost",
    "If you tell the truth, you don't have to remember anything. – Mark Twain",
    "Always forgive your enemies; nothing annoys them so much. – Oscar Wilde",
    "To live is the rarest thing in the world. Most people exist, that is all. – Oscar Wilde",
    "We accept the love we think we deserve. – Stephen Chbosky",
    "Life is what happens to us while we are making other plans. – Allen Saunders"
]
print(famous_quotes[random.randint(1, 10)])
'''

# time.localtime() - this will give you now
print(time.localtime())

# time.srftime() - this will organize the above method 
print(time.strftime('Date: %Y-%m-%d \nTime: %H:%M:%S'))
    