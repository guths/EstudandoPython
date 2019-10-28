altura=int(input("Digite a sua altura: "))

largura=int(input("Digite a largura: "))

area=int(largura*altura)

countn=1

i=1

for i in range(1,area+1):

    if countn==1 or countn==altura:

        print("$",end='')

    else:

        if ((countn-1)*largura+1)==i or (countn*largura)==i:

            print("$",end='')

        else:
            print(" ",end='')

    if i%largura==0:

        print('')

        countn=countn+1
