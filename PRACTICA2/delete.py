import connection

def elimina(diametre):
    sql = f"DELETE FROM pilotes WHERE diametre = {diametre};"
    connection.connection.execute(sql)
    connection.conn.commit()
