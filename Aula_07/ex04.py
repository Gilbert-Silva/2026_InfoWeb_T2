from datetime import datetime
s = input("Informe sua data de nascimento no formato dd/mm/aaaa: ")
data = datetime.strptime(s, "%d/%m/%Y")
print(data)
print(data.strftime("%d/%m/%Y"))
print(data.weekday()) # 0 - Seg, 1 - Ter, 2 - Qua, ....


# strptime - passa uma string para datetime
# strftime - passa uma datetime para string

x = int(input("Informe um número: "))
d = datetime.strptime(input("Informe uma data: "), "%d/%m/%Y")

