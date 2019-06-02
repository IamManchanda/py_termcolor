from termcolor import colored
from pyfiglet import figlet_format


def ascii_art(message, color):
    valid_colors = ("red", "green", "yellow", "blue",
                    "magenta", "cyan", "white")
    if color not in valid_colors:
        print(
            f"As color {color} is not in valid color list, color will be printed in cyan")
        color = "cyan"
    return colored(figlet_format(message), color=color, attrs=["bold", "dark"])


message = input("What would you like to print?\n")
color = input("What color?\n").lower()
print(ascii_art(message, color))
