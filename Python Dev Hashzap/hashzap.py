# Título: Hashzap
# Botão: Iniciar chat
    # popup/modal/alerta
        # Título: Bem vindo ao Hashzap
        # Campo de Texto: Escreva seu nome no chat
        # Botão Entrar no Chat
            # Sumir com o Título e o Botão Inicial
            # Fechar o popup
            # Criar o chat (com a mensagem de "nome do usuario entrou no chat")
            # Embaixo do chat:
                # Campo de Texto: Digite sua mensagem
                # Botão Enviar Mensagem
                    # Vai aparecer a mensagem no chat com o nome do usuário
                    # Henrique: Opa, bão?

# Flet -> aplicativo/site/programa de computador
# pip install flet

# importar flet
import flet as ft

# criar a função principal do seu sistema
def main(pagina):
    # criar alguma coisa
    # criar o título
    titulo = ft.Text("Hashzap")
    
    def enviar_mensagem_tunel(mensagem):
        chat.controls.append(ft.Text(mensagem))
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel) # cria o tunel de comunicação
    

    titulo_janela = ft.Text("Bem vindo ao Hashzap!")
    campo_nome_usuario = ft.TextField(label="Digite seu nome de usário")

    campo_texto = ft.TextField(label="Digite sua mensagem")

    def enviar_mensagem(evento):
        mensagem = f"{campo_nome_usuario.value}: {campo_texto.value}"
    
        pagina.pubsub.send_all(mensagem) # envia uma mensagem no tunel

        campo_texto.value = ""
        pagina.update()

    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    # coluna e linha
    linha_mensagem = ft.Row([campo_texto, botao_enviar])
    chat = ft.Column()
    def entrar_chat(evento):
        # tirar o título da página
        pagina.remove(titulo)
        # tirar o botao_iniciar
        pagina.remove(botao_iniciar)
        # fechar o popup/janela
        janela.open = False
        
        # criar o chat
        pagina.add(chat)
        # adicionar a linha de mensagem
        pagina.add(linha_mensagem)

        # escrever a mensagem: usuario entrou no chat
        texto_entrou_chat = f"{campo_nome_usuario.value} entrou no chat"
        pagina.pubsub.send_all(texto_entrou_chat)

        pagina.update()

    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)

    janela = ft.AlertDialog(
        title=titulo_janela,
        content=campo_nome_usuario,
        actions=[botao_entrar]
    )

    def abrir_popup(evento):
        pagina.dialog = janela
        janela.open = True
        pagina.update()
    
    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=abrir_popup)

    # colocar essa coisa na página
    # adicionar o título na página
    pagina.add(titulo)
    pagina.add(botao_iniciar)

# executar o seu sistema
ft.app(main, view=ft.WEB_BROWSER)
# , view=ft.WEB_BROWSER