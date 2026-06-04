import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="An1 TV", layout="wide")

st.title("📺 An1 TV - Live Stream")

# Bu yerda .m3u8 emas, balki o'sha kanalning 
# Telecom TV yoki boshqa saytdagi 'Embed' linki bo'lishi kerak.
# Misol uchun: 
embed_url = "https://telecomtv.uz/embed/channel_id" 

components.iframe(embed_url, height=500, scrolling=False)
