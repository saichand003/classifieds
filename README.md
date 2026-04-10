# CityConnect (Rich UI Marketplace MVP)

A Django + SQLite marketplace app inspired by local discovery apps like Sulekha.

## Rich UI features included

- Modern card-based responsive layout.
- Homepage hero with KPI counters.
- Multi-filter search (keyword, category, city, sort).
- Category chips for quick exploration.
- Listing cards with image thumbnails and featured badges.
- Improved detail page layout (content + inquiry sidebar).
- Dark mode toggle with local preference persistence.
- Toast-style success messages.

## Product features

- User registration/login/logout.
- Post listings with category, location, contact phone, optional image and optional price.
- Featured listings.
- Inquiry form on listing detail.
- Direct user-to-user chat.

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Or:

```bash
./run_local.sh
```

## Routes

- `/` Marketplace homepage
- `/post/` Create listing
- `/listing/<id>/` Listing detail + inquiry
- `/chat/` Chat inbox
- `/accounts/register/` Register
- `/accounts/login/` Login


## How to compile the latest code

Use one of the following:

### Option A: direct command
```bash
source .venv/bin/activate
python -m compileall .
```

### Option B: Makefile shortcut
```bash
make compile
```

This validates Python syntax by byte-compiling all project files.


## If you still see the old UI

1. Stop and restart the dev server.
2. Hard refresh your browser (`Cmd+Shift+R` on macOS).
3. Verify the footer shows `UI version: 2026-04-10-1`.
4. If needed, clear cached static files and restart:

```bash
find . -type d -name "__pycache__" -prune -exec rm -rf {} +
python manage.py runserver
```
