import sqlite3


class Gestao:
    def ___init__(self, banco):
        self.conn = sqlite3.adapt
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
                "INSERT INTO estoque (produto, quantidade) VALUESS (?, ?)", (produto, quantidade))
            self.conn.commit()

    def remover_produto(self, produto, quantidade):
            cursor = self.conn.cursor()
            cursor.execute(
                "SELECT quantidade FROM estoque WHERE produto=?", (produto,))
            resultado = cursor.fetchone()
            if resultado:
                estoque_atual = resultado [0]
                if estoque_atual >= quantidade:
                    cursor.execute("UPDATE estoque SET quantidade=?",
                                (estoque_atual - quantidade, produto))
                    self.conn.commit()
                else:
                    print(f'Quantidade insuficiente de {produto} em estoque.')
            else:
                print(f'{produto} não encontrado em estoque.')

    def consultar_estoque(self, produto):
        cursor = self.conn.cursor()
        cursor.execute(
        "SELECT quantidade FROM estoque WHERE produto=?", (produto,))
        resultado = cursor.fetchone()
        if resultado:
            return resultado[0]
        else:
            return 0
    
    def listar_produtos(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT produto FROM estoque")
        produtos = cursor.fetchall()
        return [produto[0] for produto in produtos]

    