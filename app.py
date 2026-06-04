import streamlit as st
from streamlit_player import st_player

# 1. Sahifa sozlamalari
st.set_page_config(page_title="An1 TV", page_icon="📺", layout="wide")

# 2. CSS orqali interfeysni "chotki" qilish
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    h1 { color: #ff4b4b; text-align: center; font-family: sans-serif; }
    .stSelectbox { border-radius: 10px; }
    </style>
""", unsafe_allow_html=True)

# 3. Sarlavha
st.title("📺 An1 TV")
st.markdown("<p style='text-align: center;'>O'zbekistonning eng sara kanallari bir manzilda</p>", unsafe_allow_html=True)

# 4. Kanallar ro'yxati (Bu yerga YouTube jonli efir linklarini qo'yasan)
channels = {
    "Sevimli TV": "https://www.youtube.com/watch?v=S25r_Y5gL7I",
    "Zo'r TV": "https://www.youtube.com/watch?v=...",
    "Milliy TV": "https://www.youtube.com/watch?v=...",
    "MTRK": "https://www.youtube.com/watch?v=..."
}

# 5. Navigatsiya (Yon menyu)
st.sidebar.header("Kanal tanlash")
selected_channel = st.sidebar.selectbox("Qaysi kanalni ko'ramiz?", list(channels.keys()))

# 6. Pleer qismi
st.write(f"### Hozir efirda: {selected_channel}")

# Pleer funksiyasi
try:
    st_player(channels[selected_channel], height=450)
except:
    st.error("Ushbu kanalning efiri hozircha mavjud emas.")

# 7. Pastki qism (Footer)
st.markdown("---")
st.sidebar.markdown("---")
st.sidebar.write("An1 TV © 2026")
st.sidebar.write("Dasturchi: **Abdulaziz Nematov**")
