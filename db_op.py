import mysql.connector

# db
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="cheapbuy"
)

cursor = conn.cursor()

def add_user(email, url):
    cursor.execute("INSERT INTO users (email, url) VALUES (%s, %s)", (email, url))
    conn.commit()


def add_product_url(url, user_id):
    cursor.execute("INSERT INTO product_urls (url, user_id) VALUES (%s, %s)", (url, user_id))
    conn.commit()

def close_connection():
    cursor.close()
    conn.close()


if __name__ == '__main__':
    close_connection()