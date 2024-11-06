from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # resources={r"/api/*": {"origins": "*"}}) Allows all origins for testing; restrict for production

@app.route("/api/events")
def get_events():
    events = {
	"event1": {"name": "Annual Meeting", "date": "2024-12-25", "location": "New York"},
        "event2": {"name": "Tech Conference", "date": "2024-11-15", "location": "San Francisco"}
    }
    return jsonify(events)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
