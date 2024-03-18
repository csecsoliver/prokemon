# import colorama

# from classes import Stats
# from shared import game_time_to_string, json_from_file


# def intro():
#     print("--- BKK Simulator ---")
#     for line in json_from_file("data/intro.json"):
#         input(line)
#     for i in range(10):
#         print("\x1B[2J")


# def display_menu(stats: Stats, dialog: str, options: list[str], line_length_override: list[int] | None = None):
#     print("\x1B[2J")
#     print("-" * 61)
#     location = stats.location
#     location_length = len(location)
#     vehicle = stats.current_vehicle
#     if vehicle is not None:
#         line = vehicle.line
#         location = f"{line.name} -> {vehicle.destination_name()}"
#         location_length = len(location)
#         location = f"{line.color}{location}{colorama.Fore.RESET}"
#     print("│ " + f"{location}" + " " * (52 - location_length) + game_time_to_string(stats.elapsed_time) + " │")
#     print(f"│ Pénz: {stats.money: 17} Ft │ Energia: {stats.stamina: 18}% │")
#     print(f"│ Jegyek: {stats.tickets: 15} db │ Bérlet: {stats.remaining_pass_time: 15} perc │")
#     print(f"│ Cél: {(stats.quest if stats.side_quest is None else stats.side_quest).ljust(52)} │ ")
#     print("-" * 61)
#     dialog_lines = dialog.split("\n")
#     if len(dialog_lines) == 1:
#         dialog_lines.append("")
#     for i, line in enumerate(dialog_lines):
#         length = len(line) if line_length_override is None or len(line_length_override) <= i else line_length_override[i]
#         print(f"│ {line}{" " * (57 - length)} │")
#     print("-" * 61)
#     for i in range(5):
#         if i < len(options):
#             print(f"│ {f"{i + 1}. {options[i]}".ljust(57)} │")
#         else:
#             print("│" + " " * 59 + "│")
#     print("-" * 61)


# def display_text_and_wait(stats: Stats, text: str, line_length_override: list[int] | None = None):
#     display_menu(stats, text, [], line_length_override)
#     input("[ENTER]")
