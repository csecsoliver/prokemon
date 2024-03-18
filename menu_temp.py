import colorama

from classes import Stats
from shared import game_time_to_string, json_from_file


def intro():
    print("--- BKK Simulator ---")
    for line in json_from_file("data/intro.json"):
        input(line)
    for i in range(10):
        print("\x1B[2J")


def display_menu(stats: Stats, dialog: str, options: list[str], line_length_override: list[int] | None = None):
    print("\x1B[2J")
    print("-" * 61)
    
    for i in range(5):
        if i < len(options):
            print(f"│ {f"{i + 1}. {options[i]}".ljust(57)} │")
        else:
            print("│" + " " * 59 + "│")
    print("-" * 61)


def display_text_and_wait(stats: Stats, text: str, line_length_override: list[int] | None = None):
    display_menu(stats, text, [], line_length_override)
    input("[ENTER]")
