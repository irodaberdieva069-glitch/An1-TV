import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="An1 TV", layout="wide")

st.title("📺 An1 TV")

# Bu yerga to'g'ridan-to'g'ri .m3u8 linkini qo'yasan
# Telecom TV yoki boshqa IPTV kanallar shunaqa link beradi
channels = {
    "Sevimli": "https://cdn.example.com/live/sevimli.m3u8", 
    "Zo'r TV": "https://cdn.example.com/live/zortv.m3u8"
}

channel = st.sidebar.selectbox("Kanalni tanlang:", list(channels.keys()))
link = channels[channel]

# Professional Pleer (HLS.js orqali)
player_html = f"""
<!DOCTYPE html>
<html>
<head>
    <script src="https://cdn.jsdelivr.net/npm/hls.js@latest"></script>
</head>
<body>
    <video id="video" width="100%" height="450" controls autoplay style="background:black;"></video>
    <script>
        var video = document.getElementById('video');
        var videoSrc = '{link}';
        var hls = new Hls();
        hls.loadSource(videoSrc);
        hls.attachMedia(video);
        hls.on(Hls.Events.MANIFEST_PARSED, function() {{ video.play(); }});
    </script>
</body>
</html>
"""

components.html(player_html, height=470)
