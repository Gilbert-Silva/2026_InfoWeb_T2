from datetime import datetime, timedelta

# init      - 8
# atributo  - 8
# validação - 8
# get/set   - 8
# str       - 8

class Avaliacao:
    def __init__(self, id, disciplina, local, data_hora):
        self.set_id(id)
        self.set_disciplina(disciplina)
        self.set_local(local)
        self.set_data_hora(data_hora)
    def set_id(self, id):
        if id < 0: raise ValueError()
        self.__id = id
    def set_disciplina(self, disciplina):
        if disciplina < "": raise ValueError()
        self.__disciplina = disciplina
    def set_local(self, local):
        if local < "": raise ValueError()
        self.__local = local
    def set_data_hora(self, data_hora):
        if data_hora < datetime.now(): raise ValueError()
        self.__data_hora = data_hora
    def get_id(self): return self.__id
    def get_disciplina(self): return self.__disciplina
    def get_local(self): return self.__local
    def get_data_hora(self): return self.__data_hora
    def __str__(self):
        return f"{self.__id} - {self.__disciplina} - {self.__local} -\
                 {self.__data_hora.strftime('%d/%m/%Y %H:%M')}"


# main     - 8
# menu     - 8
# inserir  - 8
# listar   - 8
# próximos - 8

class UI:
    objetos = []

    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.inserir()
            if op == 2: UI.listar()
            if op == 3: UI.proximos_dias()

    @staticmethod
    def menu():
        print("1-Inserir, 2-Listar, 3-Próximos dias, 9-Fim")
        return int(input("Escolha uma opção: "))

    @classmethod
    def inserir(cls):
        id = int(input("Informe o id: "))
        disciplina = input("Informe a disciplina: ")
        local = input("Informe o local: ")
        data_hora = datetime.strptime(input("Informe a data e hora: "), "%d/%m/%Y %H:%M")
        x = Avaliacao(id, disciplina, local, data_hora)
        cls.objetos.append(x) 

    @classmethod
    def listar(cls):
        for x in cls.objetos: print(x)

    @classmethod
    def proximos_dias(cls):    
        hoje = datetime.now()
        sete_dias = timedelta(days = 7)
        prox_sem = hoje + sete_dias
        for x in cls.objetos: 
            if hoje < x.get_data_hora() < prox_sem: print(x)
UI.main()
