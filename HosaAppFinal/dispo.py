# dispo.py
import flet as ft

def create_dispo_view(page, navigate_to):
    page.clean()
    page.update()
    def on_config_button_click(e):
        navigate_to("config")
    
    def volverHome(e):
        navigate_to("home")

# Define los elementos de la interfaz gráfica
    # tb1 = TextField(label="ID Usuario", hint_text="ID Usuario")
    # c = ft.Column(height=50)
    # tb2 = ft.Dropdown(label="Dispositivo", hint_text="Seleccionar")
    # tb3 = ft.dropdown(label="Zona ", hint_text="Cocina")
    # tb4 = ft.Dropdown(label="Dispositivo", hint_text="Sensor")
    # tb5 = ft.Dropdown(label="Zona", hint_text="Baño")
    # tb6 = ft.Dropdown(label="Dispositivo", hint_text="Camara")
    # tb7 = ft.Dropdown(label="Zona", hint_text="Dormitorio")
    # tb8 = ft.Dropdown(label="Dispositivo", hint_text="")
    # tb9 = ft.Dropdown(label="Zona", hint_text="")
    # registrar = ft.ElevatedButton(text="Guargar", on_click="")
    # salir = ft.ElevatedButton(text="Salir", on_click=volverHome)


    dd = ft.Dropdown(
        label="Color",
        hint_text="Seleccionar Color",
        options=[
            ft.dropdown.Option("Rojo"),
            ft.dropdown.Option("Azul"),
            ft.dropdown.Option("Verde")
        ],
        autofocus=True
    )
    dd2 = ft.Dropdown(
        label="Color",
        hint_text="Seleccionar Color",
        options=[
            ft.dropdown.Option("Rojo"),
            ft.dropdown.Option("Azul"),
            ft.dropdown.Option("Verde")
        ],
        autofocus=True
    )
    dd3 = ft.Dropdown(
        label="Color",
        hint_text="Seleccionar Color",
        options=[
            ft.dropdown.Option("Rojo"),
            ft.dropdown.Option("Azul"),
            ft.dropdown.Option("Verde")
        ],
        autofocus=True
    )
    dd4 = ft.Dropdown(
        label="Color",
        hint_text="Seleccionar",
        options=[
            ft.dropdown.Option("Rojo"),
            ft.dropdown.Option("Azul"),
            ft.dropdown.Option("Verde")
        ],
        autofocus=True
    )

    space = ft.Row(
        height=40
    )

    col = ft.Column(
        scroll= ft.ScrollMode.AUTO,
        controls=[
            space,
            dd,
            dd2,
            dd3,
            dd4
        ],
        spacing=20
    )

    scroll_container = ft.Container(
        content=col,
        height=800,
        expand=1,
    )
    # Agrega los elementos a la página
    page.add(scroll_container)

# ft.app(target=create_dispo_view)
