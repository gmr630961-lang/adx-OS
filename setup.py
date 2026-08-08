run this in python 

from flask import Flask, send_from_directory
import os
import webbrowser
import threading

# ========================================
# ADX x OS - Pure Python Server
# ========================================

app = Flask(__name__)

# Serve the main HTML file
@app.route('/')
def serve_os():
    # Agar HTML file 'index.html' same folder mein hai
    return send_from_directory('.', 'index.html')

# Serve any other static files (CSS, JS, images)
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('.', filename)

def open_browser():
    """Opens the OS in the default browser after server starts."""
    webbrowser.open('https://adx-kappa.vercel.app/')

if __name__ == '__main__':
    print("🚀 Starting ADX x OS Server...")
    print("📂 Serving files from current directory.")
    print("🌐 Open at: http://127.0.0.1:5000")
    
    # Open browser automatically in a separate thread
    threading.Timer(1.0, open_browser).start()
    
    # Run Flask server
    app.run(host='127.0.0.1', port=5000, debug=False)
