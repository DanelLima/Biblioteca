# id
# titulo
# autor
# ano_publicacao
# isbn
# categoria

class Livro:
    def __init__(self, id, titulo, autor, ano_publicacao, isbn, categoria):
        self._id = id  # Usar underline para indicar atributo "privado"
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._isbn = isbn
        self._categoria = categoria
    
    def __str__(self):
        return f"ID: {self._id} | Título: {self._titulo} | Autor: {self._autor} | Ano De Publicação: {self._ano_publicacao} | ISBN: {self._isbn} | Categoria: {self._categoria}"

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, novo_id):
        self._id = novo_id
                
    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, novo_titulo):
        self._titulo = novo_titulo

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, novo_autor):
        self._autor = novo_autor

    @property
    def ano_publicacao(self):
        return self._ano_publicacao

    @ano_publicacao.setter
    def ano_publicacao(self, novo_ano_publicacao):
        self._ano_publicacao = novo_ano_publicacao
        
    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, novo_isbn):
        self._isbn = novo_isbn
        
    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, novo_categoria):
        self._categoria = novo_categoria

    def to_string(self):
        # Conversão do livro em string para salvar no txt
        return f"{self._id};{self._titulo};{self._autor};{self._ano_publicacao};{self._isbn};{self._categoria}"

    @staticmethod
    def from_string(string):
        # Cria um objeto Livro de uma string
        id, titulo, autor, ano_publicacao, isbn, categoria = string.strip().split(";")
        return Livro(id, titulo, autor, ano_publicacao, isbn, categoria)
