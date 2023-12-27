# main.py 
import streamlit as st
from streamlit_option_menu import option_menu

# Importando as funções 'app' de cada módulo de página
import home  
import roomestimator
import cheetsheet 
import openvouchers 

# Add custom CSS to change the theme to dark mode
st.markdown("""
    <style>
    .stApp {
        background-color: #121212;
        color: #ffffff;
    }
    </style>
    """, unsafe_allow_html=True)


# Menu na barra lateral
with st.sidebar:
    selected = option_menu(
        menu_title="Menu",
        options=["Home", "Room Estimator", "Cheet Sheet", "Open Vouchers"],
        icons=["house", "calculator", "list-task", "envelope-open-fill"],
        menu_icon="cast",
        default_index=0
    )

    st.divider()

    st.caption("Developed by Icaro")

# Carrega a página correspondente
if selected == "Home":
    home.app()  # Chamando a função app() do módulo home
elif selected == "Room Estimator":
    roomestimator.app()  
elif selected == "Cheet Sheet":
    cheetsheet.app()  
elif selected == "Open Vouchers":
    openvouchers.app()  
