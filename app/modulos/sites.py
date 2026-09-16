# sites.py
import webbrowser
from .. import listas
from ..listas import sites, navegadores_padroes
from ..terminal import clear, pausa
from ..banco import salvar
from ..validacao import validar, validar_codigo, normalizar_codigo

def cadastrar_sites():
    clear()
    nome = validar("Nome do site: ")
    codigo = validar_codigo("Código do site: ")
    endereco = validar("link do site: ")

    # Validação de código duplicado
    if codigo in sites:
        print(f"Erro: O código '{codigo}' já cadastrado!")
        pausa()
        return

    sites[codigo] = {
        "nome": nome,
        "endereco": endereco
    }

    salvar()
    print("Site cadastrado com sucesso!")
    pausa()

def _abrir_com_navegador_padrao(endereco, nome=None):
    navegador_codigo = listas.navegador_padrao_selecionado

    if navegador_codigo is None or navegador_codigo not in navegadores_padroes:
        print("Nenhum navegador padrão definido. Abrindo com o navegador padrão do sistema...")
        webbrowser.open(endereco)
    else:
        navegador = navegadores_padroes[navegador_codigo]
        try:
            webbrowser.register(
                navegador_codigo,
                None,
                webbrowser.BackgroundBrowser(navegador["endereco"])
            )
            controlador = webbrowser.get(navegador_codigo)
            controlador.open(endereco)
        except webbrowser.Error:
            print(f"Não foi possível abrir com '{navegador['nome']}'. Abrindo com o navegador padrão do sistema...")
            webbrowser.open(endereco)

    if nome:
        print(f"Abrindo site: {nome} ({endereco})")
    else:
        print(f"Abrindo: {endereco}")

def abrir_site(codigo):
    if codigo not in sites:
        print(f"Nenhum site encontrado com o código '{codigo}'.")
        return

    site = sites[codigo]
    _abrir_com_navegador_padrao(site["endereco"], site["nome"])

def abrir_link(link):
    link = link.strip()

    if not link:
        print("Nenhum link informado.")
        return

    if not link.lower().startswith(("http://", "https://")):
        link = "https://" + link

    _abrir_com_navegador_padrao(link)

def listar_sites():
    if not sites:
        print("Nenhum site cadastrado.")
        pausa()
        return

    for codigo, dados in sites.items():
        print(f"[{codigo}] {dados['nome']} - {dados['endereco']}")
    pausa()

def excluir_site():
    codigo = normalizar_codigo(input("Digite o código do site que deseja excluir: "))
    if codigo not in sites:
        print(f"Nenhum site encontrado com o código '{codigo}'.")
        return

    del sites[codigo]
    salvar()
    print("Site excluído com sucesso!")

def editar_site():
    codigo = normalizar_codigo(input("Digite o código do site que deseja editar: "))
    if codigo not in sites:
        print(f"Nenhum site encontrado com o código '{codigo}'.")
        return

    site = sites[codigo]

    nome = input(f"Nome do site ({site['nome']}): ") or site['nome']
    endereco = input(f"Link do site ({site['endereco']}): ") or site['endereco']

    sites[codigo] = {
        "nome": nome,
        "endereco": endereco
    }
    
    salvar()
    print("Site atualizado com sucesso!")
