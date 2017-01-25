import os
import util
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    scripts = os.listdir('./applescripts')
    html = ''
    for script in scripts:
        path = '/applescript/' + script
        html += "<a href=" + path + ">"+ script + "</a><br>"
    # return "Available Applescripts: " + str(os.listdir('./applescripts'))
    return "Available Applescripts:<br>" + html + "<br><br>Also you can set a search string or spotify track via:<br>/applescript/set_string/(string)<br>/applescript/set_song/(song)"


@app.route("/applescript/<some_script>")
def execute_applescript(some_script):
    filepath = "applescripts/" + some_script
    if os.path.isfile(filepath):
        os.system('osascript ' + filepath)
        return 'Executed ' + some_script + "<br><br><a href='/'>home</a>"
    else:
        return some_script + ' not found.<br><br><a href='/'>home</a>'


@app.route("/applescript/set_song/<title>")
def set_surprise_song(title):
    f = open('spotify_song.txt', 'w')
    f.write(util.get_track_id(title))
    f.close()
    return "Wrote '" + title + "' spotify track info to file.<br><br><a href='/'>home</a>"


@app.route("/applescript/set_string/<title>")
def set_search_string(title):
    f = open('search_string.txt', 'w')
    f.write(title)
    f.close()
    return "Wrote '" + title + "' to file.<br><br><a href='/'>home</a>"


if __name__ == "__main__":
    args = util.setup_args().parse_args()

    if args.phone:
        util.text_ip(args.phone)

    if args.public:
        app.run(host='0.0.0.0')
    else:
        app.run()
