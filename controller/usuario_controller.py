# Função Cadastro de Usuário
# Função Login
# Função Desconectar do Usuário

#import os
#from model.usuario import Usuario

#class Usuario_controller:
    
#    def cadastrar_usuario(nome,email,tipo_usuario):
#        0
        
#    def logar_usuario(id,email):
#        0

class UsuarioController: def init(self): self.usuarios = []  
# Lista para armazenar os usuários self.emails_cadastrados = set()  
# Conjunto para evitar emails duplicados self.id_counter = 1  
# Contador para gerar IDs únicos

def cadastrar_usuario(self, nome, email, tipo_usuario):
    tipos_validos = {"aluno", "professor", "visitante"}
    
    if tipo_usuario.lower() not in tipos_validos:
        return "Erro: Tipo de usuário inválido. Escolha entre aluno, professor ou visitante."
    
    if email in self.emails_cadastrados:
        return "Erro: Email já cadastrado."
    
    usuario = {
        "id": self.id_counter,
        "nome": nome,
        "email": email,
        "tipo": tipo_usuario.lower()
    }
    
    self.usuarios.append(usuario)
    self.emails_cadastrados.add(email)
    self.id_counter += 1
    
    return f"Usuário {nome} cadastrado com sucesso!"

def logar_usuario(self, id, email):
    try:
        id = int(id)  # Converter ID para inteiro
    except ValueError:
        return "Erro: ID inválido."
    
    for usuario in self.usuarios:
        if usuario["id"] == id and usuario["email"] == email:
            return usuario  # Retorna o objeto usuário
    return None  # Retorna None se não encontrar

def desconectar_usuario(self, id):
    for usuario in self.usuarios:
        if usuario["id"] == id:
            return f"Usuário {usuario['nome']} desconectado com sucesso!"
    return "Erro: Usuário não encontrado."