import os
import secrets

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
    {
        "id": 4,
        "name": "Studio Wireless Headphones",
        "category": "Electronics",
        "description": "Comfortable over-ear headphones with a clean, minimal profile for focused listening at home or on the move. Soft ear cushions and a foldable design make them easy to wear and pack.",
        "price": 129.00,
        "image": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?auto=format&fit=crop&w=900&q=85",
        "gallery": [
            "https://images.unsplash.com/photo-1484704849700-f032a568e944?auto=format&fit=crop&w=1000&q=85",
            "https://images.unsplash.com/photo-1546435770-a3e426bf472b?auto=format&fit=crop&w=1000&q=85",
        ],
        "color": "#d8dce0",
    },
    {
        "id": 5,
        "name": "Pocket Bluetooth Speaker",
        "category": "Electronics",
        "description": "A compact wireless speaker with clear, room-filling sound. Its simple shape and portable size make it an easy addition to a desk, kitchen, or weekend away.",
        "price": 76.00,
        "image": "https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?auto=format&fit=crop&w=900&q=85",
        "gallery": [
            "https://images.unsplash.com/photo-1589003077984-894e133dabab?auto=format&fit=crop&w=1000&q=85",
            "https://images.unsplash.com/photo-1545454675-3531b543be5d?auto=format&fit=crop&w=1000&q=85",
        ],
        "color": "#d7e0dc",
    },
    {
        "id": 6,
        "name": "Ripple Ceramic Vase",
        "category": "Home",
        "description": "A hand-finished ceramic vase with a softly textured surface. Display it with a few fresh stems or let its sculptural shape stand on its own on a shelf or table.",
        "price": 54.00,
        "image": "https://images.unsplash.com/photo-1578500494198-246f612d3b3d?auto=format&fit=crop&w=900&q=85",
        "gallery": [
            "https://images.unsplash.com/photo-1578749556568-bc2c40e68b61?auto=format&fit=crop&w=1000&q=85",
            "https://images.unsplash.com/photo-1576021182211-9ea8dced3690?auto=format&fit=crop&w=1000&q=85",
        ],
        "color": "#e2d7cc",
    },
    {
        "id": 7,
        "name": "Everyday Cotton Tee",
        "category": "Clothing",
        "description": "A versatile crew-neck tee made for repeat wear. The straightforward cut layers easily and pairs with everything from relaxed denim to a favourite overshirt.",
        "price": 32.00,
        "image": "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?auto=format&fit=crop&w=900&q=85",
        "gallery": [
            "https://images.unsplash.com/photo-1503341504253-dff4815485f1?auto=format&fit=crop&w=1000&q=85",
            "https://images.unsplash.com/photo-1523381210434-271e8be1f52b?auto=format&fit=crop&w=1000&q=85",
        ],
        "color": "#e4e2d9",
    },
    {
        "id": 8,
        "name": "Utility Overshirt",
        "category": "Clothing",
        "description": "An easy midweight layer with a relaxed fit and practical pockets. Wear it open over a tee or buttoned up when the day calls for an extra layer.",
        "price": 88.00,
        "image": "https://images.unsplash.com/photo-1591047139829-d91aecb6caea?auto=format&fit=crop&w=900&q=85",
        "gallery": [
            "https://images.unsplash.com/photo-1598033129183-c4f50c736f10?auto=format&fit=crop&w=1000&q=85",
            "https://images.unsplash.com/photo-1551028719-00167b16eac5?auto=format&fit=crop&w=1000&q=85",
        ],
        "color": "#d7ddd3",
    },
    {
        "id": 9,
        "name": "Canvas Market Tote",
        "category": "Accessories",
        "description": "A sturdy everyday carryall with room for market finds, books, and daily essentials. Lightweight canvas and comfortable shoulder straps make it ready for errands or a day out.",
        "price": 28.00,
        "image": "https://images.unsplash.com/photo-1590874103328-eac38a683ce7?auto=format&fit=crop&w=900&q=85",
        "gallery": [
            "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?auto=format&fit=crop&w=1000&q=85",
            "https://images.unsplash.com/photo-1544816155-12df9643f363?auto=format&fit=crop&w=1000&q=85",
        ],
        "color": "#e2dacb",
    },
    {
        "id": 10,
        "name": "Fold Card Wallet",
        "category": "Accessories",
        "description": "A slim wallet designed to keep everyday cards and a few folded notes close at hand. Its compact shape slips easily into a pocket or small bag.",
        "price": 46.00,
        "image": "https://images.unsplash.com/photo-1627123424574-724758594e93?auto=format&fit=crop&w=900&q=85",
        "gallery": [
            "https://images.unsplash.com/photo-1622560480654-d96214fdc887?auto=format&fit=crop&w=1000&q=85",
            "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?auto=format&fit=crop&w=1000&q=85",
        ],
        "color": "#d9d2c7",
    },
]


def _get_cart_summary():
    cart = session.get("cart", {})
    cart_items = [
        {
            **product,
            "quantity": cart.get(str(product["id"]), 0),
        }
        for product in PRODUCTS
        if cart.get(str(product["id"]), 0) > 0
    ]
    return {
        "cart_items": cart_items,
        "total": sum(item["price"] * item["quantity"] for item in cart_items),
        "cart_count": sum(cart.values()),
    }


@app.get("/")
def home():
    search_query = request.args.get("q", "").strip()
    products = PRODUCTS
    if search_query:
        normalized_query = search_query.casefold()
        products = [
            product
            for product in PRODUCTS
            if normalized_query in product["name"].casefold()
            or normalized_query in product["category"].casefold()
        ]
    cart_count = sum(session.get("cart", {}).values())
    return render_template(
        "index.html",
        products=products,
        total_products=len(PRODUCTS),
        search_query=search_query,
        cart_count=cart_count,
    )


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
    return render_template("cart.html", **_get_cart_summary())


@app.get("/checkout")
def checkout():
    summary = _get_cart_summary()
    if not summary["cart_items"]:
        return redirect(url_for("view_Cart"))
    return render_template("checkout.html", **summary, customer={})


@app.post("/checkout")
def place_order():
    summary = _get_cart_summary()
    if not summary["cart_items"]:
        return redirect(url_for("view_Cart"))

    customer = {
        "name": request.form.get("name", "").strip(),
        "email": request.form.get("email", "").strip(),
        "address": request.form.get("address", "").strip(),
    }
    email_domain = customer["email"].rsplit("@", 1)[-1]
    if not all(customer.values()) or "@" not in customer["email"] or "." not in email_domain:
        return render_template(
            "checkout.html",
            **summary,
            customer=customer,
            error="Enter your name, a valid email address, and a delivery address.",
        ), 400

    order = {
        "reference": secrets.token_hex(4).upper(),
        "customer": customer,
        "items": [
            {
                "name": item["name"],
                "quantity": item["quantity"],
                "price": item["price"],
            }
            for item in summary["cart_items"]
        ],
        "total": summary["total"],
    }
    session["last_order"] = order
    session.pop("cart", None)
    return redirect(url_for("order_confirmation"))


@app.get("/order-confirmation")
def order_confirmation():
    order = session.get("last_order")
    if not order:
        return redirect(url_for("home"))
    return render_template(
        "order_confirmation.html",
        order=order,
        cart_count=sum(session.get("cart", {}).values()),
    )


if __name__ == "__main__":
    app.run(debug=True)