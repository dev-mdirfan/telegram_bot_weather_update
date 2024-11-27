from dotenv import load_dotenv
import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

import requests  # For weather API

# Load .env file
load_dotenv()

# Replace with your weather API key
# https://home.openweathermap.org/api_keys
# Fetch environment variables
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

# Start command
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Welcome! Use /subscribe to get daily weather updates. \n To get the weather details use /weather Delhi etc.")

# Subscribe command
def subscribe(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    # Save the chat_id to a database (for now, just print it)
    print(f"User subscribed: {chat_id}")
    update.message.reply_text("You have subscribed for weather updates!")

# Weather command
def weather(update: Update, context: CallbackContext):
    city = " ".join(context.args) or "London"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url).json()
    if response.get("main"):
        temp = response["main"]["temp"]
        desc = response["weather"][0]["description"]
        update.message.reply_text(f"Weather in {city}:\nTemp: {temp}°C\nDescription: {desc}")
    else:
        update.message.reply_text("City not found!")

# Main function
def main():
    updater = Updater(TELEGRAM_BOT_TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("subscribe", subscribe))
    dp.add_handler(CommandHandler("weather", weather))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
