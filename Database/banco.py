import sqlite3

class Banco():
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.cursor = self.conexao.cursor()
        self.criar_tabela()

    