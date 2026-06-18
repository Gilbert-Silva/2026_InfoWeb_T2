import json

class Cliente:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
    def __str__(self):
        return f"{self.id} - {self.nome}"
    def to_json(self):
        return { "id" : self.id, "nome" : self.nome }
    @staticmethod
    def from_json(dic):
        return Cliente(dic["id"], dic["nome"])
    
def salvar():
    a = Cliente(1, "Douglas Crockford")
    b = Cliente(2, "Jon Bosak")
    c = Cliente.from_json({ "id" : 3, "nome" : "Alan Turing" })   
    lista = [a, b, c]
    arquivo = open("clientes.json", mode="w")
    json.dump(lista, arquivo, default = Cliente.to_json, indent = 2)
    arquivo.close()
    print(a)
    print(b)
    print(c)
    print(a.__dict__)
    print(b.__dict__)
    print(c.__dict__)

def abrir():
    arquivo = open("clientes.json", mode="r")
    list_dic = json.load(arquivo) 
    for dic in list_dic:
        x = Cliente.from_json(dic)
        print(x)

#salvar()
abrir()





  