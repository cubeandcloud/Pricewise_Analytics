import streamlit as st
import os
from PIL import Image

# Sayfa ayarları
st.set_page_config(page_title="Guess the Price - Real Estate Challenge", layout="centered")

# 🧠 Session State: Tahmin geçmişi tutmak için
if "guesses" not in st.session_state:
    st.session_state.guesses = []

# --- Sidebar Menü ---
page = st.sidebar.selectbox(
    "Select Page",
    ("🏠 Play Game", "📊 Admin Panel")
)

# 🎯 Gerçek Fiyat
real_price = 214000

# --- Play Game Sayfası ---
if page == "🏠 Play Game":

    # --- Başlık ---
    st.markdown(
        """
        <div style='text-align: center;'>
            <h1 style='margin-bottom: 0; color: black;'>🏠 Guess the Price</h1>
            <h3 style='margin-top: 5px; color: green;'>Real Estate Challenge</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    # --- House Features ---
    st.header("🏡 House Features")
    col1, col2 = st.columns([2, 1])

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
            img = img.resize((img.width // 4, img.height // 4))
            st.image(img)
        else:
            st.warning("⚠️ PH1.webp not found!")

    # 📸 Fotoğraflar
    col1, col2 = st.columns(2)
    with col1:
        if os.path.exists("PH2.webp"):
            st.image("PH2.webp", caption="📍 Location", use_container_width=True)
    with col2:
        if os.path.exists("PH3.webp"):
            st.image("PH3.webp", caption="🏘️ Neighborhood", use_container_width=True)

    if os.path.exists("PH4.webp"):
        st.image("PH4.webp", caption="🛋️ Living Room", use_container_width=True)
    if os.path.exists("PH10.webp"):
        st.image("PH10.webp", caption="🍽️ Kitchen", use_container_width=True)
    if os.path.exists("PH5.webp"):
        st.image("PH5.webp", caption="🛏️ Bedroom", use_container_width=True)

    col1, col2 = st.columns(2)
    with col1:
        if os.path.exists("PH6.webp"):
            st.image("PH6.webp", caption="🛁 Bathroom", use_container_width=True)
    with col2:
        if os.path.exists("PH7.webp"):
            st.image("PH7.webp", caption="🛏️ Bedrooms", use_container_width=True)

    if os.path.exists("PH8.webp"):
        st.image("PH8.webp", caption="🛁 Bathroom", use_container_width=True)
    if os.path.exists("PH9.webp"):
        st.image("PH9.webp", caption="🚗 Garage", use_container_width=True)

    col1, col2 = st.columns(2)
    with col1:
        if os.path.exists("PH11.webp"):
            st.image("PH11.webp", caption="🏡 Exterior", use_container_width=True)
    with col2:
        if os.path.exists("PH12.webp"):
            st.image("PH12.webp", caption="📐 Floor Plan", use_container_width=True)

    # --- Kullanıcı Girişleri ---
    st.subheader("👨👩 Enter Your Name (Optional)")
    user_name = st.text_input("Your name:")

    st.subheader("💸 Enter Your Price Guess")
    user_price = st.number_input("Your guess (in USD):", min_value=0, step=1000)

    if st.button("🎯 Make a Guess"):

        if user_price == 0:
            st.warning("⚠️ Please enter a valid price guess!")
        else:
            diff = abs(user_price - real_price)

            # Tahmini kaydet
            st.session_state.guesses.append({
                "name": user_name.strip(),
                "guess": user_price,
                "diff": diff
            })

            # 🎯 Sonuç ve GIF
            if diff <= 5000:
                st.success("🎯 *So Close!* You're almost a real estate genius! 🧠💰")
                st.image("https://media4.giphy.com/media/KHKnSqATU08oS73LWi/giphy.gif", caption="🎯 Almost a perfect shot!")
            
            elif user_price < real_price:
                st.warning("📉 *Too Low!* You just undersold a hidden gem!\nAim higher next time 💎")
                st.image("https://media1.giphy.com/media/26uf14WIlvzuZkKLS/giphy.gif", caption="📉 That was a steal... for someone else!")

            else:
                st.warning("📈 *Too High!* Whoa, that's a skyscraper price! 🏢\nAt this price, the house might still be on sale when you retire 😅")
                st.image("https://media2.giphy.com/media/l0G1700P94aQRbMpW/giphy.gif", caption="📈 Way above the clouds!")

    # --- Teşekkür ve Kapanış ---
    st.markdown("---")
    if os.path.exists("PH1.webp"):
        img = Image.open("PH1.webp")
        img = img.resize((img.width // 2, img.height // 2))
        st.image(img, use_container_width=False)

    st.markdown(
        """
        <h4 style="text-align: center; color: grey;">🏠 Thank you for visiting!</h4>
        """,
        unsafe_allow_html=True
    )

# --- Admin Panel Sayfası ---
elif page == "📊 Admin Panel":
    st.title("📊 Admin Panel - Best 5 Guesses")

    if "guesses" in st.session_state and st.session_state.guesses:
        named_guesses = [g for g in st.session_state.guesses if g['name']]

        if named_guesses:
            best_guesses = sorted(named_guesses, key=lambda x: x["diff"])[:5]

            st.subheader("🏆 Best 5 Guesses (Named Only)")
            for idx, entry in enumerate(best_guesses, start=1):
                emoji = "🥇" if idx == 1 else "⭐"
                st.write(f"{emoji} **{idx}. {entry['name']}** guessed **${int(entry['guess'])}** | **Difference:** ${int(entry['diff'])}")
        else:
            st.info("ℹ️ No named guesses yet!")
    else:
        st.info("ℹ️ No guesses made yet!")
