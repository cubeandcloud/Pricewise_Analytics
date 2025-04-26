import streamlit as st
import os

# Sayfa Ayarları
st.set_page_config(page_title="Guess the Price - Real Estate Challenge", layout="centered")

# Logo gibi PH1 görseli
st.image("PH1.webp", caption=None, use_column_width=False, width=90)

# Başlık
st.markdown("""
# 👩‍🏠 Guess the Price - Real Estate Challenge
""", unsafe_allow_html=True)

# 🏡 House Features Bölümü
st.header("🏡 House Features")
st.markdown("""
- **Room Count**: 4 bedrooms, 3 bathrooms  
- **Living Area**: 165 m²  
- **Year Built**: 2007 (Renovated in 2015)  
- **Neighborhood**: Somerset, Ames, Iowa  
- **Garage**: 2-car garage (58 m²)  
- **Deck / Outdoor**: 26 m² deck + 9 m² patio  
""")

# PH2'den PH12'ye kadar olan fotoğrafları yükleme
for i in range(2, 13):
    filename = f"PH{i}.webp"
    caption = f"Photo {i}"

    if os.path.exists(filename):
        st.image(filename, caption=caption, use_container_width=True)
    else:
        st.warning(f"⚠️ Missing file: {filename}")

# 💸 Kullanıcıdan Fiyat Tahmini Al
st.subheader("💸 Enter Your Price Estimation")
user_price = st.number_input("Your estimation (in USD):", min_value=0, step=1000)

# 🎯 Gerçek Fiyat
real_price = 289000  # İstediğin gibi değiştirebilirsin

# Tahmin Sonucu
if st.button("🎯 Submit Your Guess"):
    diff = abs(user_price - real_price)

    if diff <= 5000:
        st.success("🏆 *Amazing!* You're almost spot on! Excellent market intuition!")
        st.image(
            "https://media.tenor.com/lW9bOeVpCs0AAAAC/that-is-the-best-answer-weve-had-simon-cowell.gif",
            caption="👏 Spot-on Guess!"
        )

    elif user_price < real_price:
        st.warning("📉 *A bit low!* You undervalued this property. It's worth more!")
        st.image(
            "https://media.tenor.com/YOtJ0DMyc6oAAAAC/office-the-insulting.gif",
            caption="😬 Oops, too low!"
        )

    else:
        st.warning("📈 *Too high!* Your guess went through the roof! 🏒💸")
        st.image(
            "https://media.tenor.com/UlD6LXPckBMAAAAC/very-high-gill-engvid.gif",
            caption="⏳ Might need a reality check..."
        )
