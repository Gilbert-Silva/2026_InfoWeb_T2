import json

class Cliente:
    def __init__(self, id, nome, email, fone):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)

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

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_fone(self): return self.__fone

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"

    def to_json(self):
        return { "id":self.__id, "nome":self.__nome, "email":self.__email, "fone":self.__fone }

    @staticmethod
    def from_json(dic):
        return Cliente(dic["id"], dic["nome"], dic["email"], dic["fone"])
    
class ClienteUI:
    __objetos = []  # lista de objetos (clientes)  
    @staticmethod     
    def main():
        ClienteUI.abrir()
        op = 0
        while op != 9:
            op = ClienteUI.menu()
            if op == 1: ClienteUI.inserir()
            if op == 2: ClienteUI.listar()
            if op == 3: ClienteUI.atualizar()
            if op == 4: ClienteUI.excluir()

    @staticmethod
    def menu():
        print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir, 9-Fim")
        return int(input("Escolha uma opção: "))
    
    @classmethod
    def salvar(cls):    
        arquivo = open("clientes.json", mode = "w")
        json.dump(cls.__objetos, arquivo, default = Cliente.to_json, indent = 2)
        arquivo.close()
        print("O arquivo clientes.json foi salvo") 

    @classmethod
    def abrir(cls):
        try:         
            arquivo = open("clientes.json", mode = "r")
            list_dic = json.load(arquivo)
            arquivo.close()
            cls.__objetos = []
            for dic in list_dic:
                x = Cliente.from_json(dic)
                cls.__objetos.append(x)
            print("O arquivo clientes.json foi aberto") 
        except FileNotFoundError: # Acontece qdo o arquivo não existe
            pass                  # não faz nada 

    @classmethod      # quando acessa o atributo - usa o cls
    def inserir(cls):
        id = int(input("Informe o id: "))
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o telefone: ")
        x = Cliente(id, nome, email, fone)
        cls.__objetos.append(x)
        ClienteUI.salvar()

    @classmethod
    def listar(cls):
        if len(cls.__objetos) == 0: print("Nenhum cliente cadastrado")
        else:
            for x in cls.__objetos: print(x)

    @classmethod
    def atualizar(cls):
        for x in cls.__objetos: print(x)
        id = int(input("Informe o id do cliente a ser atualizado: "))
        for x in cls.__objetos:
            if x.get_id() == id:
                nome = input("Informe o novo nome: ")
                email = input("Informe o novo e-mail: ")
                fone = input("Informe o novo telefone: ")
                x.set_nome(nome)
                x.set_email(email)
                x.set_fone(fone)
                ClienteUI.salvar()

    @classmethod
    def excluir(cls):
        for x in cls.__objetos: print(x)
        id = int(input("Informe o id do cliente a ser excluído: "))
        for x in cls.__objetos:
            if x.get_id() == id:
                cls.__objetos.remove(x)
                ClienteUI.salvar()

ClienteUI.main()
