import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")
st.title("📺 An1 TV - Sevimli Live")

# Sevimli TV ning to'g'ridan-to'g'ri iframe manzili (saytdan olingan)
sevimli_url = "https://www.youtube.com/embed/live_stream?channel=UCv4m51c4R86e24PqS_t3cRA"

# To'g'ridan-to'g'ri ko'rsatish
components.iframe(sevimli_url, height=500, scrolling=False)

st.write("Agar video qora bo'lsa, kanal hozir jonli efirda emas yoki YouTube efirni bloklagan.")
