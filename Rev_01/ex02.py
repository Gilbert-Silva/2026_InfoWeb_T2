class Triangulo:
    def __init__(self):
        self.b = 0
        self.h = 0
    def __str__(self):
        return f"Triângulo de base {self.b} e altura {self.h}"    

class UI:
    @staticmethod
    def main():
        lista = [Triangulo(), Triangulo()]
        lista.append(Triangulo())
        lista[0].b = 10
        lista[0].h = 20
        for obj in lista:
            print(obj)

UI.main()

