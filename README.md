# CityConnect (Sulekha-style Classifieds MVP)

A Django + SQLite marketplace app inspired by local community discovery platforms (services, rentals, jobs, buy/sell, and events).

## Current MVP features

- User registration/login/logout.
- Post listings with category, city/state/country, phone, optional image, optional price.
- Featured listings.
- Search + filters by query/category/city on homepage.
- Listing detail page with inquiry form (lead capture).
- Direct user-to-user chat.

## Requirements

- Python 3.10+ (3.11+ recommended)
- pip (use `python -m pip`)

## Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Or use:

```bash
./run_local.sh
```

## Core routes

- `/` Marketplace homepage (search/filter listings)
- `/post/` Post a new listing
- `/listing/<id>/` Listing details + inquiry form
- `/chat/` Chat inbox
- `/accounts/register/` Registration
- `/accounts/login/` Login

## Next steps to get even closer to Sulekha

- Add service providers business profiles and ratings.
- Add paid promotions + ad packages.
- Add saved searches and email alerts.
- Add geolocation, map results, and nearby sorting.
- Add moderation workflows and abuse reporting.
