# A main deve incluir o login do usuário, caso não exista um login, o usuário deve criá-lo. Depois do login, terá as opções de cadastro. Teremos empréstimo e devolução. Além do usuário poder consultar seus empréstimos. Existe também a parte de salvar o relatório que terá suas respectivas opções. Toda tela deve apresentar o logout. Se ele o fizer, ele irá para o login de novo.
# O salvamento de arquivos será em .txt com separação em ;. Cada registro será lançado uma linha após a outra


from controller.emprestimo_controller import Emprestimo_controller
from model.emprestimo import Emprestimo


emprestimo = Emprestimo_controller()
emprestar = emprestimo.emprestar(Emprestimo(0,1,3,"26/06/2025","Emprestado"))

print(emprestar)

emprestimos = emprestimo.listar_emprestimos()

for i in emprestimos:
    print(i)
    
emprestimo.devolucao(2)