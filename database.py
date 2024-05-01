import psycopg2

Dbname ='PyProject'
Username='postgres'
Hostname='localhost'
Port= '5432'
conn=None
cur=None

def connect_to_database():
    try:
        # Connect to the database
        conn = psycopg2.connect(
            dbname=Dbname,
            user=Username,
            password=Password,
            host=Hostname,
            port=Port
        )
        return conn

    except psycopg2.Error as e:
        return None, f"Error connecting to the database: {e}"

def signup_user(name, passw, email):
    conn = connect_to_database()
    if conn is None:
        return False, "Error connecting to the database"

    try:
        # Create a cursor
        cur = conn.cursor()

        # Check if the username already exists
        cur.execute("SELECT user_name FROM info WHERE user_name = %s", (name,))
        existing_user = cur.fetchone()

        if existing_user:
            return False, "Error: Username already exists."

        # Insert new user into the database
        cur.execute("INSERT INTO info (user_name, user_password, user_emailid) VALUES (%s, %s, %s)", (name, passw, email))
        conn.commit()  # Commit the transaction

        return True, "User signup successful."

    except psycopg2.Error as e:
        return False, f"Error signing up user: {e}"

    finally:
        # Close cursor and connection
        if cur:
            cur.close()
        if conn:
            conn.close()

def login(name, passw):
    conn = connect_to_database()
    if conn is None:
        return False, "Error connecting to the database"

    try:
        # Create a cursor
        cur = conn.cursor()

        cur.execute('SELECT * FROM info WHERE user_name=%s AND user_password=%s', (name, passw))
        user = cur.fetchone()

        if user:
            return True, "Login Successful"
        else:
            return False, "Login Failed.Incorrect Username or Password entered"

    except psycopg2.Error as e:
        return False, f"Error logging in: {e}"

    finally:
        # Close cursor and connection
        if cur:
            cur.close()
        if conn:
            conn.close()
