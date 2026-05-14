class Disciplina:
    def __init__(self, id, nome, professor, media):
        self.set_id(id)
        self.set_nome(nome)
        self.set_professor(professor)
        self.set_media(media)
    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__professor} - {self.__media}"    
    def set_id(self, id):
        if id < 0: raise ValueError("Id deve ser um valor positivo")
        self.__id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError("Nome não pode ser vazio")
        self.__nome = nome
    def set_professor(self, professor):
        if professor == "": raise ValueError("Professor não pode ser vazio")
        self.__professor = professor
    def set_media(self, media):  
        if media < 0 or media > 100: raise ValueError("Média deve ser um valor entre 0 e 100")
        self.__media = media
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_professor(self): return self.__professor
    def get_media(self): return self.__media

class UI:
    __lista = []
    @staticmethod
    def main():
        op = 0
        while op != 4:
            op = UI.menu()
            if op == 1: UI.inserir()
            if op == 2: UI.listar()
            if op == 3: UI.media()

    @staticmethod
    def menu():
        print("1-Inserir 2-Listar 3-Média 4-Sair")
        return int(input("Escolha uma opção: "))

    @classmethod
    def inserir(cls):
        id = int(input("Informe o id da disciplina: "))
        nome = input("Informe o nome: ")
        prof = input("Informe o professor: ")
        media = int(input("Informe a média entre 0 e 100: "))
        x = Disciplina(id, nome, prof, media)
        cls.__lista.append(x)

    @classmethod
    def listar(cls):
        for x in cls.__lista: print(x)

    @classmethod
    def media(cls):    
        soma = 0
        for x in cls.__lista: 
            soma += x.get_media()
        if len(cls.__lista) == 0: print(0)
        else: print(soma/len(cls.__lista))     

UI.main()


# Q1 - Atributos - 6
#    - Init      - 6
#    - Validação - 6
#    - Set/Get   - 6
#    - Str       - 6

# Q2 - Main + Lista - 8
#    - Menu         - 8
#    - Inserir      - 8
#    - Listar       - 8
#    - Media        - 8

# Q3 - Atributos - 3
#    - Métodos   - 3
#    - Parâmetros- 3
#    - Retorno   - 3
#    - Visibilidade - 3

