import streamlit as st
import sqlitecloud

st.title('The Baseball App')

st.image("https://en.wikipedia.org/wiki/Baseball_%28ball%29#/media/File:Baseball_(crop).jpg")

conn = sqlitecloud.connect("sqlitecloud://cgxs5yl7hk.sqlite.cloud:<your-host-port>?apikey=<your-api-key>")

cursor = conn.execute("SELECT * FROM albums WHERE AlbumId = ?", (1, ))
result = cursor.fetchone()

print(result)

conn.close()