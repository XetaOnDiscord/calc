# Made by HaoX#0001 on discord
# Linux Version

from time import sleep
import os


def clear(): return os.system('clear')


clear()

print("Welcome to your calculator!")

def calc():

    x = int(input("First number: "))

    userInput = input("Choose a function(+,-,*,/,^,<,>): ")

    y = int(input("Second number: "))
    if userInput == "+":
        result = x + y
        print(result)
        sleep(1.5)
        clear()
        calc()

    elif userInput == "-":
        result = x - y
        print(result)
        sleep(1.5)
        clear()
        calc()

    elif userInput == "*":
        result = x * y
        print(result)
        sleep(1.5)
        clear()
        calc()

    elif userInput == "/":
        result = x / y
        print(result)
        sleep(1.5)
        clear()
        calc()

    elif userInput == "^": 
        result = x**y
        print(result)
        sleep(1.5)
        clear()
        calc()
        
    else:
        print("Something wen't wrong! Try again")
        sleep(1)
        clear()
        calc()
calc()
