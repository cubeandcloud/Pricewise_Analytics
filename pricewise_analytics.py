import streamlit as st
import os
from PIL import Image

# Sayfa ayarları
st.set_page_config(page_title="Guess the Price - Real Estate Challenge", layout="centered")

# Başlık (2 satırlı, renkli)
st.markdown(
    """
    <div style='text-align: center;'>
        <h1 style='margin-bottom: 0; color: black;'>🏠 Guess the Price</h1>
        <h3 style='margin-top: 5px; color: green;'>Real Estate Challenge</h3>
    </div>
    """,
    unsafe_allow_html=True
)

# 🏡 House Features ve PH1 yan yana
st.header("🏡 House Features")
col1, col2 = st.columns([2, 1])  # 2:1 oranında genişlik

with col1:
    st.markdown("""
    - **Room Count**: 3 bedrooms, 2 bathrooms  
    - **Living Area**: 137 m²  
    - **Year Built**: 2003 (Renovated in 2009)  
    - **Neighborhood**: Northridge Heights, Ames, Iowa  
    - **Garage**: 2-car garage (57 m²)  
    - **Deck / Outdoor**: 24 m² deck + 7 m² patio  
    """)

with col2:
    if os.path.exists("PH1.webp"):
        img = Image.open("PH1.webp")
        width, height = img.size
        new_size = (width // 4, height // 4)
        img = img.resize(new_size)
        st.image(img)
    else:
        st.warning("⚠️ PH1.webp not found!")

# 📸 Fotoğrafları doğru açıklamalarla göster
# PH2 + PH3 yan yana
col1, col2 = st.columns(2)
with col1:
    if os.path.exists("PH2.webp"):
        st.image("PH2.webp", caption="📍 Location", use_container_width=True)
with col2:
    if os.path.exists("PH3.webp"):
        st.image("PH3.webp", caption="🏘️ Neighborhood", use_container_width=True)

# PH4 tek başına
if os.path.exists("PH4.webp"):
    st.image("PH4.webp", caption="🛋️ Living Room", use_container_width=True)

# PH10 tek başına
if os.path.exists("PH10.webp"):
    st.image("PH10.webp", caption="🍽️ Kitchen", use_container_width=True)

# PH5 tek başına
if os.path.exists("PH5.webp"):
    st.image("PH5.webp", caption="🛏️ Bedroom", use_container_width=True)

# PH6 + PH7 yan yana
col1, col2 = st.columns(2)
with col1:
    if os.path.exists("PH6.webp"):
        st.image("PH6.webp", caption="🛁 Bathroom", use_container_width=True)
with col2:
    if os.path.exists("PH7.webp"):
        st.image("PH7.webp", caption="🛏️ Bedrooms", use_container_width=True)

# PH8 tek başına
if os.path.exists("PH8.webp"):
    st.image("PH8.webp", caption="🛁 Bathroom", use_container_width=True)

# PH9 tek başına
if os.path.exists("PH9.webp"):
    st.image("PH9.webp", caption="🚗 Garage", use_container_width=True)

# PH11 + PH12 yan yana
col1, col2 = st.columns(2)
with col1:
    if os.path.exists("PH11.webp"):
        st.image("PH11.webp", caption="🏡 Exterior", use_container_width=True)
with col2:
    if os.path.exists("PH12.webp"):
        st.image("PH12.webp", caption="📐 Floor Plan", use_container_width=True)

# Kullanıcıdan isim alalım
st.subheader("🧑 Enter Your Name (Optional)")
user_name = st.text_input("Your name:")

if st.button("🎯 Make a Guess"):
    diff = abs(user_price - real_price)

    # Tahmini ve kullanıcı adını kaydet
    st.session_state.guesses.append({
        "name": user_name.strip(),  # Boşsa boş kalsın
        "guess": user_price,
        "diff": diff
    })

    # Tahmin sonucuna göre GIF ve mesaj
    if diff <= 5000:
        st.success("🎯 *So Close!* You're almost a real estate genius! 🧠💰")
        st.image("https://media4.giphy.com/media/KHKnSqATU08oS73LWi/giphy.gif", caption="🎯 Almost a perfect shot!")

    elif user_price < real_price:
        st.warning("📉 *Too Low!* You just undersold a hidden gem!\nAim higher next time 💎")
        st.image("https://media1.giphy.com/media/26uf14WIlvzuZkKLS/giphy.gif", caption="📉 That was a steal... for someone else!")

    else:
        st.warning("📈 *Too High!* Whoa, that's a skyscraper price! 🏢\nAt this price, the house might still be on sale when you retire 😅")
        st.image("https://media2.giphy.com/media/l0G1700P94aQRbMpW/giphy.gif", caption="📈 Way above the clouds!")



# 📸 En alta kapanış için tekrar PH1 resmi ve teşekkür mesajı
st.markdown("---")  # Ayırıcı çizgi

if os.path.exists("PH1.webp"):
    img = Image.open("PH1.webp")
    width, height = img.size
    new_size = (width // 2, height // 2)
    img = img.resize(new_size)

    st.image(img, use_container_width=False)

    st.markdown(
        """
        <h4 style="text-align: center; color: grey;">🏠 Thank you for visiting!</h4>
        """,
        unsafe_allow_html=True
    )
else:
    st.warning("⚠️ PH1.webp not found at the end!")
