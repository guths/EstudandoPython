import media as m
import aleatorio as a

lista=a.numeroaleatorio(10)
print(lista)

media=m.media(lista)
mediana=m.mediana(lista)
moda=m.moda(lista)


print("a media da minha lista eh "+str(media))
print("a mediana da minha lista eh "+str(mediana))
print("a moda da minha lista eh "+str(moda))