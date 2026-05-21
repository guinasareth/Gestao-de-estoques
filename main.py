# Importa o arquivo database.py.
# Assim conseguimos usar as funcoes que estao la dentro.
import database


# Funcao principal do programa.
def iniciar_programa():
    # Garante que as tabelas do banco existem antes do sistema funcionar.
    database.criar_tabelas()

    # Mensagem simples para confirmar que o programa iniciou.
    print("Sistema de gestao de estoque iniciado com sucesso!")


# Chama a funcao principal para iniciar o programa.
iniciar_programa()