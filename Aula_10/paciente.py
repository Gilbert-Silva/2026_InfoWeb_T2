from datetime import datetime

class Paciente:
    def __init__(self, nome, cpf, fone, nascimento):
        self.__nome = nome
        self.__cpf = cpf
        self.__fone = fone
        self.__nascimento = nascimento
    def __str__(self):
        return f"{self.__nome} - {self.__cpf} - {self.__fone} - {self.__nascimento.strftime('%d/%m/%Y')}" 
    def idade(self):
        x = datetime.now() - self.__nascimento
        dias = x.days
        anos = dias // 365
        meses = dias % 365 // 30
        return f"{anos} ano(s) e {meses} mes(es)"

