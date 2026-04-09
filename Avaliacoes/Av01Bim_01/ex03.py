class Aluno:
    def init(self):
        self.nome = ""                     # 5 pontos
        self.matricula = ""                # 5 pontos
    def ano_ingresso(self):
        return int(self.matricula[:4])     # 10 pontos
    
x = Aluno()                                # 6 pontos
x.nome = input("Informe o nome: ")
x.matricula = input("Informe a matrícula: ")    
ano = x.ano_ingresso()
print(f"Ano de ingresso {ano}")