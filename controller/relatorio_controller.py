# Função Gerar Quantidade de Livros por Categoria
# Função Gerar Quantidade de empréstimo por tipo de usuário
# Função Buscar livros mais emprestados

import csv
import os
from collections import Counter
from collections import defaultdict

class ReportGenerator:
    def gerar_relatorio(self):
        # Lê os arquivos
        with open("usuario.txt", encoding="utf-8") as f:
            usuarios = {u.split(";")[0]: u.strip().split(";") for u in f if u.strip()}

        with open("livro.txt", encoding="utf-8") as f:
            livros = {l.split(";")[0]: l.strip().split(";") for l in f if l.strip()}

        with open("emprestimo.txt", encoding="utf-8") as f:
            emprestimos = [e.strip().split(";") for e in f if e.strip()]

        # Estatísticas 

        # Quantidade de livros por categoria
        livros_por_categoria = defaultdict(set)
        for livro in livros.values():
            categoria = livro[5]
            livros_por_categoria[categoria].add(livro[0])  # id do livro

        # Quantidade de empréstimos por tipo de usuário
        emprestimos_por_tipo_usuario = defaultdict(int)
        for emp in emprestimos:
            id_usuario = emp[2]
            tipo = usuarios.get(id_usuario, ["", "", "", "Desconhecido"])[3]
            emprestimos_por_tipo_usuario[tipo] += 1

        # Livros mais emprestados
        contador_livros = Counter(emp[1] for emp in emprestimos)
        livros_mais_emprestados = contador_livros.most_common(5)

        # relatório string
        relatorio = "*************** RELATÓRIO ESTATÍSTICO ***************\n\n"

        relatorio += "Quantidade de livros por categoria:\n"
        for categoria, ids in livros_por_categoria.items():
            relatorio += f" - {categoria}: {len(ids)} livros\n"

        relatorio += "\nQuantidade de empréstimos por tipo de usuário:\n"
        for tipo, qtd in emprestimos_por_tipo_usuario.items():
            relatorio += f" - {tipo}: {qtd} empréstimos\n"

        relatorio += "\nLivros mais emprestados:\n"
        for id_livro, qtd in livros_mais_emprestados:
            livro = livros.get(id_livro, ["", "Desconhecido", "Autor desconhecido"])
            relatorio += f" - {livro[1]} por {livro[2]}: {qtd} empréstimos\n"

        # Salvando em CSV
        with open("relatorio_estatistico.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            writer.writerow(["Categoria", "Qtd de Livros"])
            for categoria, ids in livros_por_categoria.items():
                writer.writerow([categoria, len(ids)])
            writer.writerow([])
            writer.writerow(["Tipo de Usuário", "Qtd de Empréstimos"])
            for tipo, qtd in emprestimos_por_tipo_usuario.items():
                writer.writerow([tipo, qtd])
            writer.writerow([])
            writer.writerow(["Livro", "Autor", "Qtd de Empréstimos"])
            for id_livro, qtd in livros_mais_emprestados:
                livro = livros.get(id_livro, ["", "Desconhecido", "Autor desconhecido"])
                writer.writerow([livro[1], livro[2], qtd])

        return relatorio
