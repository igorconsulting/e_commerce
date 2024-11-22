from flask_bcrypt import Bcrypt

# Singleton Pattern: A single `bcrypt` instance is shared across the application.
bcrypt = Bcrypt()

# Function to hash passwords (Single Responsibility Principle: focuses only on password hashing).
def hash_password(password):
    return bcrypt.generate_password_hash(password).decode('utf-8')

# Function to check passwords (Single Responsibility Principle: focuses only on validation).
def check_password(password, hashed_password):
    return bcrypt.check_password_hash(hashed_password, password)
