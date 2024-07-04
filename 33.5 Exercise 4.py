# Exercise 4: Secret Code Language
import random
import time

def loading_bar(length=15, duration=1.8): # extra feature (picked from internet)
    for i in range(length + 1):
        bar = '#' * i + ' ' * (length - i)
        print(f'\r[{bar}]', end='', flush=True)
        time.sleep(duration / length)
    print()

def encoding():# EnCoding: converting normal english sentance to secret code sentance
    sentance = input("Enter your Sentance here:\n>>> ")
    words_list = sentance.split(' ')
    coded_words_list = []

    for i in words_list:
        if (len(i) < 4):
            coded_words_list.append(i[::-1])
        else:
            three_random_chars = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=3))
            middle_chars = i[1:]+i[0]
            coded_words_list.append(''.join([three_random_chars,middle_chars,three_random_chars]))

    code = ' '.join(coded_words_list)
    print('>>>',code)

def decoding():# DeCoding: converting secret code sentance to normal english sentace
    code = input("Enter your Code here:\n>>> ")
    coded_words_list = code.split(" ")
    words_list = []

    for i in coded_words_list:
        if (len(i) < 4):
            words_list.append(i[::-1])
        else:
            middle_chars = i[3:-3]
            actual_chars = middle_chars[-1]+middle_chars[:-1]
            words_list.append(actual_chars)

    sentance = ' '.join(words_list)
    print('>>>',sentance)

print("__Hacker's Chat__")
loading_bar()
while True:
    x = input("\n[E]N-CODING\n[D]E-CODING\n[Q]UIT\n$ ")
    if x in 'eE':
        print()
        encoding()
    elif x in 'dD':
        print()
        decoding()
    elif x in 'qQ':
        print()
        break
    else:
        print()
        print('ERROR: wrong input')
 
