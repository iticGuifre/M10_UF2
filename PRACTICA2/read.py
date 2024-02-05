import connection

sql = "SELECT * FROM pilotes"
def llegir():
    connection.connection.execute(sql)
    print(connection.connection.fetchall())
