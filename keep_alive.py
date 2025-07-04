from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def home():
    return "Discord Bot is Alive!"

def run():
    app.run(host='0.0.0.0', port=8080)  # Must use port 8080 for Render

def keep_alive():
    server = Thread(target=run, daemon=True)  # Run in a daemon thread
    server.start()
