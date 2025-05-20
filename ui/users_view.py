import flet as ft
from database import fetch_users, delete_user, update_user

def users_view(page: ft.Page, go_to_cadastro):
    users_column = ft.Column()
    search_input = ft.TextField(label="Buscar por nome", on_change=lambda e: load_users(search_input.value), width=300)

    def load_users(filter_text=""):
        users_column.controls.clear()
        for user in fetch_users():
            user_id, name, email = user
            if filter_text.lower() in name.lower():
                name_field = ft.TextField(value=name, width=150)
                email_field = ft.TextField(value=email, width=200)

                def update_user_data(e, uid=user_id, n=name_field, em=email_field):
                    update_user(uid, n.value.strip(), em.value.strip())
                    page.snack_bar = ft.SnackBar(ft.Text("Usuário atualizado!"))
                    page.snack_bar.open = True
                    page.update()

                def delete_user_data(e, uid=user_id):
                    delete_user(uid)
                    load_users(filter_text)

                row = ft.Row([
                    name_field,
                    email_field,
                    ft.IconButton(icon=ft.icons.SAVE, tooltip="Salvar", on_click=update_user_data),
                    ft.IconButton(icon=ft.icons.DELETE, tooltip="Excluir", on_click=delete_user_data)
                ])
                users_column.controls.append(row)
        page.update()

    return ft.View(
        "/usuarios",
        [
            ft.Text("Lista de Usuários", size=24, weight="bold"),
            ft.OutlinedButton(text="Voltar ao cadastro", on_click=lambda e: go_to_cadastro()),
            ft.Divider(),
            search_input,
            users_column
        ],
        on_view_pop=lambda e: load_users()  
    )
