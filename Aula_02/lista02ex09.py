print("Digite uma frase:")
s = input()
lista = s.split()
for palavra in lista:
    print(palavra[::-1])