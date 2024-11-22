# **E-Commerce Backend**

This repository contains the backend system for a simple e-commerce platform, built using **Flask** and **SQLAlchemy**. The platform supports user registration, product management, shopping cart functionality, and order placement. It follows modular design principles and incorporates best practices for maintainability and scalability.

---

## **Features**
- **User Management**:
  - Register, log in, and manage user accounts.
  - Secure password hashing for authentication.
- **Product Management**:
  - Admins can create, update, and delete products.
  - Regular users can view a list of available products.
- **Cart and Order Management**:
  - Users can add products to their cart and place orders.
  - Orders are saved with details, and the cart is cleared post-checkout.
- **Data Persistence**:
  - Data (users, products, carts, orders) is stored in an SQLite database.
- **Testing**:
  - Unit tests are provided for critical features, such as user registration and order placement.

---

## **Technologies Used**
- **Python**: Core language for development.
- **Flask**: Web framework for API creation.
- **SQLAlchemy**: ORM for managing database operations.
- **SQLite**: Lightweight database for local development.
- **bcrypt**: Secure password hashing.
- **pytest**: Framework for unit testing.
- **Poetry**: Dependency and environment management.

---

## **Installation**

### **1. Clone the Repository**
```bash
git clone https://github.com/igorconsulting/e_commerce.git
cd e_commerce
```

### **2. Install Dependencies Using Poetry**
Ensure that Poetry is installed. If not, install it:
```bash
pip install poetry
```

Then install the project dependencies:
```bash
poetry install
```

### **3. Activate the Virtual Environment**
```bash
poetry shell
```

### **4. Initialize the Database**
```bash
python
>>> from app.database import init_db
>>> from main import app
>>> init_db(app)
```

---

## **Usage**

### **Run the Application**
```bash
python main.py
```

The server will be available at `http://127.0.0.1:5000`.

### **API Endpoints**

#### **User Management**
- `POST /register`: Register a new user.
- `POST /login`: Authenticate a user (to be implemented).

#### **Product Management**
- `POST /products`: Add a product (admin only).
- `GET /products`: List all available products.

#### **Cart Management**
- `POST /cart`: Add an item to the cart (to be implemented).
- `GET /cart`: View the user's cart (to be implemented).

#### **Order Management**
- `POST /orders`: Place an order (to be implemented).
- `GET /orders`: View the user's orders (to be implemented).

---

## **Testing**

### **Run Unit Tests**
```bash
pytest
```

Unit tests are included for features like user registration. Extend these tests as new functionalities are added.

---

## **Project Structure**

```
e_commerce/
├── app/
│   ├── __init__.py           # Application initialization
│   ├── models.py             # Database models (User, Product, Cart, Order)
│   ├── routes.py             # API route handlers
│   ├── database.py           # Database setup and configuration
│   ├── auth.py               # Password hashing and authentication logic
├── tests/
│   ├── test_routes.py        # Unit tests for routes
├── main.py                   # Entry point for the application
├── poetry.lock               # Lock file for dependencies
├── pyproject.toml            # Poetry configuration
├── README.md                 # Project documentation
```

---

## **Design Patterns Used**
1. **Singleton**: For managing the shared `db` instance.
2. **Active Record**: Encapsulates database interactions within models.
3. **Blueprint**: Organizes routes into reusable modules.
4. **Factory**: Initializes the database through a dedicated function.
5. **Dependency Injection**: Injects database configurations into the application.

---

## **Future Enhancements**
- Add JWT-based authentication for secure user sessions.
- Implement input validation and robust error handling.
- Improve scalability for the cart and order functionalities.
- Integrate with a frontend built using modern frameworks (e.g., React, Vue.js).

---

## **Author**
- **Igor Caetano** - MLEng and Maintainer

---

## **License**
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.