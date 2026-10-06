class Triangulo:
    def __init__(self):
        self.b = 0
        self.h = 0
    def __str__(self):
        return f"Triângulo de base {self.b} e altura {self.h}"    

class UI:
    @staticmethod
    def main():
        x = Triangulo()
        x.b = -10
        x.h = 20
        y = Triangulo()
        z = x
        z.b = 30
        z.h = 40

        print(x, x.b, x.h) # 10, 20
        print(y, y.b, y.h) # 0, 0
        print(z, z.b, z.h) # 30, 40

        l = [x, y, z]
        l[0].b = 50
        l[0].h = 60

        print(x, x.b, x.h) # 50, 60
        print(l)

        l[2].b = 100
        l[2].h = 200
        print(x, x.b, x.h)

        j = l
        j[0].b = 300
        j[0].h = 400
        print(x, x.b, x.h)

UI.main()        
