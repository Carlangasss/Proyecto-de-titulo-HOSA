import flet as ft

def colores(page : ft.Page):

    color1 = ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=[ft.colors.ORANGE, ft.colors.YELLOW],
            )
    color2 = ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=["#00CED1","#E0FFFF"],
            )
    color3 = ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=["#ADD8E6", "#F5FFFA"],
            )
    color4 = ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=["#F4A460", "#FFF5EE"],
            )
    color5 = ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=["#F5F5F5", "#FFFAFA"],
            )

    a =ft.Container(
        content= ft.Text("PRUEBA DE COLOR"),
        margin=10,
        padding=20,
        width=400,
        height=80,
        border_radius=20,
        ink=True,
        gradient=color1,
        on_click="",
        opacity=1
    )
    b =ft.Container(
        content= ft.Text("PRUEBA DE COLOR"),
        margin=10,
        padding=20,
        width=400,
        height=80,
        border_radius=20,
        ink=True,
        gradient=color2,
        on_click="",
        opacity=1
    )
    c =ft.Container(
        content= ft.Text("PRUEBA DE COLOR"),
        margin=10,
        padding=20,
        width=400,
        height=80,
        border_radius=20,
        ink=True,
        gradient=color3,
        on_click="",
        opacity=1
    )
    d =ft.Container(
        content= ft.Text("PRUEBA DE COLOR"),
        margin=10,
        padding=20,
        width=400,
        height=80,
        border_radius=20,
        ink=True,
        gradient=color4,
        on_click="",
        opacity=1
    )
    e =ft.Container(
        content= ft.Text("PRUEBA DE COLOR"),
        margin=10,
        padding=20,
        width=400,
        height=80,
        border_radius=20,
        ink=True,
        gradient=color5,
        on_click="",
        opacity=1
    )

    page.add(a,b,c,d,e)



ft.app(target=colores)