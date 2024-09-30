# TripBuddy

![Project Banner](./assets/tripbuddy-banner.png)

Tripbuddy is a responsive web application built with Python Django, showcasing various travel packages including tours, treks, resorts, events, diving, and skiing experiences. Users can explore package details and make bookings, while the platform also offers API functionality for authorized users.

## 🌟 Features

- 🏞️ Browse demo packages for tours, treks, resorts, events, diving, and skiing
- 🔍 Detailed information for each package
- 📅 User-friendly booking system
- 🔐 User authentication (username/password and Google Sign-In)
- 👑 Admin and superuser roles with extended privileges
- 🚀 RESTful API for CRUD operations on travel packages

## 🛠️ Technologies Used

- Python
- Django
- SQLite3 (based on MySQL)
- Django REST Framework
- Google OAuth

## 📚 Usage

### User Features

- Sign up or sign in using username/password or Google account
- Browse available travel packages
- View detailed information about each package
- Book desired packages

### Admin Features

- Access admin panel at `/admin`
- Manage packages, and bookings

### API Endpoints

- `/tripsapi/` - API root
  - GET: Retrieve all packages (authorized and unauthorized users)
  - POST: Create new package (authorized users only)
- `/tripsapi/<id>/`
  - GET: Retrieve specific package (all users)
  - PUT/PATCH: Update package (authorized users)
  - DELETE: Remove package (authorized users)

## 🔐 Authentication

- Local authentication using username and password
- Google Sign-In integration

## 👥 User Roles

1. Regular User: Can view and book packages
2. Admin User: Additional privileges for managing content
3. Superuser: Full access to Django admin panel

Live Link: [https://chetan3010.pythonanywhere.com](https://chetan3010.pythonanywhere.com)