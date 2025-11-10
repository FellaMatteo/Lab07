import flet as ft
from UI.alert import AlertManager

class View:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK
        self.alert = AlertManager(page)
        self.controller = None

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    def load_interface(self):
        self.txt_titolo = ft.Text(value="Musei di Torino", size=38, weight=ft.FontWeight.BOLD)

        self._museo_dropdown = ft.Dropdown(
            label="Seleziona un museo",
            options=[],
            width=300,
            on_change=lambda e: self.controller.on_museo_changed(e)
        )

        self._epoca_dropdown = ft.Dropdown(
            label="Seleziona un'epoca",
            options=[],
            width=300,
            on_change=lambda e: self.controller.on_epoca_changed(e)
        )

        self._btn_mostra = ft.ElevatedButton(
            text="Mostra Artefatti",
            on_click=lambda e: self.controller.mostra_artefatti(e)
        )

        self._list_view = ft.ListView(
            expand=True,
            spacing=10,
            padding=10,
            auto_scroll=False
        )

        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

        self.page.add(
            self.toggle_cambia_tema,
            self.txt_titolo,
            ft.Divider(),
            ft.Row([self._museo_dropdown, self._epoca_dropdown], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([self._btn_mostra], alignment=ft.MainAxisAlignment.CENTER),
            ft.Container(self._list_view, expand=True, padding=10, height=400)
        )

        self.page.scroll = "adaptive"
        self.page.update()

    def cambia_tema(self, e):
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()
