from flask import Flask, jsonify, request
import random
from flask_cors import CORS
app = Flask(__name__)
# ማንኛውም ድህረ-ገጽ (GitHub) ይህንን ሰርቨር በቀጥታ እንዲያገኘው መፍቀድ
CORS(app, resources={r"/*": {"origins": "*"}})

def generate_crash_point():
    if random.random() < 0.03:
        return 1.00
    e = 2**32
    h = random.randint(0, e)
    crash_point = int((101 * e - h) / (101 * (e - h)) * 100) / 100
    return max(1.00, crash_point)
@app.route('/start-game', methods=['GET'])
def start_game():
    response = jsonify({"status": "success", "crash_point": generate_crash_point()})
    return response
@app.route('/telebirr-webhook', methods=['POST'])
def telebirr_webhook():
    return jsonify({"status": "Payment Received"})
if __name__ == '__main__':
    app.run(port=5000, debug=True)
