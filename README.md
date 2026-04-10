# Django Classifieds App

A classifieds/listing web app built with Django and SQLite.

## Features

- User account registration and login/logout.
- Create and browse listings.
- Upload listing images.
- User-to-user chat threads.

## Requirements

- Python 3.10+ (3.11 recommended)
- `pip`

## Quick start (local machine)

1. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

3. Run migrations:
   ```bash
   python manage.py migrate
   ```

4. Create an admin user (optional):
   ```bash
   python manage.py createsuperuser
   ```

5. Start the app:
   ```bash
   python manage.py runserver
   ```

6. Open: http://127.0.0.1:8000/

## Default app routes

- `/` — listings homepage
- `/listing/new/` — create listing (login required)
- `/accounts/register/` — user registration
- `/accounts/login/` — login
- `/chat/` — chat inbox (login required)
- `/admin/` — Django admin

## Troubleshooting

### `ModuleNotFoundError: No module named 'django'`
You are likely outside your virtual environment or dependencies were not installed.

### Image upload errors
Make sure Pillow installed successfully and forms use `enctype="multipart/form-data"` (already configured in templates).

### Database reset
If you want to start fresh:
```bash
rm -f db.sqlite3
python manage.py migrate
```
