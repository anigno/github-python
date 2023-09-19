from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data (in-memory storage for simplicity)
products = {
    '12345': {'name': 'Product A', 'price': 10.99},
    '67890': {'name': 'Product B', 'price': 7.49},
}

shopping_cart = {}

# http://127.0.0.1:5000//products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

"""in postman,[http://127.0.0.1:5000/add-to-cart/12345] set message to POST, add 'Content-Type' header to 'application/json' and in body add:
 {"quantity":3} or just {} as raw"""

@app.route('/add-to-cart/<product_id>', methods=['POST'])
def add_to_cart(product_id):
    if product_id not in products:
        return jsonify({'error': 'Product not found'}), 404
    quantity = request.json.get('quantity', 1)
    if product_id in shopping_cart:
        shopping_cart[product_id] += quantity
    else:
        shopping_cart[product_id] = quantity
    return jsonify({'message': f'Product added to cart currently in cart: {shopping_cart[product_id]}'}), 200

"""[http://127.0.0.1:5000/cart]"""

@app.route('/cart', methods=['GET'])
def view_cart():
    cart_contents = []
    total_cost = 0

    for product_id, quantity in shopping_cart.items():
        product = products.get(product_id)
        if product:
            item_total = product['price'] * quantity
            total_cost += item_total
            cart_contents.append({
                'product_id': product_id,
                'name': product['name'],
                'price': product['price'],
                'quantity': quantity,
                'item_total': item_total,
            })

    return jsonify({'cart_contents': cart_contents, 'total_cost': total_cost})

@app.route('/checkout', methods=['POST'])
def checkout():
    # In a real application, you would handle payment processing here.
    # For simplicity, we'll just clear the cart in this example.
    shopping_cart.clear()
    return jsonify({'message': 'Checkout successful'}), 200

if __name__ == '__main__':
    app.run(debug=True)
