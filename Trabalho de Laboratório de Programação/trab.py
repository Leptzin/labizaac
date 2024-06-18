class Livro:
    def __init__(self, titulo, autor, ano, genero, isbn):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.genero = genero
        self.isbn = isbn

class Membro:
    def __init__(self, nome, id_membro, data_nascimento, endereco):
        self.nome = nome
        self.id_membro = id_membro
        self.data_nascimento = data_nascimento
        self.endereco = endereco

class Emprestimo:
    def __init__(self, livro, membro, data_emprestimo, data_devolucao_prevista):
        self.livro = livro
        self.membro = membro
        self.data_emprestimo = data_emprestimo
        self.data_devolucao_prevista = data_devolucao_prevista

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.membros = []
        self.emprestimos = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def remover_livro(self, livro):
        self.livros.remove(livro)

    def buscar_livro_por_isbn(self, isbn):
        for livro in self.livros:
            if livro.isbn == isbn:
                return livro

    # Métodos para Membros
    def adicionar_membro(self, membro):
        self.membros.append(membro)

    def remover_membro(self, membro):
        self.membros.remove(membro)

    def buscar_membro_por_id(self, id_membro):
        for membro in self.membros:
            if membro.id_membro == id_membro:
                return membro

    # Métodos para Empréstimos
    def adicionar_emprestimo(self, emprestimo):
        self.emprestimos.append(emprestimo)

    def remover_emprestimo(self, emprestimo):
        self.emprestimos.remove(emprestimo)

    def buscar_emprestimo_por_isbn(self, isbn):
        for emprestimo in self.emprestimos:
            if emprestimo.livro.isbn == isbn:
                return emprestimo

# Exemplo de uso:
biblioteca = Biblioteca()
livro1 = Livro("Livro A", "Autor A", 2020, "Ficção", "1234567890")
membro1 = Membro("João", "001", "01/01/1990", "Endereço A")
emprestimo1 = Emprestimo(livro1, membro1, "18/06/2024", "25/06/2024")

biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_membro(membro1)
biblioteca.adicionar_emprestimo(emprestimo1)
