import psycopg2
import bcrypt

# database connection
conn = psycopg2.connect("postgresql://postgres:computer@localhost/ecommerce")

# create crusor
cur = conn.cursor()

# Create a table for user credentials and roles
with conn.cursor() as cur:
    cur.execute("""
        CREATE TABLE users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            password VARCHAR(100) NOT NULL,
            role VARCHAR(50) NOT NULL
        )
    """)

# autocommit
conn.set_session(autocommit=True)

import bcrypt

# Register a new user
def register_user(username, password, role):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO users (usernme, password, role)
            VALUES (%s, %s, %s)
        """, (username, hashed_password, role))
        conn.commit()

# Login a user and return the user's role if the login is successful
def login_user(username, password):
    with conn.cursor() as cur:
        cur.execute("""
            SELECT password, role FROM users WHERE username = %s
        """, (username,))
        row = cur.fetchone()
        if row:
            hashed_password = row[0]
            role = row[1]
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                return role
    return None

# Example function that requires a specific role
def admin_only_function(user_role):
    if user_role == 'admin':
        # Allow access
        pass
    else:
        # Deny access
        pass

