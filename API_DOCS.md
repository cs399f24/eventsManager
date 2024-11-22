# API Documentation

This section describes the endpoints available in the Events Manager API and how to interact with them.

## GET /api/events
- **Description**: Retrieve all current events from the database.
- **Method**: `GET`
- **URL**: `/api/events`
- **Response**: A JSON object containing all events, keyed by event ID. Each event includes `name`, `date`, and `location`.
- **Error Handling**: Returns a 500 status code with an error message if there is an issue retrieving the events.

## POST /api/add_event
- **Description**: Add a new event to the database and send an SNS notification.
- **Method**: `POST`
- **URL**: `/api/add_event`
- **Request Body**: Includes `name`, `date`, and `location`.
- **Response**: A 201 status code with a message confirming the event has been added.
- **Error Handling**: Returns a 400 status code with "Invalid event data" if any required fields are missing, or a 500 status code with an error message if there is an issue saving the event.

## DELETE /api/events/<event_id>
- **Description**: Delete an existing event by ID from the database and send an SNS notification.
- **Method**: `DELETE`
- **URL**: `/api/events/<event_id>`
- **Response**: A 200 status code with a message confirming the event has been deleted.
- **Error Handling**: Returns a 500 status code with an error message if there is an issue deleting the event.

## PUT /api/events/<event_id>
- **Description**: Update details of an existing event in the database and send an SNS notification.
- **Method**: `PUT`
- **URL**: `/api/events/<event_id>`
- **Request Body**: Updated `name`, `date`, and `location`.
- **Response**: A 200 status code with a message confirming the event has been updated.
- **Error Handling**: Returns a 400 status code with "Invalid event data" if any required fields are missing, or a 500 status code with an error message if there is an issue updating the event.

---

# Next Steps

Continue with the steps outlined to host the frontend and access your application via the S3 URL provided in Step 5. Ensure to configure your AWS SNS to handle notifications efficiently and securely.

