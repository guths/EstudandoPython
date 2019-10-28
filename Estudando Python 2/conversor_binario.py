
def bin_to_deci(numerob):
    print('**BINARIO PARA DECIMAL**')
    numerob = str(input('Digite um numero: '))
    soma = 0
    contador = len(numerob) - 1
    for n in numerob:
        n = int(n)
        if n == 1:
            soma = soma + (2 ** (contador))
        contador = contador - 1
    print('O numero {} em decimal eh {}'.format(numerob, soma))





