# Função Gerar Quantidade de Livros por Categoria
# Função Gerar Quantidade de empréstimo por tipo de usuário
# Função Buscar livros mais emprestados

import csv
from collections import Counter

class ReportGenerator:
    def __init__(self, book_model, user_model, loan_model):
        self.book_model = book_model
        self.user_model = user_model
        self.loan_model = loan_model
    
    def generate_book_category_report(self, file_path="book_category_report.csv"):
        categories = [book["categoria"] for book in self.book_model.get_all_books()]
        category_count = Counter(categories)
        
        with open(file_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Categoria", "Quantidade"])
            for category, count in category_count.items():
                writer.writerow([category, count])
    
    def generate_loan_by_user_type_report(self, file_path="loan_by_user_type.txt"):
        user_types = [self.user_model.get_user(loan.id_usuario).tipo for loan in self.loan_model.get_all_loans()]
        type_count = Counter(user_types)
        
        with open(file_path, "w", encoding="utf-8") as file:
            file.write("Relatório de Empréstimos por Tipo de Usuário\n")
            file.write("======================================\n")
            for user_type, count in type_count.items():
                file.write(f"{user_type}: {count} empréstimos\n")
    
    def generate_most_loaned_books_report(self, file_path="most_loaned_books.csv"):
        book_ids = [loan.id_livro for loan in self.loan_model.get_all_loans()]
        book_count = Counter(book_ids)
        
        with open(file_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Título", "Autor", "ISBN", "Quantidade de Empréstimos"])
            for book_id, count in book_count.most_common():
                book = self.book_model.get_book(book_id)
                writer.writerow([book["titulo"], book["autor"], book["isbn"], count])
    
    def generate_all_reports(self):
        self.generate_book_category_report()
        self.generate_loan_by_user_type_report()
        self.generate_most_loaned_books_report()
        print("Relatórios gerados com sucesso!")