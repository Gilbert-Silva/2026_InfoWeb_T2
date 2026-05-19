from datetime import datetime
from zoneinfo import ZoneInfo

x = datetime(2026, 5, 20, 15, 30, 10)
print(x)
print(type(x))
y = datetime(2000, 1, 5)
print(y)

print(x.day)
print(x.month)
print(x.year)
print(x.hour)
print(x.minute)
print(x.second)
print(x.microsecond)


z = datetime.now(ZoneInfo("America/Sao_Paulo"))
print(z)

z = datetime.now()
print(z)


