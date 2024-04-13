# API Documentation

## FastAPI Endpoints

### Create Account

- **URL**: `/users`
- **Method**: POST
- **Request Body**: email=user@example.com&account_name=Example+Account&website=https://example.com
- **Response**: Account created successfully


### Create Destination

- **URL**: `/create_destination/{account_id}/`
- **Method**: POST
- **Request Body**: url=https://destination.com&http_method=POST&headers=Content-Type%3A+application%2Fjson%0D%0AAccept%3A+%2A
- **Response**: Destination created successfully