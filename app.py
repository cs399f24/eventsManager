from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# In-memory storage for events
events = {
    "event1": {"name": "Annual Meeting", "date": "2024-12-25", "location": "New York"},
    "event2": {"name": "Tech Conference", "date": "2024-11-15", "location": "San Francisco"}
}

@app.route("/api/events", methods=["GET"])
def get_events():
    return jsonify(events)

@app.route("/api/add_event", methods=["POST"])
def add_event():
    data = request.json
    if "name" in data and "date" in data and "location" in data:
        new_event_id = f"event{len(events) + 1}"
        events[new_event_id] = {"name": data["name"], "date": data["date"], "location": data["location"]}
        return jsonify(events), 201
    else:
        return {"error": "Invalid event data"}, 400

@app.route("/api/events/<event_id>", methods=["DELETE"])
def delete_event(event_id):
    if event_id in events:
        del events[event_id]
        return jsonify({"message": "Event deleted successfully"}), 200
    else:
	    return {"error": "Event not found"}, 404

@app.route("/api/events/<event_id>", methods=["PUT"])
def edit_event(event_id):
    data = request.json
    if event_id in events and "name" in data and "date" in data and "location" in data:
        events[event_id] = {"name": data["name"], "date": data["date"], "location": data["location"]}
        return jsonify({"message": "Event updated successfully", "event": events[event_id]}), 200
    else:
	    return {"error": "Invalid event data or event not found"}, 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)