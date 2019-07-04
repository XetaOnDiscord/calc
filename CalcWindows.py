# Made by HaoX#0001 on discord
# Windows Version

from time import sleep
import os


def cls(): return os.system('cls')


cls()

print("Welcome to your calculator!")

def calc():

    x = int(input("First number: "))

    userInput = input("Choose a function(+,-,*,/,^,<,>): ")

    y = int(input("Second number: "))
    if userInput == "+":
        result = x + y
        print(result)
        sleep(1.5)
        cls()
        calc()

    elif userInput == "-":
        result = x - y
        print(result)
        sleep(1.5)
        cls()
        calc()

    elif userInput == "*":
        result = x * y
        print(result)
        sleep(1.5)
        cls()
        calc()

    elif userInput == "/":
        result = x / y
        print(result)
        sleep(1.5)
        cls()
        calc()

    elif userInput == "^": 
        result = x**y
        print(result)
        sleep(1.5)
        cls()
        calc()
        
    else:
        print("Something wen't wrong! Try again")
        sleep(1)
        cls()
        calc()
calc()

