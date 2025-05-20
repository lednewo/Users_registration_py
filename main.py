import flet as ft
from database import create_table
from ui.cadastro_view import cadastro_view
from ui.users_view import users_view

def main(page: ft.Page):
    create_table()

    def go_to_cadastro():
        page.views.clear()
        page.views.append(cadastro_view(page, go_to_users))
        page.update()

    def go_to_users():
        page.views.clear()
        page.views.append(users_view(page, go_to_cadastro))
        page.update()

    go_to_cadastro()

if __name__ == "__main__":
    ft.app(target=main)
