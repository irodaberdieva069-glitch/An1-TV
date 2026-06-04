import streamlit as st
import streamlit.components.v1 as components

# Sahifa sozlamalari
st.set_page_config(page_title="An1 TV", layout="wide")

# Kanallar lug'ati - shu yerga istalgan linkni qo'shasan
channels = {
    "Sevimli TV": "https://www.youtube.com/embed/live_stream?channel=UCv4m51c4R86e24PqS_t3cRA",
    "Test Stream (HLS)": "https://test-streams.mux.dev/x36xhzz/x36xhzz.m3u8" 
}

# Sidebar
selected = st.sidebar.selectbox("Kanal tanlash:", list(channels.keys()))
url = channels[selected]

st.title(f"📺 An1 TV | {selected}")

# Universal pleer (Ham YouTube, ham .m3u8 uchun)
html_code = f"""
<div id="player-container" style="background:black; border-radius:10px; overflow:hidden;">
    <iframe id="frame" width="100%" height="500px" src="{url}" frameborder="0" allowfullscreen></iframe>
</div>
<script src="https://cdn.jsdelivr.net/npm/hls.js@latest"></script>
<script>
    var url = "{url}";
    if (url.endsWith('.m3u8')) {{
        document.getElementById('frame').remove();
        var vid = document.createElement('video');
        vid.width = window.innerWidth;
        vid.height = 500;
        vid.controls = true;
        vid.autoplay = true;
        document.getElementById('player-container').appendChild(vid);
        var hls = new Hls();
        hls.loadSource(url);
        hls.attachMedia(vid);
    }}
</script>
"""

components.html(html_code, height=520)

st.sidebar.info("Dasturchi: Abdulaziz Nematov")
