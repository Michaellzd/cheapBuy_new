import mysql.connector
import configparser


# 读取.ini文件
config = configparser.ConfigParser()
config.read('db.ini')

# 获取数据库配置信息
db_config = config['database']

# 连接到数据库
conn = mysql.connector.connect(
    host=db_config['host'],
    user=db_config['user'],
    password=db_config['password'],
    database=db_config['database']
)
cursor = conn.cursor()

# create_db
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    url VARCHAR(255) NOT NULL

)
''')

conn.commit()
conn.close()
