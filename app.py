app.py
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Webhook aktif"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("DATA MASUK:", data)
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
