## API Documentation

This section describes the endpoints available in the Events Manager API and how to interact with them.

### GET /api/events
- **Description**: Retrieve all current events.
- **Method**: `GET`
- **URL**: `/api/events`
- **Response**: A JSON object containing all events keyed by event ID.

### POST /api/add_event
- **Description**: Add a new event.
- **Method**: `POST`
- **Request Body**: Includes `name`, `date`, and `location`.
- **Response**: Returns the updated list of events.

### DELETE /api/events/<event_id>
- **Description**: Delete an existing event by ID.
- **Method**: `DELETE`
- **Response**: Confirmation message on successful deletion.

### PUT /api/events/<event_id>
- **Description**: Update an existing event.
- **Method**: `PUT`
- **Request Body**: Updated `name`, `date`, and `location`.
- **Response**: Confirmation message and details of the updated event.

For complete details on each endpoint, including expected parameters and response structures, refer to the full API endpoint documentation.

---

### Next Steps

Continue with the steps outlined to host the frontend and access your application via the S3 URL provided in Step 5.
