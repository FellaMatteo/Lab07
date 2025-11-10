from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto

class ArtefattoDAO:
    def __init__(self):
        pass

    def get_artefatti(self, museo_id=None, epoca=None):
        cnx = ConnessioneDB.get_connection()
        if cnx is None:
            return []
        cursor = cnx.cursor(dictionary=True)
        query = """
            SELECT id, nome, tipologia, epoca, id_museo
            FROM artefatto
            WHERE id_museo = COALESCE(%s, id_museo)
              AND epoca = COALESCE(%s, epoca)
            ORDER BY nome
        """
        cursor.execute(query, (museo_id, epoca))
        artefatti = [
            Artefatto(
                id=row["id"],
                nome=row["nome"],
                tipologia=row["tipologia"],
                epoca=row["epoca"],
                id_museo=row["id_museo"]
            )
            for row in cursor
        ]
        cursor.close()
        cnx.close()
        return artefatti
