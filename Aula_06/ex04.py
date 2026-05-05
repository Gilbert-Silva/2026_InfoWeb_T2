# Modelo - Entidade
class Contato:
    def __init__(self, id, nome, email, fone):
        self.set_id(id)            # atributo de instância
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self.__id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError("Nome não pode ser vazio")
        self.__nome = nome
    def set_email(self, email): self.__email = email
    def set_fone(self, fone): self.__fone = fone
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_fone(self): return self.__fone
    def __str__(self): return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"

# Interface do Usuário
class ContatoUI:
    contatos = []    # lista de contatos - atributo de classe
    @staticmethod
    def main():
        op = 0
        while op != 6:
            op = ContatoUI.menu()
            if op == 1: ContatoUI.inserir()   # Create 
            if op == 2: ContatoUI.listar()    # Read
            if op == 3: ContatoUI.atualizar() # Update
            if op == 4: ContatoUI.excluir()   # Delete
            if op == 5: ContatoUI.pesquisar()

    @staticmethod
    def menu():
        print("1-Inserir 2-Listar 3-Atualizar 4-Excluir 5-Pesquisar 6-Fim")
        return int(input("Informe uma opção: "))    
    
    @classmethod
    def inserir(cls):
        # Lê os dados
        id = int(input("Informe o id do contato: "))
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o telefone: ")
        # Cria um novo objeto
        x = Contato(id, nome, email, fone)
        # Insere na lista
        cls.contatos.append(x)

    @classmethod
    def listar(cls):
        if len(cls.contatos) == 0: print("Nenhum contato inserido")
        else:
            for x in cls.contatos: print(x)

    @classmethod
    def listar_id(cls, id):
        # encontrar o contato com o id informado       
        for x in cls.contatos:
            if x.get_id() == id: return x
        # se não encontrar, retorna None
        return None    

    @classmethod
    def atualizar(cls):
        ContatoUI.listar()
        id = int(input("Informe o id do contato a ser atualizado: "))
        x = ContatoUI.listar_id(id)
        if x != None:
            # remove da lista o contato com o id informado
            cls.contatos.remove(x)
            # novos dados do contato
            nome = input("Informe o novo nome: ")
            email = input("Informe o novo e-mail: ")
            fone = input("Informe o novo telefone: ")
            # Cria um novo objeto
            x = Contato(id, nome, email, fone)
            # Insere na lista
            cls.contatos.append(x)
        else:
            print("Esse contato não existe")                

    @classmethod
    def excluir(cls):
        ContatoUI.listar()
        id = int(input("Informe o id do contato a ser excluído: "))
        x = ContatoUI.listar_id(id)
        if x != None:
            # remove da lista o contato com o id informado
            cls.contatos.remove(x)
        else:
            print("Esse contato não existe")                


    @classmethod
    def pesquisar(cls):
        iniciais = input("Informe as iniciais do nome: ")
        for x in cls.contatos:
            if x.get_nome().startswith(iniciais): print(x)

ContatoUI.main()
