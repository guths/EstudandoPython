import random
def numeroaleatorio(tam) :
    lista=[]
    for i in range(tam) :
        lista.append(random.randint(0,tam))
    return lista
