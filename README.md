Here’s a detailed and professional **README.md** for your Telegram bot and admin panel repository. You can customize it further to suit your preferences.

---

# **Telegram Weather Bot with Admin Panel**

A Telegram bot that provides weather updates to users and an admin panel to manage bot settings and user subscriptions.

## **Features**
- 🌤️ **Weather Updates**: Users can subscribe to receive weather updates for their preferred city.
- 🔧 **Admin Panel**: Manage bot settings and user subscriptions via a Flask-powered admin panel.
- 🔒 **Secure**: Uses `.env` file for managing sensitive data like API keys.
- 📡 **Real-Time Updates**: Fetches live weather data using the OpenWeatherMap API.

---

## **Tech Stack**
- **Telegram Bot API**: Bot interaction with users.
- **OpenWeatherMap API**: Fetching real-time weather data.
- **Node.js/Python**: Bot backend (Python for this implementation).
- **Flask**: Lightweight admin panel for bot management.
- **dotenv**: Securely manage environment variables.

---

## **Getting Started**

### **Prerequisites**
Ensure you have the following installed:
- Python 3.9 or later
- pip (Python package installer)
- Telegram account (to create a bot via BotFather)
- OpenWeatherMap account (to obtain an API key)

### **Setup Instructions**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/dev-mdirfan/telegram_bot_weather_update.git
   cd telegram_bot_weather_update
   ```

2. **Create a `.env` File**:
   In the project root, create a `.env` file with the following contents:
   ```env
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token
   WEATHER_API_KEY=your_weather_api_key
   FLASK_ENV=development
   FLASK_DEBUG=1
   ```

3. **Install Dependencies**:
   Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Bot**:
   Start the Telegram bot:
   ```bash
   python bot.py
   ```

5. **Run the Admin Panel**:
   Start the admin panel:
   ```bash
   python admin_panel.py
   ```
   Access the admin panel at `http://localhost:5000`.

---

## **Usage**

### **For Users**
1. Start the bot by searching for its handle on Telegram.
2. Use `/start` to initiate the bot.
3. Use `/weather <city>` to get the current weather for a city.
4. Use `/subscribe` to receive daily weather updates.

### **For Admins**
1. **Manage Users**: Add, block, or delete users via the admin panel.
2. **Update API Key**: Change the weather API key dynamically.
3. **View Settings and Users**: Monitor current settings and subscribed users.

---

## **API Endpoints**

### **Admin Panel Endpoints**
1. **Update API Key**:  
   **POST** `/update_api_key`  
   **Body**:  
   ```json
   {
       "api_key": "new_api_key"
   }
   ```

2. **Manage Users**:  
   **POST** `/manage_users`  
   **Body**:  
   ```json
   {
       "action": "add|block|delete",
       "chat_id": 12345678
   }
   ```

3. **View Settings**:  
   **GET** `/view_settings`

4. **View Users**:  
   **GET** `/view_users`

---

## **Project Structure**
```
repository-name/
│
├── bot.py                # Telegram bot script
├── admin_panel.py        # Flask admin panel script
├── requirements.txt      # Dependencies
├── .env                  # Environment variables (not pushed to GitHub)
└── README.md             # Documentation
```

---

## **Contributing**
Contributions are welcome! Feel free to:
- Fork the repository.
- Create a branch.
- Submit a pull request with your improvements.

---

## **License**
This project is licensed under the [MIT License](LICENSE).

---

Let me know if you want additional sections or adjustments! 🚀