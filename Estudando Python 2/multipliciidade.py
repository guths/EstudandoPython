numero=int(input("Digite seu numero: "))
multiplicidade=0
fator=2


while numero>0 :
    while numero%2==0 :
        multiplicidade=multiplicidade+1
        numero=numero/fator
    if multiplicidade>0 :
        print("O falor eh {} e o a multiplicidade eh {}".format(fator, multiplicidade))
    fator=fator+1
    multiplicidade=0



