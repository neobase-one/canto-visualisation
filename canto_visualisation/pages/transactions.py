import streamlit as st
from transactions.transaction_volume import TransactionVolume
from transactions.gas import GasUsed

tab1, tab2 = st.tabs([
    "Transaction Volume",
    "Gas Volume",
])

with tab1:
   tab = TransactionVolume()
   tab.fill_tab()

with tab2:
   tab = GasUsed()
   tab.fill_tab()
