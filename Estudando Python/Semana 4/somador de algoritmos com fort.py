
numero = str(input("Digite um número: "))
tamanho = len(numero)
numero = int(numero)
i=tamanho
resposta=0
divisor= 10**(tamanho-1)

while i > 0:
    resposta=(int(numero//divisor))+resposta
    numero = numero%divisor
    divisor = divisor/10
    i=i-1
print(resposta)
