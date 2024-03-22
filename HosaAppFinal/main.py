# main.py
from http.server import BaseHTTPRequestHandler, HTTPServer
import flet as ft
from login import create_login_view
from home import create_home_view
from dispo import create_dispo_view
from config import create_config_view
from registrar import create_registrar_view
from configDispo import create_configDispo_view
from reportes import create_reportes_view

def main(page: ft.Page):

    def navigate_to(view_name):
        if view_name == "home":
            create_home_view(page, navigate_to)
        elif view_name == "login":
            create_login_view(page, navigate_to)
        elif view_name == "dispo":
            create_dispo_view(page, navigate_to)
        elif view_name == "config":
            create_config_view(page, navigate_to)
        elif view_name == "registrar":
            create_registrar_view(page, navigate_to)
        elif view_name == "configDispo":
            create_configDispo_view(page, navigate_to)
        elif view_name == "reportes":
            create_reportes_view(page, navigate_to)
        
        page.update()

    navigate_to("login")

ft.app(target=main, assets_dir="assets")
