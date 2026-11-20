# Little Lemon Restaurant API

Django + Django REST Framework capstone project for a restaurant website. It serves static HTML, exposes menu and table-booking APIs, supports account registration and authentication, and includes automated tests.

## Features
- Landing page at `/` served by Django.
- Menu API: `/api/menu/` and `/api/menu/<id>/`.
- Authenticated booking API: `/api/bookings/` and `/api/bookings/<id>/`.
- Djoser registration and token endpoints under `/auth/`.
- JWT support via Simple JWT at `/api/token/` and `/api/token/refresh/`.
- Django admin for menu and booking records.
- Unit tests.
- MySQL configured through environment variables; SQLite is the local default for quick setup.

## Setup in VS Code (Windows)
1. Install Python 3.10+ and optionally MySQL Server.
2. Extract the ZIP and open its folder in VS Code.
3. Create and activate a virtual environment:
   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```
4. Install packages:
   ```bash
   pip install -r requirements.txt
   ```
5. For MySQL, create the database in MySQL:
   ```sql
   CREATE DATABASE littlelemon CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
   ```
   Then set PowerShell variables (use your own MySQL password):
   ```powershell
   $env:MYSQL_DATABASE="littlelemon"
   $env:MYSQL_USER="root"
   $env:MYSQL_PASSWORD="your_mysql_password"
   $env:MYSQL_HOST="127.0.0.1"
   $env:MYSQL_PORT="3306"
   ```
   If you do not set `MYSQL_DATABASE`, the project uses SQLite for quick testing. If the rubric explicitly requires MySQL, use MySQL before submission.
6. Run:
   ```bash
   python manage.py makemigrations restaurant
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
   ```
7. Visit `http://127.0.0.1:8000/` and `http://127.0.0.1:8000/admin/`.

## Endpoints for peer reviewers
- `GET /api/menu/` — list menu items (public).
- `POST /api/menu/` — create a menu item (authentication required).
- `GET /api/menu/<id>/` — retrieve one menu item.
- `PUT/PATCH /api/menu/<id>/` — update a menu item (authentication required).
- `DELETE /api/menu/<id>/` — delete a menu item (authentication required).
- `GET/POST /api/bookings/` — list/create bookings (authentication required).
- `GET/PUT/PATCH/DELETE /api/bookings/<id>/` — manage one booking (authentication required).
- `POST /auth/users/` — register: `{"username":"reviewer1","password":"StrongPass123!","re_password":"StrongPass123!"}`.
- `POST /auth/token/login/` — get a DRF token with username/password JSON.
- `POST /api/token/` — get JWT access/refresh tokens.
- `POST /api/token/refresh/` — refresh JWT access token.

## Test with Insomnia
1. Start the Django server.
2. Register at `POST http://127.0.0.1:8000/auth/users/`.
3. Obtain a token at `POST http://127.0.0.1:8000/auth/token/login/` with JSON body `{"username":"reviewer1","password":"StrongPass123!"}`.
4. For protected requests add header `Authorization: Token YOUR_TOKEN_HERE`.
5. Test `GET /api/menu/`. Test booking creation using `POST /api/bookings/` with JSON:
   ```json
   {"name":"Alex","no_of_guests":2,"booking_date":"2030-05-20T19:00:00Z","comment":"Window seat if possible"}
   ```
6. A successful create should return `201`; a successful GET normally returns `200`. Verify records in `/admin/`.

## Run tests
```bash
python manage.py test
```

## Upload to GitHub
Create a repository named `little-lemon-django-capstone`, then run from this folder:
```bash
git init
git add .
git commit -m "Build Little Lemon Django REST API capstone"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/little-lemon-django-capstone.git
git push -u origin main
```
Replace `YOUR-USERNAME` and submit the URL of your actual repository, not the example URL.
