s = int(input("Por favor, entre com o número de segundos que deseja converter: "))
d = s//86400
segundosrestantes = s%86400
h = segundosrestantes*24
hr = h%3600
m = hr//60
sr = m%60
print (d ,"dias" ,h, "horas",m,"minutos e " ,sr, "segundos.")
