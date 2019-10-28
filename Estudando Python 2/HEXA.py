print('**HEXADECIMAL PARA DECIMAL**')
    numeroh =str(input('Digite um numero: '))
    soma = 0
    contador = len(numeroh) - 1
    for n in numeroh:
        if n==A:
            n=10:
        elif n==B:
            n=11
        elif n==C:
            n=12
        elif n==D:
            n=13
        elif n==E:
            n=14
        elif n==F:
            n=15
            soma = soma + (n*(16 ** (contador))
        contador = contador - 1
    print('O numero {} em decimal eh {}'.format(numeroh, soma))