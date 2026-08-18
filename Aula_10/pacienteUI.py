import streamlit as st
from paciente import Paciente
from datetime import date, datetime

class PacienteUI:
    def main():
        st.header("Dados do Paciente")
        nome = st.text_input("Nome")
        cpf = st.text_input("CPF")
        fone = st.text_input("Fone")
        nasc = st.date_input("Nascimento", min_value=date(1900, 1, 1),  \
            max_value=date.today(), value=date(2000, 1, 1), format="DD/MM/YYYY")
        nasc = datetime.combine(nasc, datetime.min.time())
        if st.button("Idade"):
            x = Paciente(nome, cpf, fone, nasc)
            st.write(x.idade())
