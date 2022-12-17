import streamlit as st
from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv()

    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.write("# Canto Chain Visualisation")

    st.sidebar.success("Select a visualisation")
