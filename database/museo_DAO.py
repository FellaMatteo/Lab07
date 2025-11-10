from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""

class MuseoDAO:
    def __init__(self):
        pass

    def get_all_musei(self):
        cnx = ConnessioneDB.get_connection()
        if cnx is None:
            return []
        cursor = cnx.cursor(dictionary=True)
        query = "SELECT id, nome, tipologia FROM museo ORDER BY nome"
        cursor.execute(query)
        musei = [Museo(row["id"], row["nome"], row["tipologia"]) for row in cursor]
        cursor.close()
        cnx.close()
        return musei
