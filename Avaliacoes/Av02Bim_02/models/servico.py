class Servico:
    def __init__(self, id, descricao, valor):
        self.set_id(id)
        self.set_descricao(descricao)
        self.set_valor(valor)
   
    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self.__id = id
    def set_descricao(self, descricao):
        if descricao == "": raise ValueError("Descrição deve ser informada")
        self.__descricao = descricao
    def set_valor(self, valor):
        if valor < 0: raise ValueError("Valor deve ser positivo")
        self.__valor = valor

    def get_id(self) : return self.__id
    def get_descricao(self) : return self.__descricao
    def get_valor(self) : return self.__valor

    def __str__(self):
        return f"{self.__id} - {self.__descricao} - {self.__valor}"
   
    def to_json(self):
        return { "id":self.__id, "descricao":self.__descricao, "valor":self.__valor }
   
    @staticmethod
    def from_json(dic):
        return Servico(dic["id"], dic["descricao"], dic["valor"])