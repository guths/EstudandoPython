
def maior_primo(k):
    x=2
    primo = 0
    while x <= k:
        fator = 2
        teste = False
        while x%fator!=0 and fator <=x/2 :
            fator=fator+1
        if x % fator==0 :
          teste=False
        else :
            teste=True
        if teste :
            primo = x
        x=x+1
    return primo










