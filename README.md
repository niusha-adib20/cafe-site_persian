# کافه ما | Persian Cafe Website

A Persian, right-to-left cafe website built with **Django**. Visitors can browse a cafe menu, create an account, place orders, reserve a table, and participate in time-limited auctions.

> This is a portfolio and learning project. Orders are saved in the application; the project does not include online payment or order fulfillment integrations.

## Features

- Persian-language, RTL website pages for the cafe, menu, reservations, and auctions
- Account registration, login, and logout using Django authentication
- Database-backed menu items grouped by category, with descriptions, prices, and images
- Authenticated users can submit orders and table reservations
- A personal dashboard showing the signed-in user's orders and reservations
- Auction listings with countdowns, bid history, and the highest bid shown as the winner after the auction ends
- Django Admin for managing menu items, orders, reservations, auctions, and bids
- Local SQLite database and media-file storage

## Tech stack

- Python 3.11 recommended
- Django 5.1.6
- SQLite
- HTML, CSS, Django templates
- Pillow for image fields

## Getting started

### Prerequisites

- Python 3.11 or later compatible with the pinned Django version
- Git

### 1. Clone the repository

```bash
git clone https://github.com/niusha-adib20/cafe-site_persian.git
cd cafe-site_persian
```

### 2. Create and activate a virtual environment

**Windows PowerShell:**

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies and prepare the database

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python manage.py migrate
```

### 4. Start the development server

```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

To manage menu or auction content, create an administrator account and visit Django Admin:

```bash
python manage.py createsuperuser
```

Then open [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/). Menu item images are uploaded under `media/menu_items/`.

## Main pages

| Page | URL | Access |
|---|---|---|
| Home | `/` | Public |
| Menu | `/menu/` | Public |
| Sign in | `/login/` | Public |
| Sign up | `/signUp/` | Public |
| Table reservation | `/reservation/` | Sign-in required to submit |
| User dashboard | `/orders/dashboard/` | Sign-in required |
| Auction list | `/auction/` | Public |
| Auction details | `/auction/<auction_id>/` | Public; sign-in required to bid |
| Django Admin | `/admin/` | Staff account |

The menu and auction pages display records from the database. If they are empty in a fresh local database, add content through Django Admin.

## Project structure

```text
cafe-site_persian/
├── cafe/                  # Django project settings and root URLs
├── accounts/              # Registration, login, home, and menu pages
├── orders/                # Menu items, orders, reservations, and dashboard
├── auction/               # Auctions, bids, and auction pages
├── templates/             # Shared and page-specific Django templates
├── static/                # CSS, fonts, and static images
├── media/menu_items/      # Uploaded menu item images
├── manage.py
├── requirements.txt
└── LICENSE
```

## Current scope and deployment notes

- Order submission records a menu item, quantity, and total in the database. There is no payment gateway, cart checkout, or fulfillment workflow.
- The auction flow records bids above the starting price and current highest bid. Review and harden auction closing, validation, and concurrency behavior before using it for real transactions.
- The repository settings are configured for local development, including `DEBUG = True`, an in-source Django secret key, and SQLite. Before deployment, use a new secret key from a secure environment setting, set `DEBUG = False`, configure `ALLOWED_HOSTS`, and choose an appropriate production database and static/media storage.
- Uploaded media is stored locally. Production deployments need persistent storage, backups, and upload validation.
- A test directory exists for each Django app, but the current `tests.py` files contain Django's empty test placeholders.

## License

Released under the [MIT License](LICENSE).
