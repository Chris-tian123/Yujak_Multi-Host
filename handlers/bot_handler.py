import os
import subprocess

class BotHandler:
    def __init__(self, bot_name):
        self.bot_name = bot_name
        self.bot_path = os.path.join("bots", bot_name)
        self.process = None

    def get_script_path(self):
        for script in ["main.py", "bot.py"]:
            script_path = os.path.join(self.bot_path, script)
            if os.path.exists(script_path):
                return script_path
        return None

    def start(self):
        script_path = self.get_script_path()
        if not script_path:
            return f"Bot script not found in {self.bot_path}."

        if self.process and self.process.poll() is None:
            return f"{self.bot_name} is already running."

        self.process = subprocess.Popen(["python", script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return f"Starting {self.bot_name}..."

    def stop(self):
        if self.process and self.process.poll() is None:
            self.process.terminate()
            self.process = None
            return f"{self.bot_name} stopped."
        return f"{self.bot_name} is not running."

    def status(self):
        if self.process and self.process.poll() is None:
            return "Running"
        return "Stopped"
