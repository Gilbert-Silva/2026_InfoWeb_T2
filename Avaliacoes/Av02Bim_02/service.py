from models.cliente import Cliente
from models.clientedao import ClienteDAO
from models.servico import Servico
from models.servicodao import ServicoDAO
from datetime import datetime, timedelta

class Service:
    @staticmethod
    def cliente_inserir(id, nome, email, fone, data_cadastro):  # 5
        obj = Cliente(id, nome, email, fone, data_cadastro)
        ClienteDAO().inserir(obj)
    @staticmethod
    def cliente_listar():
        return ClienteDAO().listar()
    @staticmethod
    def cliente_listar_id(id):
        return ClienteDAO().listar_id(id)
    @staticmethod
    def cliente_atualizar(id, nome, email, fone, data_cadastro): # 5
        obj = Cliente(id, nome, email, fone, data_cadastro)
        ClienteDAO().atualizar(obj)
    @staticmethod
    def cliente_excluir(id):
        ClienteDAO().excluir(id)
    @staticmethod
    def cliente_listar_novos():
        sm = timedelta(days = 180)
        r = []                                                         # 3
        for aux in Service.cliente_listar():                           # 3
            if aux.get_data_cadastro() > (datetime.now() - sm):        # 3
                r.append(aux)                                          # 3
        return r                                                       # 3

    @staticmethod
    def servico_inserir(id, descricao, valor):
        obj = Servico(id, descricao, valor)
        ServicoDAO().inserir(obj)
    @staticmethod
    def servico_listar():
        return ServicoDAO().listar()
    @staticmethod
    def servico_listar_id(id):
        return ServicoDAO().listar_id(id)
    @staticmethod
    def servico_atualizar(id, descricao, valor):
        obj = Servico(id, descricao, valor)
        ServicoDAO().atualizar(obj)
    @staticmethod
    def servico_excluir(id):
        ServicoDAO().excluir(id)
