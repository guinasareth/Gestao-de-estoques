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

            