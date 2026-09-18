# app/validacao.py

def validar(mensagem, obrigatorio=True):
    """Pede uma entrada ao usuário, remove espaços extras nas pontas e,
    se obrigatorio=True, repete a pergunta até receber algo não vazio.

    Use obrigatorio=False em campos de edição, onde uma resposta vazia
    significa 'manter o valor atual'.
    """
    while True:
        valor = input(mensagem).strip()
        if valor or not obrigatorio:
            return valor
        print("Este campo não pode ficar vazio. Tente novamente.")


def normalizar_codigo(codigo):
    """Remove espaços das pontas e converte para minúsculas, para que
    códigos sejam tratados de forma case-insensitive (ex: 'G1' e 'g1'
    são considerados o mesmo código). Use em TODO lugar que lê ou
    compara um código digitado pelo usuário -- cadastro, busca,
    exclusão e edição -- para manter o comportamento consistente."""
    return codigo.strip().lower()


def validar_codigo(mensagem, obrigatorio=True):
    """Como validar(), mas já retorna o código normalizado
    (normalizar_codigo()). Use para os campos de 'código' nos
    cadastros; para nome/endereço continue usando validar()."""
    return normalizar_codigo(validar(mensagem, obrigatorio))
