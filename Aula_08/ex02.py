# dicionário é uma lista de itens
# os itens são separados por ,
# cada item chave : valor

x = {"RN" : "Natal", "PB" : "João Pessoa", "PE" : "Recife"}
x["AM"] = "Manaus"
x[5] = "Teste"  # insere a chave 5
x.pop(5)        # remove a chave 5
y = {}  # dicionário vazio
x["PB"] = "J. Pessoa"
print(x)
print(*x)
print(len(x)) # número de itens
print(max(x))

for item in x.items(): print(item)
for item in x: print(item)



print(x["RN"])

y = [1, 2, 3, 4]
z = (1, 2, 3, 4)
print(type(x))
print(type(y))
print(type(z))

