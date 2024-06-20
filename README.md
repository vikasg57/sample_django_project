## Contains:
- Project Starting Guide
- API Documentation

## About Project:
Mini back-end system for library management written in Python.

## Frameworks Used 🌟
- Python
- Django
- Django Rest Framework
- Django Rest Framework SimpleJWT

## Steps to Follow for Running Backend Server:
### step 1: Clone the github repository
Clone the github repository for running the project locally.
```
git clone https://github.com/vikasg57/sample_django_project.git
```
### Step 2: Set Execution Permissions for the Entrypoint File

##### On Unix-based Systems (Linux/MacOS):

To give execution permissions to the `entrypoint.sh` file in your app directory, run the following command:

```bash
chmod +x social_networking/entrypoint.sh
```

##### On Windows:

If you're using Windows, you may also need to convert the file format to Unix format. You can do this using the dos2unix utility. Run the following commands:

###### Install dos2unix (if not already installed):

```bash
sudo apt-get install dos2unix
```

###### Convert the file format:

```bash
dos2unix social_networking/entrypoint.sh
```
###### Set execution permissions:

```bash
chmod +x social_networking/entrypoint.sh
```

### Step 3: Build and Run the Docker Containers

Run the following commands to build and start the Docker containers for the Django application:

```bash
docker-compose up -d --build
```

### Step 4: Apply Database Migrations

Execute the database migrations using Django's manage.py script:

```bash
docker-compose exec web python manage.py migrate --noinput
```

## Django Social Network API Documentation

### Overview
This document provides details on the REST API endpoints available in the Django Social Network project. The API allows interaction with app.

### Base URL
http://localhost:8000

### Endpoints

### 1. Users

#### Register User
- **URL:** `/users/signup/`
- **Method:** POST
- **Description:** Register a new user.
- **Request Body:**
  ```json
  {
    "first_name": "vikas",
    "last_name": "gaikwad",
    "email": "vgaikwad299@gmail.com",
    "password":"vikas"
    }
    ```

Response:
HTTP 200 Created
```json
{
    "success": true,
    "data": {
        "first_name": "vikas",
        "last_name": "gaikwad",
        "mobile": "08381035267",
        "email": "vikas@inkle.io",
        "uuid": "cb020f94-7961-4ce9-aba9-88bc367211de",
        "refresh": [
            "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxOTQxNjAwMSwiaWF0IjoxNzE4ODExMjAxLCJqdGkiOiIzNWNlOWI4M2Y3NzU0MTg2YWNiOWE2MWRhZDAzMDk1NiIsInVzZXJfaWQiOjF9.l03K82cHq4Dugif77WD0kfOTN54jNGLUYh_WwaWQ0nQ"
        ],
        "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE5NDE2MDAxLCJpYXQiOjE3MTg4MTEyMDEsImp0aSI6ImZlYWM4MDczZjYyMTQwMDRiOWMyOWJmODY2NDIzODI4IiwidXNlcl9pZCI6MX0.LrLR4AJWQFgpW06Q8CZsS5YDbosY7muLtQL-gdukDow"
    }
}
```
If user already present
Response: HTTP 400
```json
{
    "success": false,
    "error": {
        "code": "user_already_exists",
        "message": "User Already exists! login instead."
    }
}
```
If Email Invalid format
Response: HTTP 400
```json
{
    "success": false,
    "error": {
        "code": "validation_failed",
        "message": "Enter a valid email address."
    }
}
```

#### Login User
- **URL:** `/users/login/`
- **Method:** POST
- **Description:** Login a new user.
- **Request Body:**
  ```json
  {
    "email": "vgaikwad299@gmail.com",
    "password":"vikas"
    }
    ```

Response:
HTTP 200 Created
```json
{
    "success": true,
    "data": {
        "first_name": "vikas",
        "last_name": "gaikwad",
        "mobile": "08381035267",
        "email": "vikas@inkle.io",
        "uuid": "cb020f94-7961-4ce9-aba9-88bc367211de",
        "refresh": [
            "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxOTQxNjAwMSwiaWF0IjoxNzE4ODExMjAxLCJqdGkiOiIzNWNlOWI4M2Y3NzU0MTg2YWNiOWE2MWRhZDAzMDk1NiIsInVzZXJfaWQiOjF9.l03K82cHq4Dugif77WD0kfOTN54jNGLUYh_WwaWQ0nQ"
        ],
        "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE5NDE2MDAxLCJpYXQiOjE3MTg4MTEyMDEsImp0aSI6ImZlYWM4MDczZjYyMTQwMDRiOWMyOWJmODY2NDIzODI4IiwidXNlcl9pZCI6MX0.LrLR4AJWQFgpW06Q8CZsS5YDbosY7muLtQL-gdukDow"
    }
}
```
If user not found
Response: HTTP 400
```json
{
    "success": false,
    "error": {
        "code": "user_not_exists",
        "message": "User not exists! signup instead."
    }
}
```
If email in invalid format
Response: HTTP 400
```json
{
    "success": false,
    "error": {
        "code": "validation_failed",
        "message": "Enter a valid email address."
    }
}
```
If wrong password
Response: HTTP 400
```json
{
    "success": false,
    "error": {
        "code": "validation_failed",
        "message": "Incorrect Password"
    }
}
```
### 2. Social Networking

API authentication is handled using JWT (JSON Web Tokens). You need to include the JWT token in the `Authorization` header of each request.

#### Get all Users
- **URL:** `/users/get_all/`
- **Method:** GET
- **Description:** Get all users of platform
- **Parameters:**
  - **search_term** (optional, string): Search term to filter users by.
  - **page_num** (optional, integer): Page number for pagination, defaults to 1 if not provided.

Response:HTTP 200

```json
{
    "success": true,
    "data": {
        "profiles": [
            {
                "first_name": "vikas",
                "last_name": "gaikwad",
                "mobile": null,
                "email": "vgaikwad299@gmail.com",
                "uuid": "6c61c031-df43-4c57-b8fd-fbf2f24bf548"
            },
            {
                "first_name": "vikas",
                "last_name": "gaikwad",
                "mobile": "08381035267",
                "email": "vikas@inkle.io",
                "uuid": "cb020f94-7961-4ce9-aba9-88bc367211de"
            }
        ],
        "total_pages": 1,
        "current_page": 1
    }
}
```

#### Get all Friends for a logged in User
- **URL:** `/users/get/friends/`
- **Method:** GET
- **Description:** Get friends of a logged in user.
- **Parameters:**
  - **search_term** (optional, string): Search term to filter users by.
  - **page_num** (optional, integer): Page number for pagination, defaults to 1 if not provided.

Response:HTTP 200

```json
{
    "success": true,
    "data": {
        "friends": [
            {
                "first_name": "vikas",
                "last_name": "gaikwad",
                "mobile": "08381035267",
                "email": "vikas@inkle.io",
                "uuid": "cb020f94-7961-4ce9-aba9-88bc367211de",
                "is_close_friend": false,
                "followed_date": "2024-06-19T02:57:20.540191Z"
            }
        ],
        "total_pages": 1,
        "current_page": 1
    }
}
```

#### Get all pending friend requests for logged in User
- **URL:** `/users/get/pending_requests/`
- **Method:** GET
- **Description:** Get Pending requests for logged in user (received requests).
- **Parameters:**
  - **page_num** (optional, integer): Page number for pagination, defaults to 1 if not provided.

Response:HTTP 200

```json
{
    "success": true,
    "data": {
        "pending_requests": [
            {
                "first_name": "vikas",
                "last_name": "gaikwad",
                "mobile": null,
                "email": "vgaikwad299@gmail.com",
                "uuid": "6c61c031-df43-4c57-b8fd-fbf2f24bf548",
                "request_id": "07b36dd9-e395-477b-a422-baff37ec7d2e",
                "status": "PENDING"
            }
        ],
        "total_pages": 1,
        "current_page": 1
    }
}
```

#### Send a Friend Request

- **URL:** `/users/send_request/`
- **Method:** POST
- **Description:** Send request to provided profile uuid.
- **Request Body:**
  ```json
  {
    "to_profile_id": "6c61c031-df43-4c57-b8fd-fbf2f24bf548"
  }
  ```
  
Response:HTTP 200
```json
{
    "success": true,
    "data": {
        "first_name": "divya",
        "last_name": "shelke",
        "mobile": null,
        "email": "divya@gmail.com",
        "uuid": "8dd65a04-9d0d-4b4e-b562-ab66dbe59412",
        "request_id": "b957cc29-d34f-4b4a-af75-d633edd09017",
        "status": "PENDING"
    }
}
```
If request already accepted
Response:HTTP 400
```json
{
    "success": false,
    "error": {
        "code": "request_already_exists",
        "message": "Friend request already sent."
    }
}
```

If request already rejected
Response:HTTP 400

```json
{
    "success": false,
    "error": {
        "code": "request_already_rejected",
        "message": "Friend Request already Rejected"
    }
}
```

#### Perform Action on Request

- **URL:** `/users/request/:request_id/action/`
- **Method:** POST
- **Description:** Perform an action on a specific request identified by `request_id`.
- **URL Parameters:**
  - **request_id** (string): Identifier of the request to perform action on.
- **Request Body:**
  ```json
  {
    "action": "ACCEPTED"
  }
  ```
  
Response:HTTP 200
```json
{
    "success": true,
    "data": {
        "first_name": "divya",
        "last_name": "shelke",
        "mobile": null,
        "email": "divya@gmail.com",
        "uuid": "8dd65a04-9d0d-4b4e-b562-ab66dbe59412",
        "request_id": "b957cc29-d34f-4b4a-af75-d633edd09017",
        "status": "ACCEPTED"
    }
}
```
If user do not have permission
Response:HTTP 403
```json
{
    "success": false,
    "error": {
        "code": "permission_denied",
        "message": "You Do Not Have Permission To Perform This Action."
    }
}
```

### Thank you for exploring our API documentation!
