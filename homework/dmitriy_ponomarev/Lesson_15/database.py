import psycopg2
from psycopg2.extras import RealDictCursor

db = psycopg2.connect(
    dbname='test2',
    user='postgres',
    password='1qaz2wsx',
    host='localhost',
    port='5432'
)

cursor = db.cursor(cursor_factory=RealDictCursor)
cursor.execute('SELECT * FROM users')
data = cursor.fetchall()
print(data)
# for user in data:
#     print(user['surname'])

cursor.execute('SELECT * FROM users WHERE id = 1')
data2 = cursor.fetchone() # т.к. это объект RealDictRow
result = dict(data2)
print(result)

# query = "SELECT * FROM users WHERE name = '{0}' and surname = '{1}'"
# cursor.execute(query.format(input('name'), input('surname')))
# nameDmitriy'; --   (SQL-иньекция, используется для взлома БД)
# surnamepupkin

# query = "SELECT * FROM users WHERE name = %s and surname = %s"
# cursor.execute(query, (input('name'), input('surname')))
# print(cursor.fetchall())


cursor.execute("INSERT INTO users (name, surname, age) VALUES ('Vladimir', 'Pozner', 77)")
student_id = cursor.lastrowid
cursor.execute(f"SELECT * FROM users where id = {student_id}")
print(cursor.fetchone())

insert_query = "INSERT INTO books (title, price) VALUES (%s, %s)"
cursor.executemany(
    insert_query, [
    ('Garry Potter', 2500),
    ('The Picture of Dorian Gray', 1200),
    ('The Great Gatsby', 3000)
    ]
   )


select_query = '''
SELECT * FROM users 
WHERE name = 'Dmitriy' 
AND surname = 'Ponomarev'
'''
cursor.execute(select_query)
print(cursor.fetchall())

db.commit()

db.close()
