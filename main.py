import streamlit as st
import sqlitecloud

st.title('The Baseball App')

apikey= st.secrets.APIKEY
conn = sqlitecloud.connect(f"sqlitecloud://cgxs5yl7hk.sqlite.cloud:8860?apikey={apikey}")

cursor = conn.execute("USE DATABASE chinook.sqlite; SELECT * FROM employees")
result = cursor.fetchall()

st.write(result)
st.write("something should appear above this")
# print(result)

conn.close()