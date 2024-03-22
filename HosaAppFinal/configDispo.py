import flet as ft

def create_configDispo_view(page, navigate_to):
    page.clean()
    page.update()
    page.add(ft.Text("Bienvenido a configuracion del dispositivo"))

    page.app(ft.SegmentedButton("COLOR"))

