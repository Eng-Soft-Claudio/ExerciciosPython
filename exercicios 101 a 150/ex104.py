def leiaint(numero):
    while True:
        try:
            n = int(input(numero))
        except (ValueError, TypeError):
            print("\033[0;31mERRO: por favor, digite um número inteiro válido.\033[m")
            continue
        except (KeyboardInterrupt):
            print('O usuário preferiu não digitar esse número.')
            return 0
        else:
            return n
numero = leiaint('Digite um número inteiro: ')
print(f'Você acabou de digitar o número {numero}.')