from .listas import navegadores_padroes, sites, pastas, programas
from .modulos.navegador_padrao import (
    cadastrar_navegador_padrao,
    definir_navegador_padrao,
    scanear_navegadores,
    listar_navegadores,
)
from .modulos.sites import abrir_site, cadastrar_sites, abrir_link, excluir_site, editar_site, listar_sites
from .modulos.pastas import (
    abrir_pasta,
    cadastrar_pastas,
    excluir_pasta,
    editar_pasta,
    listar_pastas,
    limpar as limpar_pasta,
)
from .modulos.programas import cadastrar_programas, abrir_programa, excluir_programa, editar_programa, listar_programas
from .terminal import clear, pausa, sair
from .menu import menu_cadastrar, menu_excluir, menu_editar, menu_listar, menu_navegador
from .banco import salvar
from .validacao import normalizar_codigo


def cadastrar():
    while True:
        op = menu_cadastrar()
        match op:
            case "0":
                break
            case "1":
                cadastrar_navegador_padrao()
            case "2":
                cadastrar_pastas()
            case "3":
                cadastrar_programas()
            case "4":
                cadastrar_sites()
            case _:
                print("Opção não existente. Tente novamente.")

def abrir(codigo):
    codigo = normalizar_codigo(codigo)
    if codigo in sites:
        abrir_site(codigo)
    elif codigo in programas:
        abrir_programa(codigo)
    elif codigo in pastas:
        abrir_pasta(codigo)
    else:
        print(f"Nenhum item encontrado com o código '{codigo}'.")

def excluir(alvo=None):
    # Se o usuário digitou um alvo (ex: "excluir programa", "excluir site", "excluir pasta")
    if alvo:
        alvo = normalizar_codigo(alvo)
        
        if alvo in ("programa", "programas"):
            excluir_programa()
            return
        elif alvo in ("site", "sites"):
            excluir_site()
            return
        elif alvo in ("pasta", "pastas"):
            excluir_pasta()
            return
        
        # Se digitou algo como "excluir g1", tenta buscar diretamente nos dicionários pelo código
        if alvo in sites:
            del sites[alvo]
            salvar()
            print(f"Site '{alvo}' excluído com sucesso!")
            return
        elif alvo in programas:
            del programas[alvo]
            salvar()
            print(f"Programa '{alvo}' excluído com sucesso!")
            return
        elif alvo in pastas:
            del pastas[alvo]
            salvar()
            print(f"Pasta '{alvo}' excluída com sucesso!")
            return

    # Se não passou argumento ou não encontrou o código direto, mostra o menu interativo
    clear()
    op = menu_excluir()

    match op:
        case "0":
            return
        case "1":
            excluir_pasta()
        case "2":
            excluir_programa()
        case "3":
            excluir_site()
        case _:
            print("Opção inexistente.")

def comandos():
    clear()
    print("\n--- Comandos Disponíveis ---")
    print("abrir {código}: para abrir programas, pastas ou sites (ex: abrir g1).")
    print("site {link}: para abrir um link direto no navegador padrão, sem cadastrar (ex: site google.com).")
    print("cadastrar: para cadastrar programa, pasta ou site.")
    print("editar: para editar programas, pastas ou sites.")
    print("excluir: para excluir programas, pastas ou sites.")
    print("listar [pastas|programas|sites|navegadores]: para listar itens cadastrados.")
    print("limpar {código da pasta}: para apagar todo o conteúdo de uma pasta cadastrada.")
    print("navegador: para cadastrar, definir, escanear ou listar navegadores.")
    print("fechar: para fechar o programa.\n")

    pausa()

def listar(alvo=None):
    if alvo:
        alvo = normalizar_codigo(alvo)

        if alvo in ("programa", "programas"):
            listar_programas()
            return
        elif alvo in ("site", "sites"):
            listar_sites()
            return
        elif alvo in ("pasta", "pastas"):
            listar_pastas()
            return
        elif alvo in ("navegador", "navegadores"):
            listar_navegadores()
            return

    clear()
    op = menu_listar()

    match op:
        case "0":
            return
        case "1":
            listar_pastas()
        case "2":
            listar_programas()
        case "3":
            listar_sites()
        case "4":
            listar_navegadores()
        case _:
            print("Opção inexistente.")
            pausa()

def navegador():
    while True:
        op = menu_navegador()
        match op:
            case "0":
                break
            case "1":
                cadastrar_navegador_padrao()
            case "2":
                definir_navegador_padrao()
                pausa()
            case "3":
                scanear_navegadores()
            case "4":
                listar_navegadores()
            case _:
                print("Opção não existente. Tente novamente.")
                pausa()

def editar(alvo=None):
    # Se o usuário digitou um alvo (ex: "excluir programa", "excluir site", "excluir pasta")
    if alvo:
        alvo = normalizar_codigo(alvo)
        
        if alvo in ("programa", "programas"):
            editar_programa()
            return
        elif alvo in ("site", "sites"):
            editar_site()
            return
        elif alvo in ("pasta", "pastas"):
            editar_pasta()
            return

    # Se não passou argumento ou não encontrou o código direto, mostra o menu interativo
    clear()
    op = menu_editar()

    match op:
        case "0":
            return
        case "1":
            editar_pasta()
        case "2":
            editar_programa()
        case "3":
            editar_site()
        case _:
            print("Opção inexistente.")
            pausa()

def tela_principal():
    while True:
        clear()
        print("Bem-vindo! Digite 'comandos' para ver as opções.")
        entrada = input("\nDigite um comando: ").strip()
        partes = entrada.split(maxsplit=1)
        comando = partes[0].lower() if partes else ""
        argumento = partes[1].strip() if len(partes) > 1 else None

        if comando == "":
            continue
        elif comando == "comandos":
            comandos()
        elif comando == "cadastrar":
            cadastrar()
        elif comando == "editar":
            editar(argumento)
            pausa()
        elif comando == "excluir":
            excluir(argumento)
            pausa()
        elif comando == "listar":
            # As funções de listagem (listar_pastas, listar_programas, etc.)
            # já pausam sozinhas ao final, então não pausamos de novo aqui.
            listar(argumento)
        elif comando == "limpar":
            limpar_pasta()
            pausa()
        elif comando == "navegador":
            navegador()
        elif comando == "abrir":
            if argumento:
                abrir(argumento)
            else:
                print("Uso: abrir {código}")
            pausa()
        elif comando in ("fechar", "sair"):
            sair()
        elif comando == "site":
            if argumento:
                abrir_link(argumento)
            else:
                print("Uso: site {link}")
            pausa()
        else:
            print("Comando não reconhecido. Digite 'comandos' para ver a lista.")
            pausa()
