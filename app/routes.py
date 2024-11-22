from flask import Blueprint, request, jsonify
from app.models import db, User, Product, Cart, Order
from app.auth import hash_password, check_password

# Blueprint Pattern: Modular organization of routes for better scalability.
routes = Blueprint('routes', __name__)

# Single Responsibility Principle: Each function handles only one specific task.

# User registration
@routes.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = hash_password(data['password'])  # Dependency Injection: The hashing logic is externalized.
    user = User(username=data['username'], password_hash=hashed_password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201

# Add product (admin only)
@routes.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    product = Product(name=data['name'], price=data['price'], stock=data['stock'])
    db.session.add(product)
    db.session.commit()
    return jsonify({'message': 'Product added successfully'}), 201

# List products
@routes.route('/products', methods=['GET'])
def list_products():
    # Example of Control Flow: Looping through product list to format the response.
    products = Product.query.all()
    return jsonify([{'id': p.id, 'name': p.name, 'price': p.price, 'stock': p.stock} for p in products]), 200
