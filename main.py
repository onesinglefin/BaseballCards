import streamlit as st
import sqlitecloud
import pandas as pd

st.title('The Baseball App')

apikey= st.secrets.APIKEY
conn = sqlitecloud.connect(f"sqlitecloud://cgxs5yl7hk.sqlite.cloud:8860?apikey={apikey}")

cursor = conn.execute("USE DATABASE baseball_card_app")

result = cursor.fetchall()

albums = pd.read_sql("SELECT * FROM card_list LIMIT 10", conn)

st.dataframe(albums, hide_index=True)

conn.close()
