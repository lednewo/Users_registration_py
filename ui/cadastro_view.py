import flet as ft
from database import insert_user

def cadastro_view(page: ft.Page, go_to_users):
    name_input = ft.TextField(label="Nome", width=300)
    email_input = ft.TextField(label="Email", width=300)
    password_input = ft.TextField(label="Senha", password=True, can_reveal_password=True, width=300)

    message = ft.Text(color=ft.colors.RED)

    def register_user(e):
        if not name_input.value.strip() or not email_input.value.strip() or not password_input.value.strip():
            message.value = "Preencha todos os campos."
        elif "@" not in email_input.value or "." not in email_input.value:
            message.value = "Email inválido."
        elif len(password_input.value) < 6:
            message.value = "A senha deve ter no mínimo 6 caracteres."
        else:
            try:
                insert_user(name_input.value.strip(), email_input.value.strip(), password_input.value)
                message.value = "✅ Usuário cadastrado com sucesso!"
                message.color = ft.colors.GREEN
                name_input.value = ""
                email_input.value = ""
                password_input.value = ""
            except Exception as err:
                message.value = f"Erro: {str(err)}"
                message.color = ft.colors.RED
        page.update()

    return ft.View(
        "/cadastro",
        [
            ft.Text("Cadastro de Usuários", size=24, weight="bold"),
            name_input,
            email_input,
            password_input,
            ft.Row([
                ft.ElevatedButton(text="Cadastrar", on_click=register_user),
                ft.OutlinedButton(text="Ver usuários", on_click=lambda e: go_to_users()),
            ]),
            message
        ],
    )
