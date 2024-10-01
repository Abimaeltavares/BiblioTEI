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