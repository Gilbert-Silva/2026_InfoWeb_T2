from models.cliente import Cliente
import json

class ClienteDAO:
    def __init__(self):
        self.__arquivo = "clientes.json"
        self.__objetos = []
        self.__abrir()

    def inserir(self, obj):
        # Prova 1: para gerar um novo id automaticamente
        id = 0
        # encontrar o maior id atual
        if len(self.__objetos) > 0:
            for aux in self.__objetos:                         # laço    - 5
                if aux.get_id() > id: id = aux.get_id()        # teste   - 5
        #id = max(self.__objetos, key = lambda aux : aux.get_id)        
        obj.set_id(id + 1)                                     # novo id - 5

        # Prova 2: testar se um id já existe
        #for aux in self.__objetos:                            # laço  - 5
        #    if aux.get_id() == obj.get_id():                  # teste - 5
        #        raise ValueError("Id já existe")              # raise - 5

        self.__objetos.append(obj) # 5
        self.__salvar()            # 5

    def listar(self):                
        return self.__objetos

    def listar_id(self, id):
        for obj in self.__objetos:
            if obj.get_id() == id: return obj
        return None

    def atualizar(self, obj):
        aux = self.listar_id(obj.get_id())
        if aux != None:
            self.__objetos.remove(aux)
            self.__objetos.append(obj)
            self.__salvar()

    def excluir(self, id):
        aux = self.listar_id(id)
        if aux != None:
            self.__objetos.remove(aux)
            self.__salvar()

    def __abrir(self):  
        try:  
            arquivo = open(self.__arquivo, mode = "r")
            list_dic = json.load(arquivo)
            arquivo.close()
            self.__objetos = []
            for dic in list_dic:
                obj = Cliente.from_json(dic)
                self.__objetos.append(obj)
        except FileNotFoundError:
            pass

    def __salvar(self):    
        arquivo = open(self.__arquivo, mode = "w")
        json.dump(self.__objetos, arquivo, default = Cliente.to_json, indent = 2)
        arquivo.close()