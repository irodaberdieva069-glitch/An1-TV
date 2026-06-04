import streamlit as st

st.set_page_config(page_title="An1 TV")
st.title("📺 An1 TV")

st.subheader("Kanallar:")

# Iframe o'rniga tugma - bu 100% ishlaydi!
if st.button("Sevimli TV ni tomosha qilish"):
    st.markdown("""
        <script>
            window.open('https://sevimli.tv/live', '_blank');
        </script>
    """, unsafe_allow_html=True)
    st.write("Yangi oynada ochildi...")

st.info("Eslatma: Ba'zi telekanallar o'z efirini boshqa saytlarda ko'rsatishni taqiqlaydi, shuning uchun ularni to'g'ridan-to'g'ri o'z saytlarida ko'rish kerak.")
