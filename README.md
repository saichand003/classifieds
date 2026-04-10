# Django Classifieds App

A classifieds/listing web app built with Django and SQLite.

## Features

- User account registration and login/logout.
- Create and browse listings.
- Upload listing images.
- User-to-user chat threads.

## Requirements

- Python 3.10+ (3.11+ recommended)
- `pip` (invoked via `python -m pip`)

## Quick start (local machine)

1. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
   ```

3. Run migrations (required before first page load):
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

## One-command boot (Linux/macOS)

```bash
./run_local.sh
```

This script auto-detects `python3` (or `python`), creates `.venv`, installs dependencies, runs migrations, and starts the server.

## Homebrew macOS notes

If you see `zsh: command not found: pip`, use Python's module form instead of `pip` directly:

```bash
python3 -m pip --version
python3 -m pip install -r requirements.txt
```

If `python3` itself is not on your `PATH`, add Homebrew Python `libexec/bin` symlinks to your shell config:

```bash
echo 'export PATH="/opt/homebrew/opt/python@3.14/libexec/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
python3 --version
```

`pipx` is not a replacement for `pip install -r requirements.txt`; `pipx` installs standalone CLI apps, not project dependencies.

## Default app routes

- `/` — listings homepage
- `/listing/new/` — create listing (login required)
- `/accounts/register/` — user registration
- `/accounts/login/` — login
- `/chat/` — chat inbox (login required)
- `/admin/` — Django admin

## Troubleshooting

### `ModuleNotFoundError: No module named 'django'`
You're likely outside your virtual environment or dependencies were not installed in the venv.

### Image upload errors
Make sure Pillow installed successfully and forms use `enctype="multipart/form-data"` (already configured in templates).

### Database reset
If you want to start fresh:
```bash
rm -f db.sqlite3
python manage.py migrate
```


### `OperationalError: no such table: listings_listing`
Your database schema is not initialized yet. Run:
```bash
python manage.py migrate
```
Then reload the page.


If you still see this error after migrating, verify you're running commands in the same project directory and virtual environment used by `runserver`:
```bash
which python
python manage.py showmigrations listings chatapp
python manage.py migrate
```
