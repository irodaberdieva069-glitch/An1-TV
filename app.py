import streamlit as st

st.set_page_config(page_title="An1 TV", layout="wide")
st.title("📺 An1 TV")

# Bu yerga to'g'ridan-to'g'ri kanalning o'zi ochiladigan sahifa linkini qo'y
# Masalan, telekanallar o'z saytida jonli efirni qayerda ko'rsatsa, o'sha link
embed_link = "https://www.youtube.com/embed/live_stream?channel=CHANNEL_ID" 

st.components.v1.iframe(embed_link, height=500)
