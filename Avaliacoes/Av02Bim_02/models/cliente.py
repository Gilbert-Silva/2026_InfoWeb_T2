from datetime import datetime

class Cliente:
    def __init__(self, id, nome, email, fone, data_cadastro):  # 5
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
        self.set_data_cadastro(data_cadastro)
   
    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self.__id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError("Nome deve ser informado")
        self.__nome = nome
    def set_email(self, email):
        if email == "": raise ValueError("E-mail deve ser informado")
        self.__email = email
    def set_fone(self, fone):
        if fone == "": raise ValueError("Fone deve ser informado")
        self.__fone = fone
    def set_data_cadastro(self, data):  # 5
        if data >= datetime.now(): raise ValueError("Data deve estar no passado")
        self.__data_cadastro = data

    def get_id(self) : return self.__id
    def get_nome(self) : return self.__nome
    def get_email(self) : return self.__email
    def get_fone(self) : return self.__fone
    def get_data_cadastro(self) : return self.__data_cadastro # 2,5

    def __str__(self): # 2,5
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone} - {self.__data_cadastro.strftime('%d/%m/%Y')}"
   
    def to_json(self): # 5
        return { "id":self.__id, "nome":self.__nome, "email":self.__email, "fone":self.__fone, "data_cadastro":self.__data_cadastro.strftime('%d/%m/%Y') }
   
    @staticmethod
    def from_json(dic): # 5
        return Cliente(dic["id"], dic["nome"], dic["email"], dic["fone"], datetime.strptime(dic["data_cadastro"], '%d/%m/%Y'))
    
# Sobrecarga de método

#x = Cliente(1, "nome1", "email1", "fone1")   # Cliente.__init__()
#y = Cliente.from_json({ "id":1, "nome":"nome1", "email":"email1", "fone":"fone1" })