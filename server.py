import os
import util
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


@app.route("/surprise_song/set/<title>")
def set_surprise_song(title):
    f = open('surprise_song.txt', 'w')
    f.write(util.get_track_id(title))
    f.close()


if __name__ == "__main__":
    args = util.setup_args().parse_args()

    if args.phone:
        util.text_ip(args.phone)

    if args.public:
        app.run(host='0.0.0.0')
    else:
        app.run()
