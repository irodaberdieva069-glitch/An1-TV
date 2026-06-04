import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

st.title("📺 Sevimli TV - To'g'ridan-to'g'ri")

# Bu Sevimli TV ning o'z saytidagi rasmiy pleer manzili
# Ushbu kod sayt pleerini to'g'ridan-to'g'ri chaqiradi
player_code = """
<div style="width: 100%; height: 500px; background-color: #000;">
    <iframe src="https://sevimli.tv/live" 
            width="100%" height="100%" 
            frameborder="0" 
            allowfullscreen>
    </iframe>
</div>
"""

components.html(player_code, height=520)

st.info("Agar qora ekran chiqsa, brauzeringiz 'Cross-Origin' (CORS) cheklovini yoqib qo'ygan bo'lishi mumkin.")
