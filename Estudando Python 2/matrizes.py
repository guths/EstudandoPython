def cria_matriz(line,column,valor):
    #Cria e retorna uma matriz com n linhas e n colunas
    matriz=[]
    for i in range(line):
        linha=[]
        for j in range(column):
            linha.append(valor)
        matriz.append(linha)
    return matriz

print(cria_matriz(2,2,2))







