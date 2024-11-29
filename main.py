import streamlit as st
import sqlitecloud

st.title('The Baseball App')

st.image("https://en.wikipedia.org/wiki/Baseball_%28ball%29#/media/File:Baseball_(crop).jpg")

apikey= st.secrets("APIKEY")
print(apikey)
# conn = sqlitecloud.connect(f"sqlitecloud://cgxs5yl7hk.sqlite.cloud:8860?apikey={apikey}")

# cursor = conn.execute("SELECT * FROM albums WHERE AlbumId = ?", (1, ))
# result = cursor.fetchone()

# print(result)

# conn.close()