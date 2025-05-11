
from flask import Flask
import psycopg2
import os

app = Flask(__name__)

@app.route('/')
def hello():
    # Connect to the database
    try:
        conn = psycopg2.connect(
            dbname="mydatabase",
            user=os.environ.get('DATABASE_USER'),
            password=os.environ.get('DATABASE_PASSWORD'),
            host=os.environ.get('DATABASE_HOST')
        )
        # Fetch a simple query from the database
        cur = conn.cursor()
        cur.execute('SELECT 1')
        db_test = cur.fetchone()
        cur.close()
        return f"Hello from Flask! Database connection test: {db_test}"
    except psycopg2.OperationalError as e:
        return f"Connection error: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
