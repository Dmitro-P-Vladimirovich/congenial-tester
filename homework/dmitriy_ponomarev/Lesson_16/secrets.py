import psycopg2
from psycopg2.extras import RealDictCursor
from homework.dmitriy_ponomarev.Lesson_16 import creds
import os
import dotenv

dotenv.load_dotenv()

db = psycopg2.connect(
    dbname=os.getenv('DB_NAME'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSW'),
    host=creds.host,
    port=creds.port
)

cursor = db.cursor(cursor_factory=RealDictCursor)
cursor.execute('SELECT * FROM users')
data = cursor.fetchall()
print(data)