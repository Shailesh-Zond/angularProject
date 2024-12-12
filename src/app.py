from flask import Flask, request, jsonify
import sqlite3
from werkzeug.security import generate_password_hash

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('user_register.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/register', methods=['POST'])
def register():
    # Get data from the request
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    contact = data.get('contact')
    password = data.get('password')
    repassword = data.get('repassword')

    if password != repassword:
        return jsonify({"error": "Passwords do not match"}), 400

    hashed_password = generate_password_hash(password)

    # Insert into the database
    conn = get_db_connection()
    conn.execute('INSERT INTO users (username, email, contact, password) VALUES (?, ?, ?, ?)',
                 (username, email, contact, hashed_password))
    conn.commit()
    conn.close()

    return jsonify({"message": "User registered successfully!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
