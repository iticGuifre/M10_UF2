import psycopg2

conn = psycopg2.connect(
    database='postgres',
    user='guifre',
    password='123456',
    host='localhost',
    port='5432'
)

connection = conn.cursor()
print(connection)
