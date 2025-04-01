# A main deve incluir o login do usuário, caso não exista um login, o usuário deve criá-lo. Depois do login, terá as opções de cadastro. Teremos empréstimo e devolução. Além do usuário poder consultar seus empréstimos. Existe também a parte de salvar o relatório que terá suas respectivas opções. Toda tela deve apresentar o logout. Se ele o fizer, ele irá para o login de novo.
# O salvamento de arquivos será em .txt com separação em ;. Cada registro será lançado uma linha após a outra

import os
import sys

from controller.emprestimo_controller import Emprestimo_controller
from model.emprestimo import Emprestimo
from controller.usuario_controller import Usuario_controller
from model.usuario import Usuario
from controller.livro_controller import Livro_controller
from model.livro import Livro
from controller.relatorio_controller import Relatorio_controller

view_login = """

    ******************************************************* LOGIN ********************************************************************
    
     Digite seu ID e digite seu email sepados por espaço para fazer login:

     Caso não tenha cadastro digite 0 para cadastrar:
     
     Caso queira encerrar a aplicação digite 1 para finalizar: 
     
     """
    
    
view_menu = """
     
    ******************************************************* MENU ********************************************************************
    
    1. Fazer Empréstimo
    2. Devolver Livro
    3. Consultar Meus Empréstimos
    4. Doar um Livro
    5. Pesquisar e listar Livros
    6. Imprimir um relatório
    7. Logout
    
    """
    

def main():
    print(view_login)
    login = input()
    
    os.system("cls")
    
    if login == "0":
        cadastro_usuario()
        
    elif login == "1":
        print("Aplicação encerrada!")
        sys.exit()
        
    else:
        id, email = login.split()
        
    usuario = Usuario_controller()
    acesso = usuario.logar_usuario(id,email) #Retorna um objeto Usuario
    
    while True:
        
        view_menu()

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            os.system("cls")
            fazer_emprestimo(acesso)
        elif opcao == "2":
            os.system("cls")
            devolver_livro(acesso)
        elif opcao == "3":
            os.system("cls")
            consultar_emprestimos(acesso)
        elif opcao == "4":
            os.system("cls")
            cadastrar_livro(acesso)
        elif opcao == "5":
            os.system("cls")
            pesquisar_livro()
        elif opcao == "6":
            os.system("cls")
            escolher_relatorio()
        elif opcao == "7":
            print("Logout realizado.")
            acesso = ""
            break
        else:
            print("Opção inválida! Tente novamente.")
            
    main()
                
def cadastro_usuario():
    print('***************************************************** Cadastro ******************************************************************')
    nome = input("Digite nome:")
    email = input("Digite email:")
    tipo_usuario = input("Digite seu tipo de usuário (aluno/professor/visitante):")
    resultado = cadastrar_usuario(nome,email,tipo_usuario)
    os.system("cls")
    print("\n\nFaça login para acessar!\n\n")
    
def cadastro_livro(acesso):
    print('***************************************************** Cadastro ******************************************************************')
    titulo = input("Digite o titulo do livro:")
    autor = input("Digite o  autor do livro:")
    ano_publicacao = input("Digite o ano de publicacao:")
    isbn = input("Digite o ISBN:")
    categoria = input("Digite a categoria:")
    resultado = cadastrar_livro(titulo, autor, ano_publicacao, isbn, categoria)
    os.system("cls")
    print("\n\nFaça login para acessar!\n\n")
    
# fazer_emprestimo(acesso)
# devolver_livro(acesso)
# consultar_emprestimos(acesso)
# pesquisar_livro()
# escolher_relatorio()


main()

# emprestimo = Emprestimo_controller()
# emprestar = emprestimo.emprestar(Emprestimo(0,1,3,"26/06/2025","Emprestado"))

# print(emprestar)

# emprestimos = emprestimo.listar_emprestimos()

# for i in emprestimos:
#     print(i)
    
# emprestimo.devolucao(2)