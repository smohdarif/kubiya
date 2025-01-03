from flask import Flask, jsonify
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({
        "message": "Hello, Docker World!",
        "hostname": socket.gethostname()
    })

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "service": "Flask Demo App"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)