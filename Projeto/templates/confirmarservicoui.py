import streamlit as st
import pandas as pd
from service import Service
import time
from datetime import datetime

class ConfirmarServicoUI:
    def main():
        st.header("Confirmar Serviço")
        horarios = Service.horario_confirmar_servico(st.session_state["usuario_id"])
        if len(horarios) == 0: st.write("Nenhum horário cadastrado")
        else:
            clientes = Service.cliente_listar()
            servicos = Service.servico_listar()
            profissionais = Service.profissional_listar()
            op = st.selectbox("Informe o horário", horarios)
            id_cliente = None if op.get_id_cliente() in [0, None] else op.get_id_cliente()
            cliente = st.selectbox("Cliente", clientes, next((i for i, c in enumerate(clientes) if c.get_id() == id_cliente), None), disabled = True)
            if st.button("Confirmar"):
                id_cliente = None
                if cliente != None: id_cliente = cliente.get_id()
                Service.horario_atualizar(op.get_id(), op.get_data(), True, id_cliente, op.get_id_servico(), op.get_id_profissional())
                st.success("Horário confirmado com sucesso")
                time.sleep(2)
                st.rerun()

