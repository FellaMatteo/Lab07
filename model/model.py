from database.museo_DAO import MuseoDAO
from database.artefatto_DAO import ArtefattoDAO

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di MuseoDAO e ArtefattoDAO)
'''

class Model:
    def __init__(self):
        self._museo_dao = MuseoDAO()
        self._artefatto_dao = ArtefattoDAO()

    # --- ARTEFATTI ---
    def get_artefatti_filtrati(self, museo: str, epoca: str):
        if museo == "Nessun filtro":
            museo = None
        if epoca == "Nessun filtro":
            epoca = None
        return self._artefatto_dao.get_artefatti(museo_id=museo, epoca=epoca)

    def get_epoche(self):
        artefatti = self._artefatto_dao.get_artefatti()
        epoche = sorted({a.epoca for a in artefatti if a.epoca})
        return epoche

    def get_musei(self):
        return self._museo_dao.get_all_musei()

