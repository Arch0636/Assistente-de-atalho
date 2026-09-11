import os
import sys
import time
from .banco import salvar

def clear():
    """Limpa a tela do terminal de forma multiplataforma."""
    os.system("cls" if os.name == "nt" else "clear")

def sair():
    """Encerra o programa graciosamente."""
    clear()
    salvar()
    print("Encerrando o programa...")
    time.sleep(1)
    clear() #pode ser apagado, Só serve para terminais que não fecha automaticamente apois o encerramento
    sys.exit()

def opcao_invalida():
    """Informa que a opção é inválida e aguarda o usuário."""
    print("Opção Inválida.\n")
    input("Pressione ENTER para continuar...")

def pausa():
    """Apenas pausa a execução até o usuário pressionar ENTER."""
    input("Pressione ENTER para continuar...")

def comandos():
    clear()
    print("--- Comandos disponíveis ---\n")
    print("sair: digite 'sair' para voltar ao menu.")
    print("fechar: digite 'fechar' para sair do programa.")
    print("listar: digite 'listar' para listar programas disponíveis.")
