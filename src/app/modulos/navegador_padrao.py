import os
import platform
import shutil
from ..listas import navegadores_padroes
from .. import listas
from ..banco import salvar
from ..terminal import pausa
from ..validacao import validar, validar_codigo, normalizar_codigo

def cadastrar_navegador_padrao():
    nome = validar("Nome do navegador: ")
    codigo = validar_codigo("Código do navegador: ")
    endereco = validar("Caminho ou link do navegador: ")

    if codigo in navegadores_padroes:
        print(f"Erro: O código '{codigo}' já cadastrado!")
        pausa()
        return

    navegadores_padroes[codigo] = {
        "nome": nome,
        "endereco": endereco
    }

    salvar()
    print("Navegador cadastrado com sucesso!")
    pausa()

def definir_navegador_padrao():
    if not navegadores_padroes:
        print("Nenhum navegador cadastrado ainda. Cadastre um navegador primeiro.")
        return

    print("\n--- Navegadores Cadastrados ---")
    for codigo, dados in navegadores_padroes.items():
        marcador = " (atual)" if codigo == listas.navegador_padrao_selecionado else ""
        print(f"{codigo}: {dados['nome']}{marcador}")

    codigo = normalizar_codigo(input("Digite o código do navegador que deseja definir como padrão: "))

    if codigo not in navegadores_padroes:
        print("Código inválido. Nenhum navegador encontrado com esse código.")
        return

    # Altera o atributo no módulo (não a referência importada localmente),
    # assim a mudança fica visível para todo o programa.
    listas.navegador_padrao_selecionado = codigo
    salvar()
    print(f"Navegador '{navegadores_padroes[codigo]['nome']}' definido como padrão!")

def listar_navegadores():
    if not navegadores_padroes:
        print("Nenhum navegador cadastrado.")
        pausa()
        return

    for codigo, dados in navegadores_padroes.items():
        marcador = " (atual)" if codigo == listas.navegador_padrao_selecionado else ""
        print(f"[{codigo}] {dados['nome']} - {dados['endereco']}{marcador}")

    pausa()

def scanear_navegadores():
    """Procura por navegadores comuns instalados no sistema e cadastra
    automaticamente os que forem encontrados (sem sobrescrever os que
    já estiverem cadastrados)."""
    sistema = platform.system()
    candidatos = []

    if sistema == "Windows":
        program_files = os.environ.get("ProgramFiles", r"C:\Program Files")
        program_files_x86 = os.environ.get("ProgramFiles(x86)", r"C:\Program Files (x86)")
        local_app_data = os.environ.get("LOCALAPPDATA", "")

        candidatos = [
            ("chrome", "Google Chrome", os.path.join(program_files, "Google", "Chrome", "Application", "chrome.exe")),
            ("chrome", "Google Chrome", os.path.join(program_files_x86, "Google", "Chrome", "Application", "chrome.exe")),
            ("firefox", "Mozilla Firefox", os.path.join(program_files, "Mozilla Firefox", "firefox.exe")),
            ("firefox", "Mozilla Firefox", os.path.join(program_files_x86, "Mozilla Firefox", "firefox.exe")),
            ("edge", "Microsoft Edge", os.path.join(program_files_x86, "Microsoft", "Edge", "Application", "msedge.exe")),
            ("edge", "Microsoft Edge", os.path.join(program_files, "Microsoft", "Edge", "Application", "msedge.exe")),
            ("brave", "Brave", os.path.join(program_files, "BraveSoftware", "Brave-Browser", "Application", "brave.exe")),
            ("brave", "Brave", os.path.join(program_files_x86, "BraveSoftware", "Brave-Browser", "Application", "brave.exe")),
            ("opera", "Opera", os.path.join(local_app_data, "Programs", "Opera", "launcher.exe")),
        ]
    elif sistema == "Darwin":
        candidatos = [
            ("chrome", "Google Chrome", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"),
            ("firefox", "Mozilla Firefox", "/Applications/Firefox.app/Contents/MacOS/firefox"),
            ("edge", "Microsoft Edge", "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge"),
            ("brave", "Brave", "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"),
            ("opera", "Opera", "/Applications/Opera.app/Contents/MacOS/Opera"),
            ("safari", "Safari", "/Applications/Safari.app/Contents/MacOS/Safari"),
        ]
    else:  # Linux e demais sistemas Unix-like
        comandos_linux = [
            ("chrome", "Google Chrome", ["google-chrome", "google-chrome-stable"]),
            ("firefox", "Mozilla Firefox", ["firefox"]),
            ("edge", "Microsoft Edge", ["microsoft-edge", "microsoft-edge-stable"]),
            ("brave", "Brave", ["brave-browser"]),
            ("opera", "Opera", ["opera"]),
            ("chromium", "Chromium", ["chromium", "chromium-browser"]),
        ]

        for codigo, nome, comandos in comandos_linux:
            for comando in comandos:
                caminho = shutil.which(comando)
                if caminho:
                    candidatos.append((codigo, nome, caminho))
                    break

    encontrados = []

    for codigo, nome, caminho in candidatos:
        # No Windows/macOS o caminho é um arquivo específico, então
        # precisamos confirmar que ele realmente existe no disco.
        # No Linux o caminho já veio validado pelo shutil.which().
        if sistema in ("Windows", "Darwin") and not os.path.exists(caminho):
            continue

        if codigo in navegadores_padroes:
            continue  # já cadastrado manualmente ou em um scan anterior

        navegadores_padroes[codigo] = {"nome": nome, "endereco": caminho}
        encontrados.append(nome)

    if encontrados:
        salvar()
        print("Navegadores encontrados e cadastrados automaticamente:")
        for nome in encontrados:
            print(f"- {nome}")
    else:
        print("Nenhum navegador novo foi encontrado (ou todos já estavam cadastrados).")

    pausa()
