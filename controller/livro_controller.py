# Função Cadastrar
# Função Pesquisar


import os
from model.livro  import Livro

class Livro_controller:
    
    file_livro = "livro.txt"
    
    def  cadastrar_livro(self, titulo, autor, ano_publicacao, isbn, categoria):
        ultimo_id = 0
        
        with open(self.file_livro, "r") as file:
            for linha in file:
                linha_objeto = Livro.from_string(linha)
                ultimo_id = max(ultimo_id, int(linha_objeto.id))  # Encontra o último id 
        
        ultimo_id = ultimo_id + 1
        livro = Livro(ultimo_id,titulo, autor, ano_publicacao, isbn, categoria)
        
        with open(self.file_livro, "a") as file:
            file.write(livro.to_string()+"\n")
        
        return "Livro registrado com sucesso!"
        
    def pesquisar_livro(self, tipo_pesquisa, descricao):
        
        if tipo_pesquisa == "titulo":
            livros = []
            with open(self.file_livro, "r") as file:
                
                for linha in file:
                    linha_objeto = Livro.from_string(linha)
                    if descricao == linha_objeto.titulo:  # Encontra a pesquisa
                        livros.append(linha_objeto)
                return livros
            
        elif tipo_pesquisa == "autor":
            livros = []
            with open(self.file_livro, "r") as file:
                
                for linha in file:
                    linha_objeto = Livro.from_string(linha)
                    if descricao == linha_objeto.autor:  # Encontra a pesquisa
                        livros.append(linha_objeto)
                return livros
            
        elif tipo_pesquisa == "categoria":
            livros = []
            with open(self.file_livro, "r") as file:
                
                for linha in file:
                    linha_objeto = Livro.from_string(linha)
                    if descricao == linha_objeto.categoria:  # Encontra a pesquisa
                        livros.append(linha_objeto)
                return livros
        
    def listar_livro(self):
        livros = []
        with open(self.file_livro, "r") as file:
            
            for linha in file:
                linha_objeto = Livro.from_string(linha)
                livros.append(linha_objeto)
            return livros