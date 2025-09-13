# SchoolCore Django API

A Django REST API project for managing users, courses, and students in a school system. This project uses Django REST Framework with JWT authentication.

## Features

- User authentication with JWT tokens
- User profile management
- Course management
- Student management
- Admin interface

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/AlirezaNourahmadi/training.git
   cd training
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```
   python manage.py migrate
   ```

5. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

## API Endpoints

### Authentication

- `POST /api/token/`: Obtain JWT token pair (access and refresh)
- `POST /api/token/refresh/`: Refresh access token

### Users

- `GET /api/users/profile/`: Get authenticated user's profile (requires authentication)

### Admin

- Access the Django admin at `/admin/` using superuser credentials

## Usage

1. Obtain a JWT token by sending a POST request to `/api/token/` with your username and password:
   ```
   {
     "username": "your_username",
     "password": "your_password"
   }
   ```

2. Use the access token in the Authorization header for authenticated requests:
   ```
   Authorization: Bearer <access_token>
   ```

3. Access the user profile at `/api/users/profile/`

## Project Structure

- `schoolcore/`: Main Django project settings
- `users/`: User management app
- `courses/`: Course management app
- `students/`: Student management app

## Technologies Used

- Django 5.1
- Django REST Framework
- Simple JWT for authentication
- SQLite database (for development)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test your changes
5. Submit a pull request

## License

This project is licensed under the MIT License.
