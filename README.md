# Django Classifieds App

A starter classifieds/listing web app built with Django and SQLite.

## Features

- User account registration and login/logout.
- Create and browse listings.
- Upload listing images.
- User-to-user chat threads.

## Tech stack

- Django
- SQLite
- Pillow (image handling)

## Run locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
3. Create an admin user (optional):
   ```bash
   python manage.py createsuperuser
   ```
4. Start server:
   ```bash
   python manage.py runserver
   ```

Open http://127.0.0.1:8000/.
