from handlers.command_handler import CommandHandler
import pyfiglet
from colorama import Fore

def main():
    command_handler = CommandHandler()
    command_handler.display_logo()

    while True:
        command = input(f"{Fore.LIGHTRED_EX}Enter command: ").strip().split()
        if not command:
            continue

        command_name = command[0]
        command_args = command[1:]

        result = command_handler.execute(command_name, *command_args)
        print(result)

if __name__ == "__main__":
    main()
