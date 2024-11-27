from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Fetch environment variables
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

# Initialize Flask app
app = Flask(__name__)

# Simulate a database with Python dictionaries
settings = {
    "weather_api_key": WEATHER_API_KEY  # Placeholder for the weather API key
}

users = []  # List to store subscribed user chat IDs

# Endpoint to update bot settings
@app.route('/update_api_key', methods=['POST'])
def update_api_key():
    """
    Endpoint to update the weather API key.
    Request payload: { "api_key": "<new_api_key>" }
    """
    data = request.json  # Get JSON payload from the request
    new_api_key = data.get("api_key")

    if not new_api_key:
        return jsonify({"error": "API key is required!"}), 400

    # Update the settings
    settings["weather_api_key"] = new_api_key
    return jsonify({"message": "API key updated successfully!", "api_key": new_api_key})

# Endpoint to manage users
@app.route('/manage_users', methods=['POST'])
def manage_users():
    """
    Endpoint to manage user accounts.
    Request payload: { "action": "add|block|delete", "chat_id": <user_chat_id> }
    """
    data = request.json
    action = data.get("action")
    chat_id = data.get("chat_id")

    if not action or not chat_id:
        return jsonify({"error": "Action and chat_id are required!"}), 400

    if action == "add":
        if chat_id in users:
            return jsonify({"error": f"User {chat_id} is already subscribed!"}), 400
        users.append(chat_id)
        return jsonify({"message": f"User {chat_id} added successfully!", "users": users})

    elif action == "block":
        if chat_id not in users:
            return jsonify({"error": f"User {chat_id} not found!"}), 404
        users.remove(chat_id)
        return jsonify({"message": f"User {chat_id} blocked successfully!", "users": users})

    elif action == "delete":
        if chat_id in users:
            users.remove(chat_id)
        return jsonify({"message": f"User {chat_id} deleted successfully!", "users": users})

    else:
        return jsonify({"error": "Invalid action!"}), 400

# Endpoint to view current settings
@app.route('/view_settings', methods=['GET'])
def view_settings():
    """
    Endpoint to view current bot settings.
    """
    return jsonify({"settings": settings})

# Endpoint to view subscribed users
@app.route('/view_users', methods=['GET'])
def view_users():
    """
    Endpoint to view all subscribed users.
    """
    return jsonify({"users": users})

if __name__ == "__main__":
    # Run the app on localhost and port 5000
    app.run(host="0.0.0.0", port=5000, debug=os.getenv("FLASK_DEBUG"))
