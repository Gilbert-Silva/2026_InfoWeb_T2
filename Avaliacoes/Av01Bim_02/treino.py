class Treino:
    def __init__(self, id, esporte, data, tempo):
        self.set_id(id)
        self.set_esporte(esporte)
        self.set_data(data)
        self.set_tempo(tempo)
    def __str__(self):
        return f"{self.__id} - {self.__esporte} - {self.__data} - {self.__tempo}"    
    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser um valor positivo")
        self.__id = id
    def set_esporte(self, esporte):
        if esporte == "": raise ValueError("Esporte não pode ser vazio")
        self.__esporte = esporte
    def set_data(self, data):
        if data == "": raise ValueError("Data não pode ser vazia")
        self.__data = data
    def set_tempo(self, tempo):  
        if tempo < 0: raise ValueError("Tempo deve ser positivo")
        self.__tempo = tempo
    def get_id(self): return self.__id
    def get_esporte(self): return self.__esporte
    def get_data(self): return self.__data
    def get_tempo(self): return self.__tempo

class UI:
    __lista = []
    @staticmethod
    def main():
        op = 0
        while op != 4:
            op = UI.menu()
            if op == 1: UI.inserir()
            if op == 2: UI.listar()
            if op == 3: UI.media()

    @staticmethod
    def menu():
        print("1-Inserir 2-Listar 3-Média 4-Sair")
        return int(input("Escolha uma opção: "))

    @classmethod
    def inserir(cls):
        id = int(input("Informe o id do treino: "))
        esporte = input("Informe o esporte: ")
        data = input("Informe a data: ")
        tempo = int(input("Informe o tempo em minutos: "))
        x = Treino(id, esporte, data, tempo)
        cls.__lista.append(x)

    @classmethod
    def listar(cls):
        for x in cls.__lista: print(x)

    @classmethod
    def media(cls):    
        soma = 0
        for x in cls.__lista: 
            soma += x.get_tempo()
        if len(cls.__lista) == 0: print(0)
        else: print(soma/len(cls.__lista))     

UI.main()


# Q1 - Atributos - 6
#    - Init      - 6
#    - Validação - 6
#    - Set/Get   - 6
#    - Str       - 6

# Q3 - Atributos - 3
#    - Métodos   - 3
#    - Parâmetros- 3
#    - Retorno   - 3
#    - Visibilidade - 3

