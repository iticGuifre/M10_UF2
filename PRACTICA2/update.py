import connection

def actualitza(diametre, color, pes, forma, esRugosa, material):
    sql = f"UPDATE pilotes SET color = '{color}', pes = {pes}, forma = '{forma}', esRugosa = {esRugosa}, material = '{material}' WHERE diametre = {diametre};"
    connection.connection.execute(sql)
    connection.conn.commit()
