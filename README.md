# Django Authentication API

## Project Overview
This project is a Django-based authentication system that implements **cookie-based authentication** with **CSRF protection**. It includes user registration, login, logout, and a protected user details endpoint. The API is documented using **Swagger**, which also ensures CSRF token generation.

## Features
- **User Registration API (`POST /api/register/`)**
  - Accepts email and password.
  - Sends a one-time password (OTP) to the email for verification.

- **User Registration Verification API (`POST /api/register/verify/`)**
  - Accepts email and OTP.
  - Verifies the OTP and completes registration.

- **User Login API (`POST /api/login/`)**
  - Accepts email and password.
  - Authenticates user and sets `auth_token` in **HTTP-only cookie**.
  - Requires CSRF token for security.

- **User Details API (`GET /api/me/`)**
  - Returns details of the authenticated user.
  - Accessible **only** if the user is logged in.

- **Logout API (`POST /api/logout/`)**
  - Clears `auth_token` from cookies.
  - Prevents further API access until login again.

- **Security Measures:**
  - **CSRF Protection**: CSRF token is required for all requests.
  - **Secure Cookies**: `HttpOnly` and `Secure` flags set to prevent XSS attacks.
  - **Swagger Integration**: Automatic CSRF token generation when accessing `/swagger/`.

---

## Installation & Setup

### 1. Clone the Repository
```sh
 git clone https://github.com/Netravati020/django_api_implementation.git
 cd <your-project-folder>
```

### 2. Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Apply Migrations
```sh
python manage.py migrate
```

### 5. Run the Development Server
```sh
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`.

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/register/` | Register a new user (sends OTP to email). |
| `POST` | `/api/register/verify/` | Verify OTP and complete registration. |
| `POST` | `/api/login/` | Login and get authentication token. |
| `GET` | `/api/me/` | Get details of the logged-in user. |
| `POST` | `/api/logout/` | Logout and clear authentication token. |
| `GET` | `/swagger/` | View API documentation. |

---

## Swagger Documentation
Swagger API documentation is available at:
```sh
http://127.0.0.1:8000/swagger/
```
Swagger automatically generates **CSRF tokens** when accessed.

---

## Security Considerations
- **CSRF Protection**: CSRF tokens are required for all requests.
- **Cookies Only Authentication**: No Authorization headers are used.
- **Secure Cookies**: Prevents JavaScript access to auth tokens.

---

## Deployment (Optional)
To deploy the project, configure **allowed hosts** and a production database in `settings.py`, then use:
```sh
python manage.py collectstatic
python manage.py runserver 0.0.0.0:8000
```

---




