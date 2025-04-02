# Função Emprestar
# Função Listar Empréstimos
# Função Devoluçâo

import os
from model.emprestimo import Emprestimo

class Emprestimo_controller:
    
    file_emprestimo = "emprestimo.txt"
    
    def emprestar(self, emprestimo):
        ultimo_id = 0
        livros_emprestados = []
        with open(self.file_emprestimo, "r") as file:
            for linha in file:
                linha_objeto = Emprestimo.from_string(linha)
                ultimo_id = max(ultimo_id, int(linha_objeto.id))  # Encontra o último id 
                if linha_objeto.situacao == "Emprestado":
                    livros_emprestados.append(linha_objeto.id_livro) 
        
        if emprestimo.id_livro in livros_emprestados:
            return "Livro já foi emprestado"
        
        ultimo_id = ultimo_id + 1   
        emprestimo.id = ultimo_id
        
        
        with open(self.file_emprestimo, "a") as file:
            file.write(emprestimo.to_string()+"\n")
        
        return "Empréstimo registrado com sucesso!"
        
    def listar_emprestimos(self):
        emprestimos = []
        with open(self.file_emprestimo, "r") as file:
            for linha in file:
                emprestimos.append(Emprestimo.from_string(linha))
        return emprestimos
    
    def  devolucao(self, id_livro):
        emprestimos = self.listar_emprestimos()

        #Procura pelo livro e atualizar a situação
        encontrado = False
        for i in range(len(emprestimos)):
            if int(emprestimos[i].id_livro) ==  int(id_livro) and emprestimos[i].situacao == "Emprestado":
                emprestimos[i].situacao = "Devolvido"
                encontrado = True
                break  

        if not encontrado:
            return f"Nenhum empréstimo encontrado para o livro {id_livro}."

        #Reescrever o arquivo atualizado
        with open(self.file_emprestimo, "w") as file:
            for i in range(len(emprestimos)):
                file.write(emprestimos[i].to_string()+"\n")
                
        return f"Livro devolvido com sucesso!"