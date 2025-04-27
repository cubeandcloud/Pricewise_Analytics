import streamlit as st
import pandas as pd
import os
from PIL import Image

# Sayfa ayarları
st.set_page_config(page_title="Guess the Price - Real Estate Challenge", layout="centered")

# 🧠 Session State: Tahmin geçmişi tutmak için
if "guesses" not in st.session_state:
    st.session_state.guesses = []

# 🎯 Gerçek Fiyat
real_price = 214000

# --- Sidebar Menü ---
page = st.sidebar.selectbox(
    "Select Page",
    ("🏠 Play Game", "📊 Admin Panel")
)

# --- Play Game Sayfası ---
if page == "🏠 Play Game":

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

    # 📸 Fotoğraflar ve diğer kısımlar...

    # Kullanıcı Bilgileri
    st.subheader("🧑 Enter Your Name (Optional)")
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

            # 🎯 Sonuçlar
            if diff <= 5000:
                st.success("🎯 *So Close!* You're almost a real estate genius! 🧠💰")
                st.image("https://media4.giphy.com/media/KHKnSqATU08oS73LWi/giphy.gif", caption="🎯 Almost a perfect shot!")

            elif user_price < real_price:
                st.warning("📉 *Too Low!* You just undersold a hidden gem!\nAim higher next time 💎")
                st.image("https://media1.giphy.com/media/26uf14WIlvzuZkKLS/giphy.gif", caption="📉 That was a steal... for someone else!")

            else:
                st.warning("📈 *Too High!* Whoa, that's a skyscraper price! 🏢\nAt this price, the house might still be on sale when you retire 😅")
                st.image("https://media2.giphy.com/media/l0G1700P94aQRbMpW/giphy.gif", caption="📈 Way above the clouds!")

# --- Admin Panel Sayfası ---
elif page == "📊 Admin Panel":
    st.title("📊 Admin Panel - Best 5 Guesses")

    # --- Şifre Kontrolü ---
    password = st.text_input("🔒 Enter Admin Password:", type="password")

    if password == "data123":  # Şifreni buraya yazabilirsin!
        st.success("🔓 Access Granted!")

        # Admin işlemleri
        if "guesses" in st.session_state and st.session_state.guesses:
            named_guesses = [g for g in st.session_state.guesses if g['name']]

            if named_guesses:
                best_guesses = sorted(named_guesses, key=lambda x: x["diff"])[:5]

                st.subheader("🏆 Best 5 Guesses (Named Only)")
                for idx, entry in enumerate(best_guesses, start=1):
                    emoji = "🥇" if idx == 1 else "⭐"
                    st.write(f"{emoji} **{idx}. {entry['name']}** guessed **${int(entry['guess'])}** | **Difference:** ${int(entry['diff'])}")

                # 🧾 Tahminleri CSV / Excel Olarak İndir
                df = pd.DataFrame(named_guesses)
                st.download_button(
                    label="📥 Download Guesses as CSV",
                    data=df.to_csv(index=False).encode('utf-8'),
                    file_name='guesses.csv',
                    mime='text/csv'
                )

            else:
                st.info("ℹ️ No named guesses yet!")
        else:
            st.info("ℹ️ No guesses made yet!")

        # --- Reset Game Butonu ---
        if st.button("♻️ Reset Game"):
            st.session_state.guesses = []
            st.success("✅ Game has been reset!")
    elif password != "":
        st.error("🚫 Wrong Password!")
