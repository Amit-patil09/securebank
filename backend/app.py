from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import os

app = Flask(__name__)
CORS(app)


# Connect to MySQL
db = mysql.connector.connect(
    host=os.environ["DB_HOST"],
    port=int(os.environ["DB_PORT"]),
    user=os.environ["DB_USER"],
    password=os.environ["DB_PASSWORD"],
    database=os.environ["DB_NAME"],
    ssl_disabled=False,
    autocommit=True
)

print("Connected to MySQL!")


@app.route("/")
def home():
    return "Bank backend is connected to MySQL!"


@app.route("/login", methods=["POST"])
def login():

    data = request.json

    username = data.get("username")
    password = data.get("password")

    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM users WHERE username = %s",
        (username,)
    )

    user = cursor.fetchone()
    
    

    cursor.close()

    if user and user["password_hash"] == password:

        return jsonify({
            "success": True,
            "message": "Login successful",
            "username": user["username"],
            "balance": float(user["balance"])
        })

    return jsonify({
        "success": False,
        "message": "Invalid username or password"
    })

if __name__ == "__main__":
    app.run(port=5000, debug=True)

