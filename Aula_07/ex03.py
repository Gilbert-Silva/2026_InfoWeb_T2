from datetime import datetime
s = input("Informe sua data de nascimento no formato dd/mm/aaaa: ")
print(s)
d,m,a = s.split("/")
d = int(d)
m = int(m)
a = int(a)
print(d)
print(m)
print(a)
data = datetime(a, m, d)
print(data)
print(data.strftime("%d/%m/%Y")) # strftime - passa uma data para string



