from app.core import tela_principal
from app.banco import carregar


def main():
    carregar()
    tela_principal()


if __name__ == "__main__":
    main()
