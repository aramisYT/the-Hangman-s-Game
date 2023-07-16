import linecache
import random
import time
import os

img = ("==========Y=\n ", "||/       |\n ", "||        0\n ", "||       /|\ \n ", "||       /|\n", "||\ \n", "=============\n")
timetosleep = 1
timetosleep2 = 2

def clear():
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')
    else:
        print("your operating system is not supported by part of the code, the experience may not be optimal. ( the os supported are : Windows, MacOS and a part of linux systems ! )")

def game():

    letters = ""
    attempt = 0
    word = linecache.getline('French_WordBook.txt', random.randint(1, 22735)).strip()
    
    while True:

        clear()

        word_blur = ""

        for x in word:
            if x not in letters:
                word_blur += "_"
            else:
                word_blur += x

        print("the word to guess is :", word_blur, "\n")

        if word_blur == word:
            print("you have find the word.\n")
            restart()

        for x in range(0, attempt):
            print(img[x].strip())

        if attempt == 7:
            clear()
            print("you have no longer attempt remaining.\n")
            print("the answer was :", word, "\n")
            time.sleep(timetosleep2)
            restart()

        user_input = input("\nenter a letter.\n--> ")

        if len(user_input) > 1:
            print("\nError : you have to enter only one letter !\n")
            time.sleep(timetosleep)
        elif not user_input.isalpha():
            print("\nError : you have to enter a letter !\n")
            time.sleep(timetosleep)
        elif user_input in letters:
            print("\nError : you have already entered this letter !\n")
            time.sleep(timetosleep)
        elif user_input in word :
            letters += user_input
            print("\nthis letter is in the word.")
            time.sleep(timetosleep)
        elif user_input not in word:
            attempt += 1
            letters += user_input
            print(f"\nthis letter is not in the word, you have {7 - attempt} attempt remaining.\n")
            time.sleep(timetosleep)

def restart():

    while True:

        clear()

        ask_for_restart = input ("do you want to restart a game ( yes / no ) ?\n--> ")

        if ask_for_restart == "no":
            quit()
        elif ask_for_restart == "yes":
            game()
        else:
            print("Error : you have to answer with \"yes\" or \"no\" ! ")

game()
