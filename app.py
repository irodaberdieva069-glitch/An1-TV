import streamlit as st
import streamlit.components.v1 as components

# 1. Sahifa sozlamalari
st.set_page_config(page_title="An1 TV", page_icon="📺", layout="wide")

# 2. CSS - Dizaynni "chotki" qilish
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    .title { color: #ffffff; text-align: center; font-family: 'Arial', sans-serif; font-size: 40px; margin-bottom: 20px; }
    .footer { text-align: center; color: #888888; margin-top: 50px; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>📺 An1 TV</div>", unsafe_allow_html=True)

# 3. Kanallar ro'yxati (Bu yerda 'embed' linklardan foydalanamiz)
# Eslatma: Bular YouTube Live uchun 'embed' formatdagi linklar
channels = {
    "Sevimli TV": "https://www.youtube.com/embed/live_stream?channel=UCv4m51c4R86e24PqS_t3cRA",
    "Zo'r TV": "https://www.youtube.com/embed/live_stream?channel=UCQ5a73L9dY3O4_6O-f1_y0Q",
    "Milliy TV": "https://www.youtube.com/embed/live_stream?channel=UC5m_S0m-c-Y9QzW_R3j2N6A",
    "MTRK": "https://www.youtube.com/embed/live_stream?channel=UCZJ-g-o8Qn_33A0_O1P7Z9w"
}

# 4. Sidebar - Kanal tanlash
st.sidebar.header("Kanal tanlash")
selected_channel = st.sidebar.selectbox("Qaysi kanalni ko'ramiz?", list(channels.keys()))

# 5. Pleer qismi (Iframe orqali - eng stabil yo'l)
st.write(f"### Hozir efirda: {selected_channel}")

# Iframe kodini yaratish
player_html = f"""
<div style="background-color: black; border-radius: 15px; overflow: hidden;">
    <iframe width="100%" height="500" 
            src="{channels[selected_channel]}" 
            frameborder="0" 
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
            allowfullscreen>
    </iframe>
</div>
"""

# Komponentni sahifaga chiqarish
components.html(player_html, height=550)

# 6. Pastki qism
st.markdown("<div class='footer'>An1 TV © 2026 | Abdulaziz Nematov tomonidan</div>", unsafe_allow_html=True)
