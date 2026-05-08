import sqlite3


class Gestao:
    def __init__(self, banco):
        self.conn = sqlite3.connect(banco)
        self.criar_tabela_estoque()

    def criar_tabela_estoque(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS estoque (
                id INTEGER PRIMARY KEY,
                produto TEXT,
                quantidade INTEGER
            )
        ''')
        self.conn.commit()

    def adicionar_produto(self, produto, quantidade):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO estoque (produto, quantidade) VALUES (?, ?)",
            (produto, quantidade)
        )
        self.conn.commit()
        print(f'{produto} adicionado ao estoque.')

    def remover_produto(self, produto, quantidade):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT quantidade FROM estoque WHERE produto=?",
            (produto,)
        )
        resultado = cursor.fetchone()

        if resultado:
            estoque_atual = resultado[0]

            if estoque_atual >= quantidade:
                cursor.execute(
                    "UPDATE estoque SET quantidade=? WHERE produto=?",
                    (estoque_atual - quantidade, produto)
                )
                self.conn.commit()
                print(f'{quantidade} unidade(s) de {produto} removida(s).')
            else:
                print(f'Quantidade insuficiente de {produto} em estoque.')
        else:
            print(f'{produto} não encontrado em estoque.')

    def consultar_estoque(self, produto):
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT quantidade FROM estoque WHERE produto=?",
            (produto,)
        )
        resultado = cursor.fetchone()

        if resultado:
            return resultado[0]
        return 0

    def listar_produtos(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT produto, quantidade FROM estoque")
        produtos = cursor.fetchall()
        return produtos

    def fechar_conexao(self):
        self.conn.close()


def menu():
    sistema = Gestao("estoque.db")

    while True:
        print("\n===== SISTEMA DE ESTOQUE =====")
        print("1 - Adicionar produto")
        print("2 - Remover produto")
        print("3 - Consultar estoque")
        print("4 - Listar produtos")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            produto = input("Nome do produto: ")
            quantidade = int(input("Quantidade: "))
            sistema.adicionar_produto(produto, quantidade)

        elif opcao == "2":
            produto = input("Nome do produto: ")
            quantidade = int(input("Quantidade para remover: "))
            sistema.remover_produto(produto, quantidade)

        elif opcao == "3":
            produto = input("Nome do produto: ")
            quantidade = sistema.consultar_estoque(produto)
            print(f'Quantidade de {produto} em estoque: {quantidade}')

        elif opcao == "4":
            produtos = sistema.listar_produtos()

            if produtos:
                print("\nProdutos em estoque:")
                for produto, quantidade in produtos:
                    print(f'{produto}: {quantidade}')
            else:
                print("Nenhum produto cadastrado.")

        elif opcao == "5":
            sistema.fechar_conexao()
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida. Tente novamente.")


menu()
