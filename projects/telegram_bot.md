# 🤖 How to run a TELEGRAM BOT in Android

All this process is documented in the following [video - pending]()

![](/projects/images/telegram_bot/telegram_bot_running.png)

# 📚 Index

* 🏁 [First steps](#first-steps)
* ⚙️ [Get Bot TOKEN](#step1)
* 🤖 [Run the Telegram Bot](#step2)


<br>

---  
---  

<br>

## 🏁 First steps <a name=first-steps></a>

- **Download and install Termux app from the [official GitHub repository](https://github.com/termux/termux-app).**

- **Update and upgrade packages:** 
```
pkg update
pkg upgrade -y
```

Tip: You can select the mirror corresponding to the area closest to you with the command: 
```
termux-change-repo
```

- **Install Python (the language we are going to use for the bot)** 
```
pkg install python python-pip git
```

---  

<br>

## ⚙️ Get Bot TOKEN <a name=step1></a>

- Open your Telegram and start a conversation to the bot used in Telegram to manage your bots: https://t.me/BotFather or `@BotFather`

- Send the following message and follow the steps from the chat
```
/newbot
```
- Set a name for the bot: `AndroidTestingBot`
- Set a @ or username for the bot (needs to end in `bot`): `DroidMaster_testing_bot`

You will get your bot TOKEN (save it for later)

![](/projects/images/telegram_bot/bot_father_conversation.png)

---  

<br>

## 🤖 Run the Telegram Bot <a name=step2></a>


- **Download the Telegram Bot template** 
```
wget https://raw.githubusercontent.com/LinuxDroidMaster/Termux-Projects/main/projects/scripts/telegram_bot/telegram_bot.py
```

- **Replace the TOKEN in the `main` method with the one obtained in the previous step** 

```
# Replace this part (line 40): TOKEN_VALUE_FROM_BOTFATHER
```

- **Install dependencies**
```
pip install python-telegram-bot yt-dlp
```

- **Run the BOT**
```
python telegram_bot.py
```

- **Run the BOT in background**
```
python telegram_bot.py &
```

- **Check and kill background process**
```
ps aux | grep python # Get the PID
pkill PID
```