import os
import platform
import subprocess
import shutil
from ..listas import pastas
from ..terminal import pausa, clear
from ..banco import salvar

def cadastrar_pastas():
    clear()
    nome = input("Nome da pasta: ")
    codigo = input("Código da pasta: ")
    endereco = input("Caminho ou link da pasta: ")

    pastas[codigo] = {
        "nome": nome,
        "endereco": endereco
    }

    salvar()
    print("Pasta cadastrada com sucesso!")
    pausa()

def abrir_pasta(codigo):
    if codigo not in pastas:
        print(f"Nenhuma pasta encontrada com o código '{codigo}'.")
        return

    pasta = pastas[codigo]

    # Expande variáveis de ambiente e "~", assim caminhos como "%temp%",
    # "%appdata%" (Windows) ou "~/Downloads" (Linux/macOS) funcionam como atalhos,
    # sem precisar cadastrar o caminho absoluto exato.
    endereco = os.path.expandvars(os.path.expanduser(pasta["endereco"]))

    if not os.path.isdir(endereco):
        print(f"O caminho '{endereco}' não existe ou não é uma pasta válida.")
        return

    sistema = platform.system()

    try:
        if sistema == "Windows":
            os.startfile(endereco)
        elif sistema == "Darwin":  # macOS
            subprocess.Popen(["open", endereco])
        else:  # Linux e demais sistemas Unix-like
            subprocess.Popen(["xdg-open", endereco])

        print(f"Abrindo pasta: {pasta['nome']} ({endereco})")
    except Exception as e:
        print(f"Não foi possível abrir a pasta '{pasta['nome']}': {e}")

def listar_pastas():
    if not pastas:
        print("Nenhuma pasta cadastrada.")
        pausa()
        return

    for codigo, dados in pastas.items():
        print(f"[{codigo}] {dados['nome']} - {dados['endereco']}")

    pausa()

def excluir_pasta():
    codigo = input("Digite o código da pasta que deseja excluir: ")
    if codigo not in pastas:
        print(f"Nenhuma pasta encontrado com o código '{codigo}'.")
        return

    del pastas[codigo]
    salvar()
    print("Pasta excluída com sucesso!")

def limpar():
    """Apaga todo o conteúdo (arquivos e subpastas) de uma pasta cadastrada,
    mantendo a própria pasta. Pede confirmação antes de apagar, já que a
    ação não pode ser desfeita."""
    codigo = input("Digite o código da pasta que deseja limpar: ")
    if codigo not in pastas:
        print(f"Nenhuma pasta encontrada com o código '{codigo}'.")
        return

    pasta = pastas[codigo]
    endereco = os.path.expandvars(os.path.expanduser(pasta["endereco"]))

    if not os.path.isdir(endereco):
        print(f"O caminho '{endereco}' não existe ou não é uma pasta válida.")
        return

    itens = os.listdir(endereco)
    if not itens:
        print(f"A pasta '{pasta['nome']}' já está vazia.")
        return

    print(f"Isso vai apagar TODO o conteúdo de '{pasta['nome']}' ({endereco}).")
    print(f"{len(itens)} item(ns) encontrados dentro dela.")
    confirmacao = input(
        "Essa ação NÃO pode ser desfeita. Tem certeza que deseja continuar? (s/n): "
    ).strip().lower()

    if confirmacao != "s":
        print("Operação cancelada.")
        return

    apagados = 0
    erros = []

    for item in itens:
        caminho_item = os.path.join(endereco, item)
        try:
            if os.path.isdir(caminho_item) and not os.path.islink(caminho_item):
                shutil.rmtree(caminho_item)
            else:
                os.remove(caminho_item)
            apagados += 1
        except Exception as e:
            erros.append(f"{item}: {e}")

    print(f"{apagados} item(ns) apagado(s) da pasta '{pasta['nome']}'.")
    if erros:
        print("Alguns itens não puderam ser apagados:")
        for erro in erros:
            print(f"- {erro}")

def editar_pasta():
    codigo = input("Digite o código da pasta que deseja editar: ")
    if codigo not in pastas:
        print(f"Nenhuma pasta encontrada com o código '{codigo}'.")
        return

    pasta = pastas[codigo]

    nome = input(f"Nome da pasta ({pasta['nome']}): ") or pasta['nome']
    endereco = input(f"Caminho ou link da pasta ({pasta['endereco']}): ") or pasta['endereco']

    pastas[codigo] = {
        "nome": nome,
        "endereco": endereco
    }
    
    salvar()
    print("Pasta atualizada com sucesso!")
