import streamlit as st
import plotly.express as px
import pandas.io.sql as sqlio
from classes.tab import Tab

class TransactionVolume(Tab):

    def get_data(self, start: int, end: int):
        query = """
            SELECT 
                block_number,
                count(*) 
            FROM public.transactions
            WHERE block_number BETWEEN {} AND {}
            GROUP BY block_number
        """.format(start, end)
        df = sqlio.read_sql_query(con=self.db_connection, sql=query)
        return df

    def create_graph(self, df):
        df.columns = ["Block Number", "Transaction Count"]
        fig = px.line(df, x="Block Number", y="Transaction Count", title="Transactions Per Block")
        return fig

    def fill_tab(self):
        try:
            start = st.number_input(
                label="Start Block Number", 
                min_value=1, 
                step=1,
            )   
            end = st.number_input(
                label="End Block Number", 
                min_value=start+1, 
                step=1,
            )

            if not start or not end:
                st.error("Pick a start and end block for transaction visualisation")
            else:
                df = self.get_data(start, end)
                fig = self.create_graph(df)
                st.plotly_chart(fig)
        except:
            st.error("Error building graph")
