import streamlit as st
import streamlit.components.v1 as components

# Sahifa sozlamalari
st.set_page_config(page_title="An1 TV", layout="wide")

st.title("📺 An1 TV")

# Kanallar (Bu yerga haqiqiy .m3u8 linklarini qo'yasan)
channels = {
    "Kanal 1": "https://test-streams.mux.dev/x36xhzz/x36xhzz.m3u8", # Bu test uchun link
    "Kanal 2": "https://...link_yozasan..."
}

# Sidebar
selected_channel = st.sidebar.selectbox("Kanalni tanlang:", list(channels.keys()))

# Pleer qismi
st.write(f"### Hozir efirda: {selected_channel}")

# HTML kodini o'zgaruvchiga olamiz
m3u8_link = channels[selected_channel]

# Bu yerda HLS.js kutubxonasini ishlatamiz, chunki oddiy brauzer .m3u8 ni to'g'ridan-to'g'ri ko'rsata olmaydi
html_code = f"""
<script src="https://cdn.jsdelivr.net/npm/hls.js@latest"></script>
<video id="video" width="100%" height="400" controls autoplay></video>
<script>
  var video = document.getElementById('video');
  var videoSrc = '{m3u8_link}';
  if (Hls.isSupported()) {{
    var hls = new Hls();
    hls.loadSource(videoSrc);
    hls.attachMedia(video);
  }} else if (video.canPlayType('application/vnd.apple.mpegurl')) {{
    video.src = videoSrc;
  }}
</script>
"""

# Komponentni chaqiramiz
components.html(html_code, height=450)
