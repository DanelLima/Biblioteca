# id
# nome
# e-mail
# tipo_usuario

class Usuario:
    def __init__(self, id, nome, email, tipo_usuario):
        self._id = id # Usar underline para indicar atributo "privado"
        self._nome = nome  
        self._email = email
        self._tipo_usuario = tipo_usuario

    @property
    def id(self):
        return self._id
                
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, novo_email):
        self._email = novo_email

    @property
    def tipo_usuario(self):
        return self._tipo_usuario 

    @tipo_usuario.setter
    def tipo_usuario(self, tipo_usuario):
        self._tipo_usuario = tipo_usuario

    def to_string(self):
        # Conversão do usuário em string para salvar no txt
        return f"{self._id};{self._nome};{self._email};{self._tipo_usuario}"

    @staticmethod
    def from_string(string):
        # Cria um objeto Usuario de uma string
        id, nome, email, tipo_usuario = string.strip().split(";")
        return Usuario(id, nome, email, tipo_usuario)
