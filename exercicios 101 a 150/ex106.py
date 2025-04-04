from time import sleep

# Definição de cores
c = ('\033[m',        # 0 - sem cor
     '\033[0;30;41m', # 1 - vermelho
     '\033[0;30;42m', # 2 - verde
     '\033[0;30;43m', # 3 - amarelo
     '\033[0;30;44m', # 4 - azul
     '\033[0;30;45m', # 5 - roxo
     '\033[7;30m'     # 6 - branco
     )

def ajuda(com):
    """
    Exibe o manual de um comando ou função usando a função help().
    """
    titulo(f"Acessando o manual do comando '{com}'", 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)

def titulo(msg, cor=0):
    """
    Exibe uma mensagem estilizada com bordas e cores.
    :param msg: Mensagem a ser exibida.
    :param cor: Índice da cor na tupla 'c'.
    """
    tam = len(msg) + 4
    print(c[cor], end='')
    print("~" * tam)
    print(f"  {msg}")
    print("~" * tam)
    print(c[0], end='')
    sleep(1)

def main():
    """
    Função principal que implementa o sistema de ajuda interativo.
    """
    while True:
        titulo('SISTEMA DE AJUDA PyHELP', 2)
        comando = input('Função ou Biblioteca > ').strip()
        if comando.upper() == 'FIM':
            break
        else:
            ajuda(comando)
    titulo('ATÉ LOGO!', 1)
    sleep(1)

# Execução do programa
if __name__ == "__main__":
    main()