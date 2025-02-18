from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

@app.route('/htop')
def htop():
    try:
        name = "Nikhil Koul"  # Replace with your full name
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
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
