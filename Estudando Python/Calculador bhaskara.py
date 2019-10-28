import math
a = int(input("Insira o valor da constante A : "))
b = int(input("Insira o valor da constante B : "))
c = int(input("Insira o valor da constante C : "))

d = b**2-4*a*c

if d>0:
    delta = math.sqrt(d)
    x=(-b + delta)/(2*a)
    y=(-b - delta)/(2*a)
    print("as raízes da equação são", x ,"e" , y ,)
elif d == 0 :
    math.sqrt(d)
    x=-b / (2*a)
    print("a raiz desta equação é", x)
elif d<0 :
    print ("esta equação não possui raízes reais")
