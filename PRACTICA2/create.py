import connection

def crear(diametre, color, pes, forma, esRugosa, material):
    sql = f"INSERT INTO pilotes (diametre, color, pes, forma, esRugosa, material) VALUES ({diametre}, '{color}', {pes}, '{forma}', {esRugosa}, '{material}');"
    connection.connection.execute(sql)
    connection.conn.commit()



