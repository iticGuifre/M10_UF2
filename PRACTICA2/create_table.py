import connection

sql = 'CREATE TABLE pilotes (diametre INT, color VARCHAR(255), pes INT, forma VARCHAR(255), esRugosa BOOLEAN, material VARCHAR(255));'

connection.connection.execute(sql)

connection.conn.commit()
