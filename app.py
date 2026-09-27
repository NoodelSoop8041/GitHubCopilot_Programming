import os

from flask import Flask, abort, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "development-only-key")

PRODUCTS = [
    {
        "id": 1,
        "name": "Arc Table Lamp",
        "category": "Lighting",
        "description": "A softly arched silhouette and warm, diffused light make this an easy companion for late reading and slow mornings. Its compact footprint fits neatly on a bedside table or a favourite sideboard.",
        "price": 84.00,
        "image": "https://images.unsplash.com/photo-1507473885765-e6ed057f782c?auto=format&fit=crop&w=900&q=85",
        "gallery": [
            "https://images.unsplash.com/photo-1513506003901-1e6a229e2d15?auto=format&fit=crop&w=1000&q=85",
            "https://images.unsplash.com/photo-1543198126-a8ad8e47fb22?auto=format&fit=crop&w=1000&q=85",
        ],
        "color": "#e5d9c9",
    },
    {
        "id": 2,
        "name": "Form Lounge Chair",
        "category": "Furniture",
        "description": "A relaxed seat with a sculptural profile, made for settling in with a book or an unhurried cup of coffee. Its simple lines bring a considered touch to a reading corner or living room.",
        "price": 340.00,
        "image": "https://images.unsplash.com/photo-1503602642458-232111445657?auto=format&fit=crop&w=900&q=85",
        "gallery": [
            "https://images.unsplash.com/photo-1567538096630-e0c55bd6374c?auto=format&fit=crop&w=1000&q=85",
            "https://images.unsplash.com/photo-1598300053653-d4a4e1e7a3b2?auto=format&fit=crop&w=1000&q=85",
        ],
        "color": "#dce2d8",
    },
    {
        "id": 3,
        "name": "Sunday Coffee Table",
        "category": "Furniture",
        "description": "A low, easygoing centerpiece for everyday living. Its clean profile leaves room for coffee, books, and the little things you like to keep close, while warm natural wood brings an inviting finish to the room.",
        "price": 248.00,
        "image": "https://images.unsplash.com/photo-1533090481720-856c6e3c1fdc?auto=format&fit=crop&w=900&q=85",
        "gallery": [
            "https://images.unsplash.com/photo-1494438639946-1ebd1d20bf85?auto=format&fit=crop&w=1000&q=85",
            "https://images.unsplash.com/photo-1616486338812-3dadae4b4ace?auto=format&fit=crop&w=1000&q=85",
        ],
        "color": "#d9c8b3",
    },
]


@app.get("/")
def home():
    cart_count = sum(session.get("cart", {}).values())
    return render_template("index.html", products=PRODUCTS, cart_count=cart_count)


@app.get("/products/<int:product_id>")
def product_detail(product_id):
    product = next((item for item in PRODUCTS if item["id"] == product_id), None)
    if product is None:
        abort(404)
    cart_count = sum(session.get("cart", {}).values())
    return render_template("product.html", product=product, cart_count=cart_count)


@app.post("/cart/add/<int:product_id>")
def add_to_cart(product_id):
    if any(product["id"] == product_id for product in PRODUCTS):
        cart = session.get("cart", {})
        product_key = str(product_id)
        cart[product_key] = cart.get(product_key, 0) + 1
        session["cart"] = cart
    if request.form.get("return_to") == "product":
        return redirect(url_for("product_detail", product_id=product_id))
    return redirect(url_for("home", _anchor="collection"))


@app.post("/cart/update/<int:product_id>")
def update_cart_quantity(product_id):
    quantity = request.form.get("quantity", type=int)
    if any(product["id"] == product_id for product in PRODUCTS) and 1 <= (quantity or 0) <= 99:
        cart = session.get("cart", {})
        product_key = str(product_id)
        if product_key in cart:
            cart[product_key] = quantity
            session["cart"] = cart
    return redirect(url_for("view_Cart"))


@app.post("/cart/remove/<int:product_id>")
def remove_from_cart(product_id):
    if any(product["id"] == product_id for product in PRODUCTS):
        cart = session.get("cart", {})
        cart.pop(str(product_id), None)
        session["cart"] = cart
    return redirect(url_for("view_Cart"))


@app.get("/cart")
def view_Cart():
    cart = session.get("cart", {})
    cart_items = [
        {
            **product,
            "quantity": cart.get(str(product["id"]), 0),
        }
        for product in PRODUCTS
        if cart.get(str(product["id"]), 0) > 0
    ]
    total = sum(item["price"] * item["quantity"] for item in cart_items)

    return render_template(
        "cart.html",
        cart_items= cart_items,
        total=total,
        cart_count=sum(cart.values()),
    )


if __name__ == "__main__":
    app.run(debug=True)