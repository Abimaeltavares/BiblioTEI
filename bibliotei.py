def main_menu():
    print("Bem-vindo ao BiblioTEI!")
    print("1. Cadastrar Livro")
    print("2. Consultar Livro")
    print("3. Emprestar Livro")
    print("4. Devolver Livro")
    print("5. Gerar Relatórios")
    print("6. Sair")

    option = input("Escolha uma opção: ")
    return option

if __name__ == "__main__":
    while True:
        option = main_menu()
        if option == '6':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print(f"Você escolheu a opção {option}. (Funcionalidade ainda não implementada)")

            livros = {}

def cadastrar_livro():
    codigo = input("Digite o código do livro: ")
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    isbn = input("Digite o ISBN do livro: ")
    editora = input("Digite a editora do livro: ")
    
    # Verifica se o código já existe
    if codigo in livros:
        print("Erro: Um livro com esse código já está cadastrado.")
        return
    
    # Cadastra o livro
    livros[codigo] = {
        'titulo': titulo,
        'autor': autor,
        'isbn': isbn,
        'editora': editora,
        'status': 'disponível'
    }
    print(f"Livro '{titulo}' cadastrado com sucesso!")

def consultar_livro():
    busca = input("Digite o título, autor ou ISBN do livro: ")
    
    resultados = [livro for livro in livros.values() if busca.lower() in livro['titulo'].lower() or
                  busca.lower() in livro['autor'].lower() or
                  busca.lower() in livro['isbn'].lower()]
    
    if not resultados:
        print("Nenhum livro encontrado.")
        return
    
    print("Livros encontrados:")
    for livro in resultados:
        print(f" - Título: {livro['titulo']}, Autor: {livro['autor']}, ISBN: {livro['isbn']}, Editora: {livro['editora']}, Status: {livro['status']}")

def main_menu():
    print("Bem-vindo ao BiblioTEI!")
    print("1. Cadastrar Livro")
    print("2. Consultar Livro")
    print("3. Emprestar Livro")
    print("4. Devolver Livro")
    print("5. Gerar Relatórios")
    print("6. Sair")

    option = input("Escolha uma opção: ")
    return option

if __name__ == "__main__":
    while True:
        option = main_menu()
        if option == '1':
            cadastrar_livro()
        elif option == '2':
            consultar_livro()
        elif option == '6':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print(f"Você escolheu a opção {option}. (Funcionalidade ainda não implementada)")