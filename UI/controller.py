import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view
        self.museo_selezionato = None
        self.epoca_selezionata = None
        self.popola_dropdown()

    def popola_dropdown(self):
        musei = self._model.get_musei()
        epoche = self._model.get_epoche()

        self._view._museo_dropdown.options.clear()
        self._view._museo_dropdown.options.append(ft.dropdown.Option("Nessun filtro"))
        for m in musei:
            self._view._museo_dropdown.options.append(ft.dropdown.Option(str(m.id)))
        self._view._museo_dropdown.update()

        self._view._epoca_dropdown.options.clear()
        self._view._epoca_dropdown.options.append(ft.dropdown.Option("Nessun filtro"))
        for e in epoche:
            self._view._epoca_dropdown.options.append(ft.dropdown.Option(e))
        self._view._epoca_dropdown.update()

    def on_museo_changed(self, e):
        self.museo_selezionato = e.control.value

    def on_epoca_changed(self, e):
        self.epoca_selezionata = e.control.value

    def mostra_artefatti(self, e):
        artefatti = self._model.get_artefatti_filtrati(
            museo=self.museo_selezionato,
            epoca=self.epoca_selezionata
        )

        self._view._list_view.controls.clear()

        if not artefatti:
            self._view.show_alert("Nessun artefatto trovato per i filtri selezionati.")
        else:
            for a in artefatti:
                card = ft.Card(
                    content=ft.Container(
                        content=ft.Column([
                            ft.Text(f"Nome: {a.nome}", size=16, weight="bold"),
                            ft.Text(f"Epoca: {a.epoca}"),
                            ft.Text(f"Museo: {a.id_museo}")
                        ]),
                        padding=10
                    ),
                    margin=10
                )
                self._view._list_view.controls.append(card)

        self._view._list_view.update()