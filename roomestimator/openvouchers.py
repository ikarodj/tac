import streamlit as st

def app():

    st.title('Open Vouchers')
    st.header('UpLoad the file below in CSV format')
    
    user_csv = st.file_uploader("Upload your file here", type="csv")