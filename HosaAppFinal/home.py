# home.py
import logging
import flet as ft
from tuya_connector import TuyaOpenAPI, TUYA_LOGGER
import mysql.connector

#Conección con la api TUYA
ACCESS_ID = "xje5t5vu8cqcvvhadw78"
ACCESS_KEY = "68b3b2f2e6984ba4bf06be90a7ad78fa"
API_ENDPOINT = "https://openapi.tuyaus.com"

# TUYA_LOGGER.setLevel(logging.DEBUG)
openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
openapi.connect()



#Dispositivos Id
LUZ_1 ="ebb63196d8a8ff3e05buvw"

response = openapi.get('/v1.0/devices/{}'.format(LUZ_1))
data = response

def create_home_view(page :ft.Page, navigate_to):
    
    #configuración página
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.fonts = {
        "Rubik" : "assets/fonts/RubikDoodleShadow-Regular.ttf",
        "Dosis" : "assets/fonts/Dosis-VariableFont_wght.ttf"
    }
    
    def ConfigDispo(e):
        page.clean()
        page.update()
        navigate_to("configDispo")

    def salirApp(e):
        page.clean()
        page.update()
        navigate_to("login")

    def menuDispo(e):
        page.clean()
        page.update()
        navigate_to("dispo")
    
    def reportes(e):
        page.clean()
        page.update()
        navigate_to("reportes")
    
    def inicio(e):
        page.clean()
        page.update()
        navigate_to("home")

    tituloHome = ft.Text(
        spans=[
            ft.TextSpan(
                "H O S A",
                ft.TextStyle(
                    size=40,
                    weight=ft.FontWeight.BOLD,
                    font_family="Rubik",
                    color="#FF8C00"
                ),
                on_click=inicio
            )
        ],
    )

    columnMenu = ft.Column(
        spacing=15,
        controls=[
            ft.TextButton("Menu Dispositivos",on_click=menuDispo, icon=ft.icons.PERM_DEVICE_INFO_OUTLINED, width=300, height=80),
            ft.TextButton("Zonas",on_click=salirApp, icon=ft.icons.OTHER_HOUSES_OUTLINED, width=300, height=80),
            ft.TextButton("Reportes",on_click=reportes, icon=ft.icons.FACT_CHECK_OUTLINED, width=300, height=80),
            ft.TextButton("HOSA",on_click=salirApp, icon=ft.icons.OFFLINE_BOLT_OUTLINED, width=300, height=80),
            ft.TextButton("Configuracion",on_click=salirApp, icon=ft.icons.SETTINGS_OUTLINED, width=300, height=80),
            # ft.TextButton("usuarios",on_click=on_dispo_button_click, icon=ft.icons.SUPERVISED_USER_CIRCLE_OUTLINED, width=300, height=80),
            ft.TextButton("Deslogearse",on_click=salirApp, icon=ft.icons.LOGOUT_OUTLINED, width=300, height=80)
        ],
    )

    page.drawer = ft.NavigationDrawer(
        controls=[
            ft.Container(height=20),
            ft.Row(
                width=100,
                height=80,
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Text("Menu",size=24,text_align=ft.TextAlign.CENTER),
                ]
            ),
            ft.Divider(thickness=1),
            ft.Container(height=5),
            columnMenu
        ],
    )
   
    page.appbar = ft.AppBar(
        leading_width=50,
        center_title=True,
        title=tituloHome,
        bgcolor="#008B8B",
    )

    
    #Contenido

    flag = True

    def estadoLuz(e):
        nonlocal flag
        flag = not flag
        commands = {'commands': [{'code': 'switch_led', 'value': flag}]}
        openapi.post('/v1.0/iot-03/devices/{}/commands'.format(LUZ_1), commands)
        page.update()

    items = [] 
    items.append(ft.Icon(name=ft.icons.LIGHTBULB, color=ft.colors.AMBER, size=25))
    items.append(ft.Text(data['result']['name'],size=15, color="#0F1111"))

    row = ft.Row(controls=items,spacing=20)

    row2 = ft.Row(controls=[
        ft.Icon(name=ft.icons.LIGHTBULB, color=ft.colors.AMBER, size=25),
        ft.Text("Luz Pieza 3",size=15, color="#0F1111")
    ],spacing=20)
    row3 = ft.Row(controls=[
        ft.Icon(name=ft.icons.WIND_POWER_SHARP, color=ft.colors.AMBER, size=25),
        ft.Text("Aire Ac Dormi",size=15, color="#0F1111")
    ],spacing=20)
    row4 = ft.Row(controls=[
        ft.Icon(name=ft.icons.CAMERA_INDOOR, color=ft.colors.AMBER, size=25),
        ft.Text("Camara Comedor",size=15, color="#0F1111")
    ],spacing=20)
    row5 = ft.Row(controls=[
        ft.Icon(name=ft.icons.LIGHTBULB, color=ft.colors.AMBER, size=25),
        ft.Text("Luz Comedor",size=15, color="#0F1111")
    ],spacing=20)

    wd = 290
    ht = 80

    tablaDispo = ft.Container(
        content= row,
        margin=10,
        padding=20,
        width=wd,
        height=ht,
        border_radius=20,
        ink=True,
        bgcolor="#DEF1FF",
        on_click=estadoLuz,
    )
    tablaDispo2 = ft.Container(
        content= row2,
        margin=10,
        padding=20,
        width=wd,
        height=ht,
        border_radius=20,
        ink=True,
        bgcolor="#DEF1FF",
        on_click=estadoLuz,
    )
    tablaDispo3 = ft.Container(
        content= row3,
        margin=10,
        padding=20,
        width=wd,
        height=ht,
        border_radius=20,
        ink=True,
        bgcolor="#DEF1FF",
        on_click=estadoLuz,
    )
    tablaDispo4 = ft.Container(
        content= row4,
        margin=10,
        padding=20,
        width=wd,
        height=ht,
        border_radius=20,
        ink=True,
        bgcolor="#DEF1FF",
        on_click=estadoLuz,
    )
    tablaDispo5 = ft.Container(
        content= row5,
        margin=10,
        padding=20,
        width=wd,
        height=ht,
        border_radius=20,
        ink=True,
        bgcolor="#DEF1FF",
        on_click=estadoLuz,
    )

#

    tablaDispoRow = ft.Container(
        content= ft.Row(
            controls=[ft.Icon(name=ft.icons.SETTINGS, color=ft.colors.AMBER, size=25)],
            alignment= ft.MainAxisAlignment.CENTER
        ),
        width=60,
        height=60,
        border_radius=20,
        ink=True,
        on_click=ConfigDispo,
        alignment=ft.alignment.center
    )

    bt1 = ft.Row(
        controls=[tablaDispo, tablaDispoRow],
        spacing=3
    )
    bt2 = ft.Row(
        controls=[tablaDispo2, tablaDispoRow],
        spacing=3
    )
    bt3 = ft.Row(
        controls=[tablaDispo3, tablaDispoRow],
        spacing=3
    )
    bt4 = ft.Row(
        controls=[tablaDispo4, tablaDispoRow],
        spacing=3
    )
    bt5 = ft.Row(
        controls=[tablaDispo5, tablaDispoRow],
        spacing=3
    )

    page.add(bt1, bt2, bt3, bt4, bt5)
