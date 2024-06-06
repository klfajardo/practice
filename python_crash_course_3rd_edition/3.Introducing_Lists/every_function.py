import time
import os

# Refs:
# https://stackoverflow.com/questions/517970/how-can-i-clear-the-interpreter-console
# https://www.freecodecamp.org/news/python-switch-statement-switch-case-example/


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


operations = ["sort", "sort reverse", "reverse", "length"]
myList = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o",]

while True:
    print(f"List: {myList}")

    print(f"\nOperations: {operations}")
    user_input = input("Enter an operation: ").strip().lower()

    match user_input:
        case "sort":
            myList.sort()
        case "sort reverse":
            myList.sort(reverse=True)
        case "reverse":
            myList.reverse()
        case "length":
            print(len(myList))
            time.sleep(2)
        case _:
            print("Error: enter a supported command.")
            time.sleep(2)
    cls()
