from flask import Flask, send_from_directory
import threading
import webview

app = Flask(__name__)

@app.route('/')
@app.route('/<path:filename>')
def serve(filename='index.html'):
    return send_from_directory('.', filename)

def start_flask():
    app.run(host='127.0.0.1', port=5000, debug=False, use_reloader=False)

threading.Thread(target=start_flask, daemon=True).start()

webview.create_window(
    title="ADX x OS",
    url="http://127.0.0.1:5000",
    width=1280,
    height=720,
    resizable=True,
    min_size=(800, 600),
    easy_drag=True,
    confirm_close=True
)
webview.start()
