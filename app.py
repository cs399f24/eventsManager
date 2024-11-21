from flask import Flask, jsonify, request
from flask_cors import CORS
import boto3
from botocore.exceptions import ClientError
import uuid

app = Flask(__name__)
CORS(app)

# Initialize DynamoDB client
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')  # Specify your region
table = dynamodb.Table('EventsTable')  # Use your DynamoDB table name

# Initialize SNS client
sns_client = boto3.client('sns', region_name='us-east-1')

def send_sns_notification(subject, message):
    try:
        response = sns_client.publish(
            TopicArn='arn:aws:sns:us-east-1:134601196591:EventsManagerNotifications',
            Subject=subject,
            Message=message
        )
        print("SNS Notification Sent:", response)
    except Exception as e:
        print("Error Sending SNS Notification:", e)

@app.route("/api/events", methods=["GET"])
def get_events():
    try:
        response = table.scan()
        events = {item['event_id']: item for item in response['Items']}
        return jsonify(events)
    except ClientError as e:
        return {"error": str(e)}, 500

@app.route("/api/add_event", methods=["POST"])
def add_event():
    data = request.json
    if "name" in data and "date" in data and "location" in data:
        new_event_id = str(uuid.uuid4())
        try:
            table.put_item(
                Item={
                    'event_id': new_event_id,
                    'name': data["name"],
                    'date': data["date"],
                    'location': data["location"]
                }
            )
            send_sns_notification("New Event Added", f"Event {data['name']} added successfully.")
            return jsonify({"message": "Event added successfully"}), 201
        except ClientError as e:
            return {"error": str(e)}, 500
    else:
        return {"error": "Invalid event data"}, 400

@app.route("/api/events/<event_id>", methods=["DELETE"])
def delete_event(event_id):
    try:
        table.delete_item(Key={'event_id': event_id})
        send_sns_notification("Event Deleted", "An event was deleted successfully.")
        return jsonify({"message": "Event deleted successfully"}), 200
    except ClientError as e:
        return {"error": str(e)}, 500

@app.route("/api/events/<event_id>", methods=["PUT"])
def edit_event(event_id):
    data = request.json
    if "name" in data and "date" in data and "location" in data:
        try:
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
            send_sns_notification("Event Updated", f"Event {data['name']} updated successfully.")
            return jsonify({"message": "Event updated successfully"}), 200
        except ClientError as e:
            return {"error": str(e)}, 500
    else:
        return {"error": "Invalid event data"}, 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
