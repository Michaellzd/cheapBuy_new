import mysql.connector
import configparser

def create_connection():
    """创建并返回数据库连接和光标"""

    # 读取.ini文件
    config = configparser.ConfigParser()
    config.read('db.ini')

    # 获取数据库配置信息
    db_config = config['database']
    print(db_config)
    # 连接到数据库
    conn = mysql.connector.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password'],
        database=db_config['database']
    )

    cursor = conn.cursor()
    return conn, cursor

def add_user(email, url, cursor, conn):
    cursor.execute("INSERT INTO users (email, url) VALUES (%s, %s)", (email, url))
    conn.commit()

def add_product_url(url, user_id, cursor, conn):
    cursor.execute("INSERT INTO product_urls (url, user_id) VALUES (%s, %s)", (url, user_id))
    conn.commit()

def close_connection(cursor, conn):
    cursor.close()
    conn.close()

if __name__ == '__main__':
    conn,cursor=create_connection()
    close_connection(cursor,conn)

