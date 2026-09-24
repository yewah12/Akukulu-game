from flask import Flask, jsonify, request
import random
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
def generate_crash_point():
    if random.random() < 0.03:
        return 1.00
    e = 2**32
    h = random.randint(0, e)
    crash_point = int((101 * e - h) / (101 * (e - h)) * 100) / 100
    return max(1.00, crash_point)
@app.route('/start-game', methods=['GET'])
def start_game():
    crash_point = generate_crash_point()
    return jsonify({
        "status": "success",
        "crash_point": crash_point
    })
@app.route('/telebirr-webhook', methods=['POST'])
def telebirr_webhook():
    data = request.json
    print(f"Payment received: {data}")
    return jsonify({"status": "Payment Received"})
if __name__ == '__main__':
    app.run(port=5000, debug=True)
