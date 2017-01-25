# httplescripts
Flask server which runs local applescripts in response to HTTP requests

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

### Current Applescripts
- Set volume level to 0
- Cycle through volume level
- Google an arbitrary string
- Play an arbitrary song on Spotify

### Non-Applescript Functionality
- Set search string to google
- Set spotify track to play

