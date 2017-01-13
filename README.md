# pie-troll
<https://twitter.com/internetofshit>

### Usage:
- run `python server.py [OPTION]`
- `--phone` option will send the public ip address of the server to the specified phone number
- `--public` option will make the server public, and accessible to all devices on the network

### Features:
- Extremely quick to set up and run
- Easily add functionality by dropping new applescripts in the applescripts directory
- Remotely control a computer through HTTP requests

### What it does:
- Sets up a Flask app to recieve HTTP requests
- Dynamically creates URLs for each applescript
- Runs individual applescripts in response to the HTTP requests

### To-Dos
- Create front-end interface
- Make set Spotify song work
- Make set Chrome search string work

### Current Applescripts
- Set volume level to 0
- Cycle through volume level
- Google a string
- Play a song on Spotify

#### Front End Notes

react

<https://realpython.com/blog/python/the-ultimate-flask-front-end/>

<http://aviadas.com/blog/2015/08/05/evaluating-react-dot-js-and-flask/>

https://github.com/nickjj/flask-webpack

https://github.com/callemall/material-ui
