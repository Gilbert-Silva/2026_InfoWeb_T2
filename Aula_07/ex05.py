from datetime import datetime, timedelta

x = timedelta(hours=1, minutes=30)
print(x)
y = timedelta(minutes=40)
print(y)
print(x+y)

hoje = datetime.now()
nasc = datetime.strptime(input("Sua data de nascimento: "), "%d/%m/%Y")

d = hoje - nasc
print(d)
anos = d.days // 365
meses = d.days % 365 // 30
print(anos, "anos")
print(meses, "meses")

