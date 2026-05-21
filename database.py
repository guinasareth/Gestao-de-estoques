# Importa a biblioteca sqlite3.
# Ela ja vem com o Python e permite criar/usar banco de dados SQLite.
import sqlite3

# Importa Path, que ajuda a trabalhar com caminhos de arquivos e pastas.
from pathlib import Path
from datetime import datetime


# __file__ representa este arquivo atual: database.py
# resolve() pega o caminho completo do arquivo
# parent pega a pasta onde o arquivo esta
BASE_DIR = Path(__file__).resolve().parent

# Define o caminho do banco de dados.
# O arquivo estoque.db sera criado dentro da pasta do projeto.
DB_PATH = BASE_DIR / "estoque.db"


# Funcao que abre a conexao com o banco de dados.
def conectar():
    # Se o arquivo estoque.db nao existir, o SQLite cria automaticamente.
    conexao = sqlite3.connect(DB_PATH)

    # Devolve a conexao para quem chamou a funcao.
    return conexao


# Funcao que cria as tabelas do sistema.
def criar_tabelas():
    # Abre a conexao com o banco.
    conexao = conectar()

    # Cria o cursor.
    # O cursor e quem executa comandos SQL no banco.
    cursor = conexao.cursor()

    # Cria a tabela de produtos, se ela ainda nao existir.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            categoria TEXT NOT NULL,
            preco REAL NOT NULL,
            quantidade_inicial INTEGER NOT NULL,
            quantidade_atual INTEGER NOT NULL,
            especificacoes TEXT
        )
    """)

    # Cria a tabela de movimentacoes, se ela ainda nao existir.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS movimentacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            produto_id INTEGER NOT NULL,
            tipo TEXT NOT NULL,
            motivo TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            data TEXT NOT NULL,
            FOREIGN KEY (produto_id) REFERENCES produtos (id)
        )
    """)

    # Salva as alteracoes feitas no banco.
    conexao.commit()

    # Fecha a conexao para nao deixar o banco preso.
    conexao.close()

def cadastrar_produto(nome, categoria, preco, quantidade_inicial, especificacoes):
    # Guarda a data e hora atual em formato de texto.
    # Isso pode ser usado para os relatórios depois!
    data_cadastro = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # Abre a conexao com o banco.
    conexao = conectar()

    # Cria o cursor para executar comandos SQL.
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO produtos (
            nome,
            categoria,
            preco,
            quantidade_inicial,
            quantidade_atual,
            especificacoes
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        nome,
        categoria,
        preco,
        quantidade_inicial,
        quantidade_inicial,
        especificacoes
    ))
    

    # Salva o cadastro no banco
    conexao.commit()

    # Fecha a conexao
    conexao.close()
  
# Mostra uma mensagem para confirmar.
print('Produto cadastrado com sucesso!')


# Este bloco so roda quando executamos:
# python database.py
#
# Se outro arquivo importar database.py, esse bloco nao roda automaticamente.
if __name__ == "__main__":
    criar_tabelas()
    print("Banco de dados criado com sucesso!")