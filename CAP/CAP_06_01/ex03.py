class Produto: # A classe é um tipo de variável
    def __init__(self, id, nome, preco, avaliacao):  # método mágico
        self.set_id(id)
        self.set_nome(nome)
        self.set_preco(preco)
        self.set_avaliacao(avaliacao)
    def __str__(self):
        return f"Produto: {self.__id} - {self.__nome} - R${self.__preco:.2f} - {self.__avaliacao} estrela(s)"    
    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser positivo")
        self.__id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError("Nome não pode ser vazio")
        self.__nome = nome
    def set_preco(self, preco):
        if preco < 0: raise ValueError("Preço deve ser positivo")
        self.__preco = preco
    def set_avaliacao(self, avaliacao):
        if avaliacao < 1 or avaliacao > 5: 
            raise ValueError("Avaliação deve ser de 1 a 5")
        self.__avaliacao = avaliacao
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_preco(self): return self.__preco
    def get_avaliacao(self): return self.__avaliacao

class UI:
    def menu():
        print("1-Novo produto 2-Fim")
        return int(input("Escolha uma opção: "))
    
    def main():
        op = 0
        while op != 2:
            op = UI.menu()
            if op == 1: UI.novo_produto()

    def novo_produto():   
        id = int(input("Informe o id: ")) 
        nome = input("Informe o nome: ") 
        preco = float(input("Informe o preço: "))
        avalicao = int(input("Informe a avaliação: ")) 
        a = Produto(id, nome, preco, avalicao)
        print(a.get_id())
        print(a.get_nome())
        print(a.get_preco())
        print(a.get_avaliacao())
        print(a)

UI.main()



