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
