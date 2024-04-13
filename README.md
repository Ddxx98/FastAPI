# API Documentation

## FastAPI Endpoints

### Create Account

- **URL**: `/users`
- **Method**: POST
- **Request Body**: {
    "email":"deexith2016@gmail.com",
    "account_name": "Deekshith D V",
    "website": "www.google.com"
}
- **Response**: {"message": "Account created successfully","account_id": "661a16f4cc9f8139e0fe6543"}

### Update Account

- **URL**: `/users`
- **Method**: PUT
- **Request Body**: {
    "email":"deexith2016@gmail.com",
    "account_name": "Deekshith D V",
    "website": "www.google.com"
}
- **Response**: {"message": "Account updated successfully","account_id": "661a16f4cc9f8139e0fe6543"}

### Delete Account

- **URL**: `/users/{id}`
- **Method**: DELETE
- **Response**: {"message": "Account deleted successfully"}

### Get ID

- **URL**: `/users/{email}`
- **Method**: GET
- **Response**: {"id": "661a16f4cc9f8139e0fe6543"}

### Get SecreteCode

- **URL**: `/users/{id}`
- **Method**: GET
- **Response**: {"secretCode": "te78twgcuydsg78ewyduoshucej"}

### Create Destination

- **URL**: `/destination`
- **Method**: POST
- **Request Body**: {
    "account_id": "661a16f4cc9f8139e0fe6543",
    "destination": [
        {
            "url": "http://127.0.0.1:8000/destination",
            "http_method": "get",
            "headers": {
                "APP_ID": "1234APPID1234",
                "APP_SECTET": "ok",
                "ACTION": "add.destination",
                "Content-Type": "application/json",
                "Accept": "*"
            }
        }
    ]
}
- **Response**: {"message": "Destination created successfully", "destination_id": "661a16f4cc9f8139e0fe6543"}

### Add Destination

- **URL**: `/destination`
- **Method**: PUT
- **Request Body**: {
            "url": "http://127.0.0.1:8000/destination",
            "http_method": "get",
            "headers": {
                "APP_ID": "1234APPID1234",
                "APP_SECTET": "ok",
                "ACTION": "add.destination",
                "Content-Type": "application/json",
                "Accept": "*"
            }
        }
- **Response**: {"message": "Destination updated successfully"}

### Get Destination

- **URL**: `/destination/{id}`
- **Method**: GET
- **Response**: [
        {
            "url": "http://127.0.0.1:8000/destination",
            "http_method": "get",
            "headers": {
                "APP_ID": "1234APPID1234",
                "APP_SECTET": "ok",
                "ACTION": "add.destination",
                "Content-Type": "application/json",
                "Accept": "*"
            }
        }
    ]

### Call Webhook

- **URL**: `/server/incoming_data/`
- **Method**: POST
- **Request Body**: {
    "email":"deexith2016@gmail.com",
    "account_name": "Deekshith D V",
    "website": "www.google.com"
}
- **Response**: {"message": "Data sent to destinations successfully","response":responseData}