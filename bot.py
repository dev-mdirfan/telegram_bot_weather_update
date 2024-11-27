from dotenv import load_dotenv
import os
from flask import Flask
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests  # For weather API

# Load .env file
load_dotenv()

# Fetch environment variables
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

app = Flask(__name__)

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

# Initialize the updater
updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("subscribe", subscribe))
dp.add_handler(CommandHandler("weather", weather))

# Main function to run the bot
def run_bot():
    print("Starting bot...")
    updater.start_polling()
    updater.idle()

# Dummy route for Flask
@app.route("/")
def home():
    return "Bot is running!"

if __name__ == "__main__":
    # Start the bot in the same process
    print("Starting Telegram bot...")
    run_bot()

    # Start Flask app after the bot starts
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
