from flet import *
from appmenu import appmenu
from Foryou import section2
from Gridcard import gridscreen
from Gridcard import gridscreen2

def main(page: Page):
    def login(e):
        if not entrada_nome.value:
            entrada_nome.error_text = "preencha seu nome."
            page.update()
        if not entrada_senha.value:
            entrada_senha.error_text = "Campo Obrigatorio."
            page.update()
        else:
            nome = entrada_nome.value
            senha = entrada_senha.value
            print(f"Nome: {nome}\nSenha: {senha}")
            page.clean()
            heightscr = page.window_height
            widthscr = page.window_width
            page.spacing = 0
            page.padding = 0
            page.add(
                ResponsiveRow([
                    Container(
                        width=widthscr,
                        height=heightscr,
                        gradient=LinearGradient(
                            begin=alignment.top_left,
                            end=Alignment(0.5, 0.9),
                            colors=["#006E99", "#142733"]
                        ),
                        content=Column([
                            appmenu,
                            section2,
                            gridscreen
                        ])
                    )
                ])
            )

    page.title = "WAVE+"
    entrada_nome = TextField(label="digite seu nome")
    entrada_senha = TextField(label="digite sua senha")

    page.add(
        entrada_nome,
        entrada_senha,
        ElevatedButton("clique aqui", on_click=login)
    )

app(target=main)



