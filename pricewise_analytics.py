import streamlit as st
import os
from PIL import Image

# Sayfa Ayarları
st.set_page_config(page_title="Guess the Price - Real Estate Challenge", layout="centered")

# 📸 PH1 görselini yükle ve küçült
if os.path.exists("PH1.webp"):
    img = Image.open("PH1.webp")
    width, height = img.size
    new_size = (width // 4, height // 4)  # 4'te 1 küçültme
    img = img.resize(new_size)

    # İkisini yan yana koymak için iki kolon kullanıyoruz
    col1, col2 = st.columns([4, 1])

    with col1:
        st.markdown("<h1 style='text-align: right;'>🏠 Guess the Price</h1>", unsafe_allow_html=True)

    with col2:
        st.image(img)
else:
    st.warning("⚠️ PH1.webp bulunamadı!")

# 🏡 House Features Bölümü
st.header("🏡 House Features")
st.markdown("""
- **Room Count**: 3 bedrooms, 2 bathrooms  
- **Living Area**: 137 m²  
- **Year Built**: 2003 (Renovated in 2009)  
- **Neighborhood**: Northridge Heights, Ames, Iowa  
- **Garage**: 2-car garage (57 m²)  
- **Deck / Outdoor**: 24 m² deck + 7 m² patio  
""")

# 📸 Fotoğrafları belirli düzende yükle
# PH2 ve PH3 yan yana
col1, col2 = st.columns(2)
with col1:
    if os.path.exists("PH2.webp"):
        st.image("PH2.webp", caption="Photo 2", use_column_width=True)
    else:
        st.warning("⚠️ PH2.webp bulunamadı!")

with col2:
    if os.path.exists("PH3.webp"):
        st.image("PH3.webp", caption="Photo 3", use_column_width=True)
    else:
        st.warning("⚠️ PH3.webp bulunamadı!")

# PH4 tek başına
if os.path.exists("PH4.webp"):
    st.image("PH4.webp", caption="Photo 4", use_column_width=True)
else:
    st.warning("⚠️ PH4.webp bulunamadı!")

# PH5 tek başına
if os.path.exists("PH5.webp"):
    st.image("PH5.webp", caption="Photo 5", use_column_width=True)
else:
    st.warning("⚠️ PH5.webp bulunamadı!")

# PH6 ve PH7 yan yana
col1, col2 = st.columns(2)
with col1:
    if os.path.exists("PH6.webp"):
        st.image("PH6.webp", caption="Photo 6", use_column_width=True)
    else:
        st.warning("⚠️ PH6.webp bulunamadı!")

with col2:
    if os.path.exists("PH7.webp"):
        st.image("PH7.webp", caption="Photo 7", use_column_width=True)
    else:
        st.warning("⚠️ PH7.webp bulunamadı!")

# PH8 tek başına
if os.path.exists("PH8.webp"):
    st.image("PH8.webp", caption="Photo 8", use_column_width=True)
else:
    st.warning("⚠️ PH8.webp bulunamadı!")

# PH9 tek başına
if os.path.exists("PH9.webp"):
    st.image("PH9.webp", caption="Photo 9", use_column_width=True)
else:
    st.warning("⚠️ PH9.webp bulunamadı!")

# PH11 ve PH12 yan yana
col1, col2 = st.columns(2)
with col1:
    if os.path.exists("PH11.webp"):
        st.image("PH11.webp", caption="Photo 11", use_column_width=True)
    else:
        st.warning("⚠️ PH11.webp bulunamadı!")

with col2:
    if os.path.exists("PH12.webp"):
        st.image("PH12.webp", caption="Photo 12", use_column_width=True)
    else:
        st.warning("⚠️ PH12.webp bulunamadı!")

# 💸 Kullanıcıdan Fiyat Tahmini Al
st.subheader("💸 Enter Your Price Guess")
user_price = st.number_input("Your guess (in USD):", min_value=0, step=1000)

# 🎯 Gerçek Fiyat (Doğru: 214000)
real_price = 214000

if st.button("🎯 Make a Guess"):
    diff = abs(user_price - real_price)

    if diff <= 5000:
        st.success("🏆 *Incredible!* You guessed almost spot on!\nYou must have a sixth sense for real estate deals 🧠💰")
        st.image(
            "https://media.tenor.com/lW9bOeVpCs0AAAAC/that-is-the-best-answer-weve-had-simon-cowell.gif",
            caption="👏 Perfect answer!"
        )
    elif user_price < real_price:
        st.warning("📉 *Too Low!* You just undersold a gem!\nThis house is more valuable than that 💎")
        st.image(
            "https://media.tenor.com/YOtJ0DMyc6oAAAAC/office-the-insulting.gif",
            caption="😬 That was a bit insulting..."
        )
    else:
        st.warning("📈 *Too High!* Whoa! That’s a sky-high guess! 💸\nAt that price, the house might still be on sale when you’re retired 😅")
        st.image(
            "https://media.tenor.com/UlD6LXPckBMAAAAC/very-high-gill-engvid.gif",
            caption="⏳ Hope you're patient..."
        )
