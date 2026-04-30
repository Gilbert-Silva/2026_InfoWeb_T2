x = [10, 20, 30, 40]
y = x         # x e y são a mesma lista
y.append(50)
print(x)
z = x[:]      # z é uma cópia
z.append(60)
print(x)
print(z)

x = [8, 1, 3, 4, 10]
print(x)
x.reverse()
print(x)
