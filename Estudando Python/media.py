#media , mediana e a moda(valor que mais se repete)
def media(lista) :
    media= sum(lista)/float(len(lista))
    return media
def mediana(lista):
    lista_ordenada = sorted(lista)
    tamanho = len(lista_ordenada)

    if t %2 == 0 :
        mediana= (lista_ordenada[int(tamanho/2)]+lista_ordenada[int((tamanho/2+1)])/2
    elif t%2==1 :
        mediana=lista_ordenada[int(tamanho/2)]
return mediana






