# app.py
from flask import Flask, jsonify, request, render_template
import json

app = Flask(__name__)

# In-memory database
database = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    transaction = request.json
    database.append(transaction)
    return jsonify({'status': 'Transaction added', 'data': transaction}), 201

@app.route('/get_transactions', methods=['GET'])
def get_transactions():
    return jsonify(database), 200

@app.route('/get_balance', methods=['GET'])
def get_balance():
    balance = sum([t['amount'] for t in database])
    return jsonify({'balance': balance}), 200

if __name__ == '__main__':
    app.run(debug=True)
