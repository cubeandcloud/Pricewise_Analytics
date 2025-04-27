import streamlit as st
import pandas as pd
import os
from PIL import Image

# --- Sayfa ayarları ---
st.set_page_config(page_title="Guess the Price - Real Estate Challenge", layout="centered")

# --- 🎯 Gerçek Fiyat ---
real_price = 214000

# --- 🧠 Session State: Sadece geçici tutuyoruz ---
if "guesses" not in st.session_state:
    st.session_state.guesses = []

# --- Sidebar Menü ---
page = st.sidebar.selectbox(
    "Select Page",
    ("🏠 Play Game", "📊 Admin Panel")
)

# --- 🏠 Play Game Sayfası ---
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

    # --- 📸 Fotoğraflar ---
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
            st.image("PH6.webp", caption="🛏️ Bedrooms", use_container_width=True)
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

    # --- Kullanıcı Bilgileri ---
    st.subheader("🧑 Enter Your Name (Optional)")
    user_name = st.text_input("Your name:")

    st.subheader("💸 Enter Your Price Guess")
    user_price = st.number_input("Your guess (in USD):", min_value=0, step=1000)

    if st.button("🎯 Make a Guess"):
        if user_price == 0:
            st.warning("⚠️ Please enter a valid price guess!")
        else:
            diff = abs(user_price - real_price)

            # --- Tahmini kaydet (hem Session'a hem CSV'ye) ---
            guess_record = {
                "name": user_name.strip(),
                "guess": user_price,
                "diff": diff
            }
            st.session_state.guesses.append(guess_record)

            # --- CSV'ye yaz ---
            if os.path.exists("guesses.csv"):
                df_existing = pd.read_csv("guesses.csv")
                df = pd.concat([df_existing, pd.DataFrame([guess_record])], ignore_index=True)
            else:
                df = pd.DataFrame([guess_record])

            df.to_csv("guesses.csv", index=False)

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

# --- 📊 Admin Panel Sayfası ---
elif page == "📊 Admin Panel":
    st.title("📊 Admin Panel - Best 5 Guesses")

    password = st.text_input("🔒 Enter Admin Password:", type="password")

    if password == "data123":  # Şifren burası (değiştirebilirsin)
        st.success("🔓 Access Granted!")

        if os.path.exists("guesses.csv"):
            df = pd.read_csv("guesses.csv")
            named_guesses = df[df['name'] != ""]

            if not named_guesses.empty:
                best_guesses = named_guesses.sort_values(by="diff").head(5)

                st.subheader("🏆 Best 5 Guesses (Named Only)")
                for idx, row in best_guesses.iterrows():
                    emoji = "🥇" if idx == best_guesses.index[0] else "⭐"
                    st.write(f"{emoji} **{row['name']}** guessed **${int(row['guess'])}** | **Difference:** ${int(row['diff'])}")

                # 🧾 Tahminleri CSV Olarak İndir
                st.download_button(
                    label="📥 Download All Guesses as CSV",
                    data=df.to_csv(index=False).encode('utf-8'),
                    file_name='guesses.csv',
                    mime='text/csv'
                )
            else:
                st.info("ℹ️ No named guesses yet!")
        else:
            st.info("ℹ️ No guesses made yet!")

        # --- Reset Guesses Butonu ---
        if st.button("♻️ Clear All Guesses"):
            if os.path.exists("guesses.csv"):
                os.remove("guesses.csv")
            st.session_state.guesses = []
            st.success("✅ All guesses have been cleared!")

    elif password != "":
        st.error("🚫 Wrong Password!")
