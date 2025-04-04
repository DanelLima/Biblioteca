# A main deve incluir o login do usuário, caso não exista um login, o usuário deve criá-lo. Depois do login, terá as opções de cadastro. Teremos empréstimo e devolução. Além do usuário poder consultar seus empréstimos. Existe também a parte de salvar o relatório que terá suas respectivas opções. Toda tela deve apresentar o logout. Se ele o fizer, ele irá para o login de novo.
# O salvamento de arquivos será em .txt com separação em ;. Cada registro será lançado uma linha após a outra

import os
import sys

from controller.emprestimo_controller import Emprestimo_controller
from model.emprestimo import Emprestimo
from controller.usuario_controller import Usuario_Controller
from model.usuario import Usuario
from controller.livro_controller import Livro_controller
from model.livro import Livro
from controller.relatorio_controller import ReportGenerator
from datetime import datetime, timedelta

view_login = """

******************************************************* LOGIN ********************************************************************

Escolha uma opção:

0. Fazer cadastro

1. Encerrar a aplicação

2. Fazer login 
    
Escolha uma opção: """
    
    
view_menu = """
     
******************************************************* MENU ********************************************************************
    
1. Fazer Empréstimo
2. Devolver Livro
3. Consultar todos os Empréstimos
4. Doar um Livro
5. Pesquisar e listar Livros
6. Imprimir as estatísticas em um relatório
7. Logout
    
    """
    
acesso = ""

def main():
    
    global acesso
    
    if acesso == "":
        
        while True:
            login = input(view_login)
            
            if login == "0":
                os.system("cls")
                cadastro_usuario()
                break
                
            elif login == "1":
                os.system("cls")
                print("Aplicação encerrada!")
                sys.exit()
            
            elif login == "2":
                id = input("Digite seu id:")
                email = input("Digite seu email:")
                usuario = Usuario_Controller()
                os.system("cls")
                acesso = usuario.logar_usuario(id,email) #Retorna um objeto Usuario
                break
                
            else:
                print("Opção inválida! Tente novamente.")
            
    if acesso != "Erro: ID ou e-mail incorretos!" and acesso != "Nenhum usuário cadastrado ainda!" and acesso != "":
        while True:
            
            print(view_menu)

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
                cadastro_livro(acesso)
            elif opcao == "5":
                os.system("cls")
                pesquisar_livro()
            elif opcao == "6":
                os.system("cls")
                relatorio()
            elif opcao == "7":
                os.system("cls")
                print("Logout realizado.")
                acesso = ""
                break
            else:
                print("Opção inválida! Tente novamente.")
                
    else:
        print(acesso)
        acesso = ""
        print("Faça login para acessar!")
            
    main()
                
def cadastro_usuario():
    print('***************************************************** Cadastro ******************************************************************')
    nome = input("Digite nome:")
    email = input("Digite email:")
    tipo_usuario = input("Digite seu tipo de usuário (aluno/professor/visitante):")
    
    usuario = Usuario_Controller()
    resultado = usuario.cadastrar_usuario(nome,email,tipo_usuario)
    os.system("cls")
    print(resultado)
    print("\n\nFaça login para acessar!\n\n")
    
def cadastro_livro(acesso):
    print('***************************************************** Cadastro ******************************************************************')
    titulo = input("Digite o titulo do livro:")
    autor = input("Digite o  autor do livro:")
    ano_publicacao = input("Digite o ano de publicacao:")
    isbn = input("Digite o ISBN:")
    categoria = input("Digite a categoria:")
    
    livro = Livro_controller()
    resultado = livro.cadastrar_livro(titulo, autor, ano_publicacao, isbn, categoria)
    os.system("cls")
    print(resultado)
    
def fazer_emprestimo(acesso):
    print('***************************************************** Emprestimo ****************************************************************')
    id_livro = input("Digite o id do livro para fazer emprestimo: ")
    data_atual = datetime.now()
    data_futura = data_atual + timedelta(days=30)
    data_futura = data_futura.strftime("%d/%m/%Y")
    
    emprestimo = Emprestimo_controller()
    resultado = emprestimo.emprestar(Emprestimo(0,id_livro,acesso.id,data_futura,"Emprestado"))
    print(resultado)
    
def devolver_livro(acesso):
    print('***************************************************** Devolução ****************************************************************')
    id_livro = input("Digite o id do livro devolvido: ")
    
    emprestimo = Emprestimo_controller()
    resultado = emprestimo.devolucao(id_livro)
    print(resultado)
    
def consultar_emprestimos(acesso):
    print('********************************************** Todos os Emprestimos ************************************************************')
    
    emprestimo = Emprestimo_controller()
    emprestimos = emprestimo.listar_emprestimos()
    for i in emprestimos:
        print(i)

def pesquisar_livro():
    print('************************************************ Pesquisar livro ***************************************************************')
    
    while True:
        opcao = input("""
                      
    Selecione qual opção realizar: 
    1. Pesquisar por (1: título / 2: autor / 3: categoria)
    2. Listar todos os livros
    
                      """)

        if opcao == "1":
            opcao_pesquisa = input(""" 
                                   
            Escolha a pesquisa:
            1. título
            2. autor
            3. categoria
            
                                   """)
            
            descricao = input("Digite a pesquisa:")
            
            if opcao_pesquisa == "1":
                livro = Livro_controller()
                resultado = livro.pesquisar_livro("titulo", descricao)
                os.system("cls")
                print("Resultado da pesquisa:")
                for i in resultado:
                    print(i)
                break
                
            elif opcao_pesquisa == "2":
                livro = Livro_controller()
                resultado = livro.pesquisar_livro("autor", descricao)
                os.system("cls")
                print("Resultado da pesquisa:")
                for i in resultado:
                    print(i)
                break
            
            elif opcao_pesquisa == "3":
                livro = Livro_controller()
                resultado = livro.pesquisar_livro("categoria", descricao)
                os.system("cls")
                print("Resultado da pesquisa:")
                for i in resultado:
                    print(i)
                break
            
            else:
                print("Opção inválida! Tente novamente.")
            break
        
        elif opcao == "2":
            livro = Livro_controller()
            livros = livro.listar_livro()
            os.system("cls")
            print('********************************************* Todos os Livros **************************************************************')
            for i in livros:
                print(i)
            break
        
        else:
            print("Opção inválida! Tente novamente.")
    
    
def relatorio():
    print('************************************************ Estatísticas *****************************************************************')
    relatorio = ReportGenerator()
    resultado = relatorio.gerar_relatorio()
    print(resultado)
    print("Arquivo csv criado para relatório!")

main()

