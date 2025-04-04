def escreva(msg):
    tam = int(len(msg) + 4)
    print('~' * tam)
    print(f"{msg}".center(tam))
    print('~' * tam)

msg = str(input('Digite uma mensagem: ')).strip()
escreva(msg)
print('Fim do programa.')
