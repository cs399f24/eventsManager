#!/bin/bash

# Find the process running app.py and terminate it
FLASK_PID=$(ps aux | grep 'python3 app.py' | grep -v 'grep' | awk '{print $2}')

if [ -n "$FLASK_PID" ]; then
    echo "Stopping Flask app with PID: $FLASK_PID"
    kill $FLASK_PID
    echo "Flask app stopped."
else
    echo "Flask app is not running."
fi

