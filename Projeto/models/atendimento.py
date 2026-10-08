from datetime import datetime

class Atendimento:
    def __init__(self, id, data, queixa_principal, historico_saude, avaliacao, prescricao, id_horario):
        self.set_id(id)
        self.set_data(data)
        self.set_queixa_principal(queixa_principal)
        self.set_historico_saude(historico_saude)
        self.set_avaliacao(avaliacao)
        self.set_prescricao(prescricao)
        self.set_id_horario(id_horario)

    def __str__(self):
        return f"{self.__id} - {self.__data.strftime('%d/%m/%Y %H:%M')} - {self.__queixa_principal}"

    def get_id(self): return self.__id
    def get_data(self): return self.__data
    def get_queixa_principal(self): return self.__queixa_principal
    def get_historico_saude(self): return self.__historico_saude
    def get_avaliacao(self): return self.__avaliacao
    def get_prescricao(self): return self.__prescricao
    def get_id_horario(self): return self.__id_horario

    def set_id(self, id): self.__id = id
    def set_data(self, data): self.__data = data
    def set_queixa_principal(self, queixa_principal): self.__queixa_principal = queixa_principal
    def set_historico_saude(self, historico_saude): self.__historico_saude = historico_saude 
    def set_avaliacao(self, avaliacao): self.__avaliacao = avaliacao 
    def set_prescricao(self, prescricao): self.__prescricao = prescricao
    def set_id_horario(self, id_horario): self.__id_horario = id_horario

    def to_json(self):
        dic = {"id":self.__id, "data":self.__data.strftime("%d/%m/%Y %H:%M"), \
            "queixa_principal":self.__queixa_principal, "historico_saude":self.__historico_saude,   \
            "avaliacao":self.__avaliacao, "prescricao":self.__prescricao, "id_horario":self.__id_horario
        }
        return dic

    @staticmethod
    def from_json(dic):
        return Atendimento(dic["id"], datetime.strptime(dic["data"], "%d/%m/%Y %H:%M"), dic["queixa_principal"],\
                           dic["historico_saude"], dic["avaliacao"], dic["prescricao"], dic["id_horario"])
    
