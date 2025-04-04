import os
from model.usuario import Usuario

class Usuario_Controller:
    def __init__(self):
        self.arquivo = "usuario.txt"  # Nome do arquivo onde os usuários serão armazenados

    def cadastrar_usuario(self, nome, email, tipo_usuario):
        """Registra um novo usuário no sistema."""
        # Verifica se o  email já está em uso
        with open(self.arquivo, "r", encoding="utf-8") as file:
            for linha in file:
                usuario = Usuario.from_string(linha)
                if email == usuario.email:
                    return "Email já cadastrado!"
                
        if not nome or not email or not tipo_usuario:
            return "Erro: Todos os campos são obrigatórios!"

        # Gerar um ID único
        novo_id = self.gerar_novo_id()

        # Criar usuário e salvar no arquivo
        novo_usuario = Usuario(novo_id, nome, email, tipo_usuario)
        with open(self.arquivo, "a", encoding="utf-8") as file:
            file.write(novo_usuario.to_string() + "\n")
        
        return f"Usuário {nome} cadastrado com sucesso! ID: {novo_id}"
    
    def logar_usuario(self, id, email):
        """Valida o login do usuário pelo ID e e-mail."""
        if not os.path.exists(self.arquivo):
            return "Nenhum usuário cadastrado ainda!"
        
        with open(self.arquivo, "r", encoding="utf-8") as file:
            for linha in file:
                usuario = Usuario.from_string(linha)
                if usuario.id == id and usuario.email == email:
                    return usuario  # Retorna o objeto Usuario se o login for bem-sucedido
        
        return "Erro: ID ou e-mail incorretos!"

    def gerar_novo_id(self):
        """Gera um novo ID baseado no maior ID existente no arquivo."""
        if not os.path.exists(self.arquivo):
            return "1"
        
        max_id = 0
        with open(self.arquivo, "r", encoding="utf-8") as file:
            for linha in file:
                usuario = Usuario.from_string(linha)
                max_id = max(max_id, int(usuario.id))

        return str(max_id + 1)