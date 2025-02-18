from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz
<<<<<<< HEAD
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

@app.route('/htop')
def htop():
    try:
        name = "Your Full Name"
        username = os.getenv('USER', 'unknown')  # Use os.getenv to avoid issues with os.getlogin()
        ist_time = datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S %Z%z')
        top_output = subprocess.getoutput('top -bn1')

        return f"""
        <html>
            <body>
                <h1>System Information</h1>
                <p><strong>Name:</strong> {name}</p>
                <p><strong>Username:</strong> {username}</p>
                <p><strong>Server Time (IST):</strong> {ist_time}</p>
                <pre>{top_output}</pre>
            </body>
        </html>
        """
    except Exception as e:
        app.logger.error(f"Error occurred: {e}")
        return "Internal Server Error", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
=======

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Your Full Name"
    username = os.getlogin()
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %Z%z')
    top_output = subprocess.getoutput('top -b -n 1')

    return f"""
    <html>
        <body>
            <h1>System Information</h1>
            <p><strong>Name:</strong> {name}</p>
            <p><strong>Username:</strong> {username}</p>
            <p><strong>Server Time (IST):</strong> {server_time}</p>
            <pre>{top_output}</pre>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
>>>>>>> a4eb654ff8af9963ff944511cc57196c06c736e4
