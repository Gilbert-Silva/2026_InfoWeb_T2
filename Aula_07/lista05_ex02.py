from enum import Enum
from datetime import datetime

class Pagamento(Enum):
    EM_ABERTO = 1
    PAGO_PARCIAL = 2
    PAGO = 3

class Boleto:
    def __init__(self, cod, emissao, venc, valor):
        # atributos que serão validados
        self.set_cod_barras(cod)
        self.set_data_emissao(emissao)
        self.set_data_vencimento(venc)
        self.set_valor_boleto(valor)
        # atributos com valor inicial definido
        self.__data_pagamento = None
        self.__valor_pago = 0
        self.__situacao_pagamento = Pagamento.EM_ABERTO
    def set_cod_barras(self, cod):
        # supondo que o boleto deve ter 10 dígitos
        if len(cod) != 10: raise ValueError("Código deve ter 10 dígitos")
        self.__cod_barras = cod
    def set_data_emissao(self, emissao):
        if emissao > datetime.now(): raise ValueError("Data não pode estar no futuro")
        self.__data_emissao = emissao
    def set_data_vencimento(self, venc):
        #if venc < datetime.now(): raise ValueError("Data não pode estar no passado")
        self.__data_vencimento = venc
    def set_valor_boleto(self, valor):
        if valor < 0: raise ValueError("Valor não pode ser negativo")
        self.__valor_boleto = valor
    def pagar(self, valor_pago):
        if valor_pago < 0: raise ValueError("Valor não pode ser negativo")
        if self.__situacao_pagamento != Pagamento.EM_ABERTO: raise ValueError("Boleto já foi pago")
        self.__valor_pago = valor_pago
        self.__data_pagamento = datetime.now()
        if self.__valor_pago >= self.__valor_boleto: self.__situacao_pagamento = Pagamento.PAGO
        else: self.__situacao_pagamento = Pagamento.PAGO_PARCIAL
    def get_cod_barras(self): return self.__cod_barras
    def get_data_emissao(self): return self.__data_emissao
    def get_data_vencimento(self): return self.__data_vencimento
    def get_data_pagamento(self): return self.__data_pagamento
    def get_valor_boleto(self): return self.__valor_boleto
    def get_valor_pago(self): return self.__valor_pago
    def get_situacao_pagamento(self): return self.__situacao_pagamento
    # no diagrama get_situacao_pagamento está como situacao
    def situacao(self): return self.__situacao_pagamento
    def __str__(self):
        s = f"Boleto: {self.__cod_barras} - Emissão: {self.__data_emissao.strftime('%d/%m/%Y')} - "
        s += f"Vencimento: {self.__data_vencimento.strftime('%d/%m/%Y')}\n"
        s += f"Valor Boleto R$ {self.__valor_boleto:.2f} - "
        s += f"Valor Pago R$ {self.__valor_pago:.2f}\n"
        if self.__data_pagamento != None:
            s += f"Data de pagamento: {self.__data_pagamento.strftime('%d/%m/%Y')}\n"
        s += f"Situação: {self.__situacao_pagamento}"
        return s
    
class BoletoUI:
    __boletos = []
    @staticmethod
    def main():
        op = 0
        while op != 10:
            op = BoletoUI.menu()
            if op == 1: BoletoUI.inserir()
            if op == 2: BoletoUI.listar()
            if op == 8: BoletoUI.vencidos()
    @staticmethod
    def menu():
        print("---------------------------------------------")
        print(" 1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir ")
        print(" 5-Boletos em Aberto, 6-Boletos Pagos        ")
        print(" 7-Boletos a Vencer,  8-Boletos Vencidos     ")
        print(" 9-Pagar Boleto,      10-Fim                 ")
        print("---------------------------------------------")
        return int(input("Escolha uma opção: "))
    @classmethod
    def inserir(cls):
        cod = input("Informe o código com 10 dígitos: ")
        emissao = datetime.strptime(input("Informe a data de emissão dd/mm/yyyy: "), "%d/%m/%Y")
        venc = datetime.strptime(input("Informe a data de vencimento dd/mm/yyyy: "), "%d/%m/%Y")
        valor = float(input("Informe o valor: "))
        x = Boleto(cod, emissao, venc, valor)
        cls.__boletos.append(x)
    @classmethod
    def listar(cls):
        for x in cls.__boletos: print(x)
    @classmethod
    def vencidos(cls):
        for x in cls.__boletos: 
            if x.get_situacao_pagamento() == Pagamento.EM_ABERTO and \
                x.get_data_vencimento() < datetime.now(): print(x)

BoletoUI.main()




