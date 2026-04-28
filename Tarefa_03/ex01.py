class Viagem:
    def __init__(self, dest: str, dist: float, lt: float):
        self.set_destino(dest)
        self.set_distancia(dist)
        self.set_litros(lt)

    # --------- GETTERS ---------
    def get_destino(self) -> str:
        return self.__destino

    def get_distancia(self) -> float:
        return self.__distancia

    def get_litros(self) -> float:
        return self.__litros

    # --------- SETTERS COM VALIDAÇÃO ---------
    def set_destino(self, dest: str):
        if not isinstance(dest, str) or dest.strip() == "":
            raise ValueError("Destino deve ser uma string não vazia.")
        self.__destino = dest

    def set_distancia(self, dist: float):
        if not isinstance(dist, (int, float)) or dist <= 0:
            raise ValueError("Distância deve ser um número maior que zero.")
        self.__distancia = float(dist)

    def set_litros(self, lt: float):
        if not isinstance(lt, (int, float)) or lt <= 0:
            raise ValueError("Litros deve ser um número maior que zero.")
        self.__litros = float(lt)

    # --------- MÉTODOS DA CLASSE ---------
    def Consumo(self) -> float:
        return self.__distancia / self.__litros

    def __str__(self) -> str:
        return (f"Destino: {self.__destino}, "
                f"Distância: {self.__distancia:.2f} km, "
                f"Litros: {self.__litros:.2f} L, "
                f"Consumo: {self.Consumo():.2f} km/L")

class UI:
    @staticmethod
    def main():
        op = 0
        while op != 2:
            op = UI.menu()
            if op == 1: UI.calculo()
        print("Tchau!!!! Volte logo.")    

    @staticmethod
    def menu():
        print("1 – Calcular, 2 – Fim")
        return int(input("Qual a opção: "))

    @staticmethod
    def calculo():
        dest = input("Qual foi seu destino na viagem? ")
        dist = float(input("Qual a distância percorrida em km? "))
        litros = float(input("Quantos litros de combustível foram gastos? "))
        x = Viagem(dest, dist, litros)
        print(x)

UI.main()
