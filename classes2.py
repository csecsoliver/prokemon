import classes
import platform
import os


def clearscreen():
    match platform.system():
        case "Windows":
            os.system("cls")
        case "Linus":
            print("WTF are you doing?")
        case "Linux":
            os.system("clear")
        case "Darwin":
            os.system("clear")
        case "Java":
            print("Why? Cannot clear the screen.")
        case _:
            print("Incompatible system, cannot clear the screen")