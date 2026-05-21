from datetime import datetime

class Paciente:
    def __init__(self, i, n, c, t, nasc):
        self.set_id(i)
        self.set_nome(n)
        self.set_cpf(c)
        self.set_telefone(t)
        self.set_nascimento(nasc)
    def set_id(self, i):
        if i < 0: raise ValueError("Id deve ser positivo")
        self.__id = i
    def set_nome(self, n):
        if n == "": raise ValueError("Nome não pode ser vazio")
        self.__nome = n
    def set_cpf(self, c):
        if c == "": raise ValueError("CPF não pode ser vazio")
        self.__cpf = c
    def set_telefone(self, t):
        if t == "": raise ValueError("Telefone não pode ser vazio")
        self.__telefone = t
    def set_nascimento(self, nasc):
        if nasc > datetime.now(): raise ValueError("Data não pode ser no futuro")
        self.__nascimento = nasc
    def get_id(self): return self.__id    
    def get_nome(self): return self.__nome    
    def get_cpf(self): return self.__cpf    
    def get_telefone(self): return self.__telefone    
    def get_nascimento(self): return self.__nascimento    
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__cpf} - {self.__telefone} - " + \
            f"{self.__nascimento.strftime("%d/%m/%Y")}"
    def idade(self):
        tempo = datetime.now() - self.__nascimento  # medido em dias, horas, ... timedelta
        anos = tempo.days // 365
        meses = tempo.days % 365 // 30
        return f"{anos} ano(s) e {meses} mes(es)"

#x = Paciente(1, "Eduardo", "09808909812", "84900090909", datetime(1990, 10, 5))
#print(x)
#print(x.idade())    
class PacienteUI:
    __pacientes = []  # atributo - fora do init - não tem objetos de PacienteUI
    @staticmethod     # quando não acessa o atributo
    def main():
        op = 0
        while op != 9:
            op = PacienteUI.menu()
            if op == 1: PacienteUI.inserir()
            if op == 2: PacienteUI.listar()

    @staticmethod
    def menu():
        print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir, 5-Pesquisar, 6-Aniversariantes, 9-Fim")
        return int(input("Escolha uma opção: "))
    
    @classmethod      # quando acessa o atributo - usa o cls
    def inserir(cls):
        id = int(input("Informe o id: "))
        nome = input("Informe o nome: ")
        cpf = input("Informe o cpf: ")
        fone = input("Informe o telefone: ")
        nasc = datetime.strptime(input("Informe a data de nascimento dd/mm/aaaa: "), "%d/%m/%Y")
        x = Paciente(id, nome, cpf, fone, nasc)
        cls.__pacientes.append(x)

    @classmethod
    def listar(cls):
        if len(cls.__pacientes) == 0: print("Nenhum paciente cadastrado")
        else:
            for x in cls.__pacientes: print(x, x.idade())

PacienteUI.main()