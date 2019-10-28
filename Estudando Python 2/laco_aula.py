cp=0
ci=0
somap=0
somai=0

numero=int(input("Digite seu numero: "))

while numero>0 :
    if numero%2==0 :
        cp=cp+1
        somap=numero+somap
    else :
        ci=ci+1
        somai=somai+numero
    numero = int(input("Digite seu numero: "))

mediap=somap/cp
mediai=somai/ci

print("A media dos numeros pares eh {}".format(mediap))
print("A media dos numeros impares eh {}".format(mediai))
print("A quantidade de numeros impares eh {}".format(ci))
print("A quantidade de numeros pares eh {}".format(cp))



