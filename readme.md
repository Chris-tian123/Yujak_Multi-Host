# Yujak Multi-Host

Welcome to **Yujak Multi-Host**, a powerful and easy-to-use multi-bot hosting system for managing and running multiple bots efficiently. Built with Python, this system allows you to start, stop, restart, and monitor bots from a single console interface.

![Image](https://media.discordapp.net/attachments/1239329065404469298/1337898084344004741/image.png?ex=67a91e30&is=67a7ccb0&hm=13411732ad6b115551fa72022526163f057caeccb4aa08d856b3c45fab654a1e&=&format=webp&quality=lossless)

## Features

- Start, stop, and restart bots easily
- Monitor memory usage
- View the status of all bots
- Colorful and interactive console
- ASCII art for a cool interface

## Requirements

Ensure you have the following installed:

- Python 3.x
- Required dependencies (install using the command below)

```sh
pip install -r requirements.txt
```

## How to Use

### 1. Setting Up

Place your bots inside the `bots/` directory. Each bot should be in its own folder, with a `bot.py` file inside it. IMPORTANT: If the file is not named `bot.py` , the script won't run the code

Example structure:

```
/bots
  /bot1
     bot.py
  /bot2
     bot.py
```

### 2. Dependencies

Before running Yujak Multi-Host, you must write your bot's dependencies in requirements.txt found in /root! 
**Important: Do NOT remove the folowing dependencies:**

```txt
colorama
pyfiglet
```

### 3. Running Yujak Multi-Host

To start the hosting system, run:

```sh
python host.py
```

### 4. Available Commands

| Command         | Description                  |
| --------------- | ---------------------------- |
| `start <bot>`   | Starts the specified bot     |
| `stop <bot>`    | Stops the specified bot      |
| `restart <bot>` | Restarts the specified bot   |
| `list`          | Lists all available bots     |
| `status`        | Shows the status of all bots |
| `mem`           | Displays memory usage        |
| `help`          | Shows available commands     |

### 5. Running a Bot

Each bot must have a Python script that starts it. The system will look for `bot.py` inside each bot folder.

Example of `bot.py` inside a bot folder:

```python
import time

def run():
    while True:
        print("Bot is running...")
        time.sleep(10)

if __name__ == "__main__":
    run()
```

## Credits

Made by **Chris-tian123**

Enjoy using Yujak Multi-Host! 🚀

## Contact

If you want to collab, contact me on [telegram](https://t.me/Asteral), [discord](https://discord.com/users/915158686723358720) or [email](mailto:asteral.dev@outlook.com)