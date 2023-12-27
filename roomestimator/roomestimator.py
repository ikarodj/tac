#roomestimator.py

import streamlit as st
from datetime import datetime

def calcular_quartos(etd, num_pax):
    hora = etd.time()

    # Valores correspondentes às células D26, E26, F26, G26, etc.
    # Ajuste estes valores com os dados reais da sua planilha
    valores = {
        ('00:59', '06:00'): [7, 14, 18, 22],  # Valores para madrugada
        ('06:01', '12:00'): [7, 14, 18, 22],  # Valores para manhã
        ('12:01', '18:00'): [7, 14, 18, 22],  # Valores para tarde
        ('18:01', '23:59'): [7, 14, 18, 22]   # Valores para noite
    }

    # Determinar o intervalo de tempo
    for (inicio, fim), quartos in valores.items():
        inicio = datetime.strptime(inicio, "%H:%M").time()
        fim = datetime.strptime(fim, "%H:%M").time()
        if inicio < hora <= fim:
            # Determinar o número de quartos com base no número de passageiros
            if num_pax <= 40:
                return quartos[0]
            elif num_pax <= 240:
                return quartos[1]
            elif num_pax <= 720:
                return quartos[2]
            elif num_pax <= 1440:
                return quartos[3]
            else:
                return "Erro: Número de passageiros excede o limite"

    return "Erro: Horário de partida não reconhecido."

def app():

# Código Streamlit
    st.title("Room Estimator")

    with st.form(key='my_form'):
        etd_str = st.text_input("Please enter the ETD Estimated Date and Time of Departure UTC (format DDMMYYYY HHMM):")
        num_pax = st.number_input("Please enter the total pax on the flight:", min_value=0, format="%d")
        submit_button = st.form_submit_button(label='Caulculate')

    if submit_button:
        try:
            etd = datetime.strptime(etd_str, '%d%m%Y %H%M')
            resultado = calcular_quartos(etd, num_pax)
            st.success(f"Estimated Number of Rooms to book for EZY Pax: {resultado}")
        except ValueError:
            st.error("Erro no formato da data/hora. Por favor, insira no formato DDMMYYYY HHMM.")
