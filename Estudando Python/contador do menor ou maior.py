
i=soma=media=maior=menor=0

while i<=500 :
    numero = int(input("Digite o um numero "))
    soma=soma+numero
    i=i+1
    if  numero>maior :
        maior=numero
    if numero<maior:
        menor=numero


media=soma/i
print(maior,menor)
print(soma)
print(media)




