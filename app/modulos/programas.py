import os
import subprocess
from ..listas import programas
from ..banco import salvar
from ..terminal import pausa

_COMANDOS_PERIGOSOS = [
    "format ", "mkfs", "dd if=", "dd of=",
    "rm -rf /", "rm -rf ~", "rm -rf *", "rm -rf .",
    "del /s", "del /f /s", "rd /s", "rmdir /s",
    "shutdown", "restart-computer", "reboot",
    "reg delete", "reg import",
    "diskpart", "bcdedit", "vssadmin", "cipher /w",
    "taskkill /f /im", ":(){ :|:& };:",
    "chmod -R 777 /", "chown -R / ", "sudo rm",
    "> /dev/sda", "mkfs.",
]

def _eh_comando_perigoso(comando):
    comando_lower = comando.lower()
    return any(trecho in comando_lower for trecho in _COMANDOS_PERIGOSOS)

def cadastrar_programas():
    nome = input("Nome do programa/comando: ")
    codigo = input("Código: ")
    comando = input(
        "Comando ou caminho do executável (ex: regedit, calc, notepad, explorer %temp%): "
    )

    if _eh_comando_perigoso(comando):
        print("Esse comando parece potencialmente destrutivo e não será cadastrado por segurança.")
        return

    programas[codigo] = {
        "nome": nome,
        "comando": comando
    }

    salvar()
    print("Programa cadastrado com sucesso!")
    pausa()

def abrir_programa(codigo):
    if codigo not in programas:
        print(f"Nenhum programa encontrado com o código '{codigo}'.")
        return

    programa = programas[codigo]

    comando = os.path.expandvars(os.path.expanduser(programa["comando"]))

    if _eh_comando_perigoso(comando):
        print("Esse comando parece potencialmente destrutivo e não será executado.")
        return

    try:
        subprocess.Popen(comando, shell=True)
        print(f"Executando: {programa['nome']} ({comando})")
    except Exception as e:
        print(f"Não foi possível executar '{programa['nome']}': {e}")

def listar_programas():
    if not programas:
        print("Nenhum programa cadastrado.")
        pausa()
        return

    for codigo, dados in programas.items():
        print(f"[{codigo}] {dados['nome']} - {dados['comando']}")

    pausa()

def editar_programa():
    codigo = input("Digite o código do programa que deseja editar: ")
    if codigo not in programas:
        print(f"Nenhum programa encontrado com o código '{codigo}'.")
        return

    programa = programas[codigo]

    nome = input(f"Nome do programa/comando ({programa['nome']}): ") or programa['nome']
    comando = input(f"Comando ou caminho do executável ({programa['comando']}): ") or programa['comando']

    if _eh_comando_perigoso(comando):
        print("Esse comando parece potencialmente destrutivo e não será cadastrado por segurança.")
        return

    programas[codigo] = {
        "nome": nome,
        "comando": comando
    }

    salvar()
    print("Programa atualizado com sucesso!")

def excluir_programa():
    codigo = input("Digite o código do programa que deseja excluir: ")
    if codigo not in programas:
        print(f"Nenhum programa encontrado com o código '{codigo}'.")
        return

    del programas[codigo]
    salvar()
    print("Programa excluído com sucesso!")
