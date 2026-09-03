import streamlit as st
import pandas as pd
from service import Service
import time
from datetime import datetime

class ManterHorarioUI:
    def main():
        st.header("Cadastro de Horários")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterHorarioUI.listar()
        with tab2: ManterHorarioUI.inserir()
        with tab3: ManterHorarioUI.atualizar()
        with tab4: ManterHorarioUI.excluir()

    def listar():
        horarios = Service.horario_listar()
        if len(horarios) == 0: st.write("Nenhum horário cadastrado")
        else:
            dic = []
            for obj in horarios:
                cliente = Service.cliente_listar_id(obj.get_id_cliente())
                servico = Service.servico_listar_id(obj.get_id_servico())
                if cliente != None: cliente = cliente.get_nome()
                if servico != None: servico = servico.get_descricao()
                dic.append({"id" : obj.get_id(), "data" : obj.get_data(),
                "confirmado" : obj.get_confirmado(), "cliente" : cliente,
                "serviço" : servico})
            df = pd.DataFrame(dic)
            st.dataframe(df)

    def inserir():
        clientes = Service.cliente_listar()
        servicos = Service.servico_listar()
        data = st.text_input("Informe a data e horário do serviço", datetime.now().strftime("%d/%m/%Y %H:%M"))
        confirmado = st.checkbox("Confirmado")
        cliente = st.selectbox("Informe o cliente", clientes, index = None)
        servico = st.selectbox("Informe o serviço", servicos, index = None)
        if st.button("Inserir"):
            id_cliente = None
            id_servico = None
            if cliente != None: id_cliente = cliente.get_id()
            if servico != None: id_servico = servico.get_id()
            Service.horario_inserir(datetime.strptime(data, "%d/%m/%Y %H:%M"), confirmado, id_cliente, id_servico)
            st.success("Horário inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        horarios = Service.horario_listar()
        if len(horarios) == 0: st.write("Nenhum horário cadastrado")
        else:
            clientes = Service.cliente_listar()
            servicos = Service.servico_listar()
            op = st.selectbox("Atualização de Horários", horarios)
            data = st.text_input("Informe a nova data e horário do serviço", op.get_data().strftime("%d/%m/%Y %H:%M"))
            confirmado = st.checkbox("Nova confirmação", op.get_confirmado())
            id_cliente = None if op.get_id_cliente() in [0, None] else op.get_id_cliente()
            id_servico = None if op.get_id_servico() in [0, None] else op.get_id_servico()
            cliente = st.selectbox("Informe o novo cliente", clientes, next((i for i, c in enumerate(clientes) if c.get_id() == id_cliente), None))
            servico = st.selectbox("Informe o novo serviço", servicos, next((i for i, s in enumerate(servicos) if s.get_id() == id_servico), None))
            if st.button("Atualizar"):
                id_cliente = None
                id_servico = None
                if cliente != None: id_cliente = cliente.get_id()
                if servico != None: id_servico = servico.get_id()
                Service.horario_atualizar(op.get_id(), datetime.strptime(data, "%d/%m/%Y %H:%M"), confirmado, id_cliente, id_servico)
                st.success("Horário atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        horarios = Service.horario_listar()
        if len(horarios) == 0: st.write("Nenhum horário cadastrado")
        else:
            op = st.selectbox("Exclusão de Horários", horarios)
            if st.button("Excluir"):
                Service.horario_excluir(op.get_id())
                st.success("Horário excluído com sucesso")
                time.sleep(2)
                st.rerun()