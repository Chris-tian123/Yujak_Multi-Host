import os
import psutil
import pyfiglet
from colorama import Fore, init
from handlers.bot_handler import BotHandler

init(autoreset=True)

class CommandHandler:
    def __init__(self):
        self.bots = self.load_bots()

    def load_bots(self):
        bot_dirs = [d for d in os.listdir("bots") if os.path.isdir(os.path.join("bots", d))]
        return {bot_name: BotHandler(bot_name) for bot_name in bot_dirs}

    def execute(self, command, *args):
        try:
            if command == "help":
                return self.help()
            elif command == "start":
                return self.start_bot(*args)
            elif command == "stop":
                return self.stop_bot(*args)
            elif command == "restart":
                return self.restart_bot(*args)
            elif command == "list":
                return self.list_bots()
            elif command == "mem":
                return self.memory_status()
            elif command == "status":
                return self.status()
            else:
                return f"{Fore.RED}Unknown command. Use {Fore.GREEN}'help'{Fore.RED} for a list of commands."
        except Exception as e:
            return f"{Fore.RED}Error: {e}"

    def start_bot(self, bot_name):
        bot = self.bots.get(bot_name)
        if bot:
            return bot.start()
        return f"{Fore.RED}Bot {bot_name} not found."

    def stop_bot(self, bot_name):
        bot = self.bots.get(bot_name)
        if bot:
            return bot.stop()
        return f"{Fore.RED}Bot {bot_name} not found."

    def restart_bot(self, bot_name):
        bot = self.bots.get(bot_name)
        if bot:
            bot.stop()
            return bot.start()
        return f"{Fore.RED}Bot {bot_name} not found."

    def list_bots(self):
        return "\n".join([f"{Fore.CYAN}{bot_name}" for bot_name in self.bots]) if self.bots else f"{Fore.YELLOW}No bots available."

    def status(self):
        statuses = [f"{Fore.GREEN}{bot_name}{Fore.WHITE}: {bot.status()}" for bot_name, bot in self.bots.items()]
        return "\n".join(statuses) if statuses else f"{Fore.YELLOW}No bots available."

    def memory_status(self):
        memory = psutil.virtual_memory()
        return (
            f"{Fore.CYAN}Total Memory: {memory.total / (1024 * 1024):.2f} MB\n"
            f"Used Memory: {memory.used / (1024 * 1024):.2f} MB\n"
            f"Free Memory: {memory.free / (1024 * 1024):.2f} MB\n"
            f"Memory Usage: {memory.percent}%"
        )

    def help(self):
        return f"""{Fore.YELLOW}Available commands:
        {Fore.CYAN}- {Fore.GREEN}start <bot_name>{Fore.WHITE} : Start a bot
        {Fore.CYAN}- {Fore.GREEN}stop <bot_name>{Fore.WHITE} : Stop a bot
        {Fore.CYAN}- {Fore.GREEN}restart <bot_name>{Fore.WHITE} : Restart a bot
        {Fore.CYAN}- {Fore.GREEN}list{Fore.WHITE} : List all bots
        {Fore.CYAN}- {Fore.GREEN}mem{Fore.WHITE} : Show memory usage
        {Fore.CYAN}- {Fore.GREEN}status{Fore.WHITE} : Show status of all bots
        {Fore.CYAN}- {Fore.GREEN}help{Fore.WHITE} : Show this help message"""

    def display_logo(self):
        ascii_logo = pyfiglet.figlet_format("Yujak Multi-Host", font="standard")
        ascii_subtext = pyfiglet.figlet_format("Made by Chris-tian123", font="small")

        print(Fore.LIGHTCYAN_EX + ascii_logo)
        print(Fore.CYAN + ascii_subtext)
