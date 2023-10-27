import os
from dotenv import load_dotenv
from bot.bot import Bot

TOKEN = os.getenv('BOT_TOKEN')

bot = Bot()


if __name__ == '__main__':

    load_dotenv()
    
    bot.run(TOKEN)