import socket
import os
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/applescript/<some_script>")
def execute_applescript(some_script):
    filepath = "applescripts/" + some_script
    if os.path.isfile(filepath):
        os.system('osascript ' + filepath)
        return 'executing ' + some_script
    else:
        return some_script + ' not found'


@app.route("/ip")
def get_ip():
    return socket.gethostbyname(socket.gethostname())


if __name__ == "__main__":
    app.run()
