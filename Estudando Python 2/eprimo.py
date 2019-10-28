from funcao_primo import *


numero=int(input("Digite seu numero:  "))


while numero>0 :
    if primo(numero):
        print("O numero {} eh primo".format(numero))
    else :
        print("O numero {} n eh primo".format(numero))
    numero = int(input("Digite seu numero:   "))