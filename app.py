from flask import Flask, jsonify, request
from flask_cors import CORS
import boto3
from botocore.exceptions import ClientError
import uuid  # For generating unique IDs

app = Flask(__name__)
CORS(app)

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')  # Specify your region
table = dynamodb.Table('EventsTable')  # Use your DynamoDB table name

@app.route("/api/events", methods=["GET"])
def get_events():
    try:
        # Scan the DynamoDB table to get all events
        response = table.scan()
        events = {item['event_id']: item for item in response['Items']}
        return jsonify(events)
    except ClientError as e:
        return {"error": str(e)}, 500

@app.route("/api/add_event", methods=["POST"])
def add_event():
    data = request.json
    if "name" in data and "date" in data and "location" in data:
        # Generate a unique event_id using UUID
        new_event_id = str(uuid.uuid4())
        try:
            # Add the event to DynamoDB
            table.put_item(
                Item={
                    'event_id': new_event_id,
                    'name': data["name"],
                    'date': data["date"],
                    'location': data["location"]
                }
            )
            return jsonify({"message": "Event added successfully"}), 201
        except ClientError as e:
            return {"error": str(e)}, 500
    else:
        return {"error": "Invalid event data"}, 400

@app.route("/api/events/<event_id>", methods=["DELETE"])
def delete_event(event_id):
    try:
        # Delete the event from DynamoDB
        table.delete_item(Key={'event_id': event_id})
        return jsonify({"message": "Event deleted successfully"}), 200
    except ClientError as e:
        return {"error": str(e)}, 500

@app.route("/api/events/<event_id>", methods=["PUT"])
def edit_event(event_id):
    data = request.json
    if "name" in data and "date" in data and "location" in data:
        try:
            # Update the event in DynamoDB
            table.update_item(
                Key={'event_id': event_id},
                UpdateExpression="SET #n = :name, #d = :date, #l = :location",
                ExpressionAttributeNames={'#n': 'name', '#d': 'date', '#l': 'location'},
                ExpressionAttributeValues={
                    ':name': data["name"],
                    ':date': data["date"],
                    ':location': data["location"]
                }
            )
            return jsonify({"message": "Event updated successfully"}), 200
        except ClientError as e:
            return {"error": str(e)}, 500
    else:
        return {"error": "Invalid event data"}, 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
