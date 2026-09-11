from .terminal import clear, pausa

def menu_cadastrar():
    clear()
    print("\n--- Menu de Cadastro ---")
    print("1. Navegador")
    print("2. Pasta")
    print("3. Programa")
    print("4. Site")
    print("0. Voltar")
    return input("Escolha uma opção: ")

def menu_excluir():
    clear()
    print("\n--- Menu de Exclusão ---")
    print("1. Excluir Pasta")
    print("2. Excluir Programa")
    print("3. Excluir Site")
    print("0. Voltar")
    return input("Escolha uma opção: ")

def menu_editar():
    clear()
    print("\n--- Menu de Edição ---")
    print("1. Editar Pasta")
    print("2. Editar Programa")
    print("3. Editar Site")
    print("0. Voltar")
    return input("Escolha uma opção: ")

def menu_listar():
    clear()
    print("\n--- Menu de Listagem ---")
    print("1. Listar Pastas")
    print("2. Listar Programas")
    print("3. Listar Sites")
    print("4. Listar Navegadores")
    print("0. Voltar")
    return input("Escolha uma opção: ")

def menu_navegador():
    clear()
    print("\n--- Menu de Navegadores ---")
    print("1. Cadastrar navegador")
    print("2. Definir navegador padrão")
    print("3. Escanear navegadores instalados no sistema")
    print("4. Listar navegadores cadastrados")
    print("0. Voltar")
    return input("Escolha uma opção: ")
