import database


database.criar_tabelas()

database.cadastrar_produto(
    nome = 'Mouse',
    categoria = 'Perifericos',
    preco = 50.00,
    quantidade_inicial = 10,
    especificacoes = 'Mouse USB com fio' 
)