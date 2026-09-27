# Morrow Goods

Morrow Goods is a small e-commerce storefront demo built with Python and Flask. Visitors can browse a curated sample collection, view product descriptions and photo galleries, and manage a session-based shopping bag.

## Features

- Responsive storefront homepage with three sample products.
- Individual product pages with descriptions, pricing, and photo galleries.
- Shopping bag with add, quantity update, and remove actions.
- Subtotal calculation and an empty-bag state.

## Requirements

- Python 3.9 or newer.
- Internet access to load the product photography and web fonts.

## Installation

Open PowerShell in the project directory and create a virtual environment:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run the application

Start Flask's development server from the project directory:

```powershell
flask --app app run --debug
```

Open http://127.0.0.1:5000 in a browser. Stop the server with `Ctrl+C`; leave the virtual environment with `deactivate`.

## Using the storefront

1. Browse the collection on the homepage.
2. Select a product image or name to open its detail page. The sample product pages are `/products/1`, `/products/2`, and `/products/3`.
3. Add a product to the bag from either the homepage or its detail page.
4. Open **Bag** to change an item's quantity (1-99), remove it, or review the subtotal.

The bag is stored in Flask's signed session cookie. It is intended for this demo and is not a substitute for persistent order storage. The application does not include checkout, payment processing, or an inventory database.

## Project structure

```text
app.py                  Flask routes and sample product data
requirements.txt        Python dependencies
static/style.css        Responsive storefront and cart styles
templates/index.html    Storefront homepage
templates/product.html Product detail page
templates/cart.html    Shopping bag page
```

## Configuration and deployment

For local development, the app has a fallback session key. Before deployment, set `SECRET_KEY` to a long, randomly generated value and keep it out of source control. Do not use Flask's debug development server in production; configure a production WSGI server and add persistent storage and checkout services as needed.
