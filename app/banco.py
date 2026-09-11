import json
import os
from . import listas

# Caminho para a pasta data/ na raiz do projeto (dois níveis acima deste arquivo:
# app/banco.py -> app/ -> raiz do projeto -> data/)
_RAIZ_PROJETO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARQUIVO_DADOS = os.path.join(_RAIZ_PROJETO, "data", "dados.json")

def salvar():
    """Salva o estado atual (sites, pastas, programas, navegadores) em um arquivo JSON."""
    dados = {
        "navegadores_padroes": listas.navegadores_padroes,
        "programas": listas.programas,
        "pastas": listas.pastas,
        "sites": listas.sites,
        "navegador_padrao_selecionado": listas.navegador_padrao_selecionado
    }

    try:
        os.makedirs(os.path.dirname(ARQUIVO_DADOS), exist_ok=True)
        with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)
    except OSError as e:
        print(f"Erro ao salvar dados: {e}")

def carregar():
    """Carrega o estado salvo do arquivo JSON, se ele existir."""
    if not os.path.exists(ARQUIVO_DADOS):
        return

    try:
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
    except (json.JSONDecodeError, OSError) as e:
        print(f"Erro ao carregar dados: {e}")
        return

    # Importante: usar .clear() + .update() em vez de "listas.sites = ..."
    # Assim os dicionários continuam sendo os MESMOS objetos que outros
    # módulos já importaram (ex: "from listas import sites" em sites.py).
    # Se reatribuíssemos o atributo do módulo, quem já importou o dicionário
    # antigo continuaria enxergando os dados desatualizados.
    listas.navegadores_padroes.clear()
    listas.navegadores_padroes.update(dados.get("navegadores_padroes", {}))

    listas.programas.clear()
    listas.programas.update(dados.get("programas", {}))

    listas.pastas.clear()
    listas.pastas.update(dados.get("pastas", {}))

    listas.sites.clear()
    listas.sites.update(dados.get("sites", {}))

    # Esse é um valor simples (str ou None), não um dicionário, então pode
    # ser reatribuído normalmente no módulo.
    listas.navegador_padrao_selecionado = dados.get("navegador_padrao_selecionado")
