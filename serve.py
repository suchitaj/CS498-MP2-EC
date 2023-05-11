from flask import Flask, request
import stress_cpu
import socket
import subprocess

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def getSeed():
    if request.method == 'POST':
        subprocess.Popen(["python", "stress_cpu.py"])
        return socket.gethostname()
    else:
        return socket.gethostname()

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 80, debug = True)