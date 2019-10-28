import matrizes


def soma_matriz(a, b):
    '''tem como parametro a matriz e a matriz b '''
    numl = len(a)
    numc = len(a[0])
    c = matrizes.cria_matriz(numl, numc, 0)
    for l in range(numl):
        for c in range(numc):
            c[line][column] = a[line][column] + b[line][column]
    return c
