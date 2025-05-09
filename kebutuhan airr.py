import streamlit as st
import requests
from streamlit_lottie import st_lottie

# Konfigurasi halaman
st.set_page_config(page_title="🐧 Kalkulator Minum Air Harian Lucu", layout="centered")

# Fungsi untuk ambil animasi Lottie
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Animasi Lottie
lottie_water = load_lottieurl("https://lottie.host/87bafc33-681f-42fa-8d0e-1b95f25e758f/PRmavlvoPQ.json")

# Background dengan gambar air minum segar
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1610878180933-c4df3df72d1c?ixlib=rb-4.0.3&auto=format&fit=crop&w=1650&q=80");
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
    }
    .block-container {
        background-color: rgba(255, 255, 255, 0.92);
        padding: 2rem;
        border-radius: 15px;
    }
    .highlight-box {
        background-color: #31adff;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #add8e6;
        margin-bottom: 15px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# HEADER lucu
st.markdown("<h1 style='text-align: center; color: #00CFFF;'>🐧💦 Berapa Banyak Air yang Harus Kamu Minum Hari Ini?</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Biar nggak jadi kaktus kering, yuk hitung kebutuhan air kamu hari ini! 🌵➡💧</p>", unsafe_allow_html=True)

# Animasi lucu
if lottie_water:
    st_lottie(lottie_water, height=200)
else:
    st.info("⚠️ Animasi tidak berhasil dimuat.")

# FORM input
st.markdown("<div class='highlight-box'><b>🥤 Isi dulu datanya yaa, biar tahu kamu butuh berapa galon! 😄</b></div>", unsafe_allow_html=True)

berat = st.number_input("⚖ Berat badan kamu (kg):", min_value=1.0, step=0.5)
aktivitas = st.selectbox("💃 Seberapa aktif kamu hari ini?", ["Hari ini cuma matkul teori 😴", "Cukup banyak praktik 🧘", "Lari Kejar deadline laprak 🏃‍♂💨"])
cuaca = st.selectbox("☀ Cuaca di luar gimana?", ["❄ Dingin Brrrr", "🌤 Normal Aja", "🔥 Panas Terik!"])
jenis_kelamin = st.selectbox("🚻 Jenis kelamin kamu apa?", ["👦 Laki-laki", "👧 Perempuan"])
usia = st.number_input("🎂 Umur kamu (biar nggak salah ngitung):", min_value=1, max_value=120, step=1)

# Fungsi perhitungan lucu
def hitung_air(berat, aktivitas, cuaca, jenis_kelamin, usia):
    dasar = berat * 30

    if aktivitas == "Hari ini cuma matkul teori 😴":
        dasar += 300
    elif aktivitas == "Lari Kejar deadline laprak 🏃‍♂💨":
        dasar += 600

    if cuaca == "🔥 Panas Terik!":
        dasar += 400
    elif cuaca == "❄ Dingin Brrrr":
        dasar -= 200

    if jenis_kelamin == "👦 Laki-laki":
        dasar += 200
    else:
        dasar -= 100

    if usia < 18:
        dasar -= 300

    return dasar / 1000

# Tombol dan hasil perhitungan
if st.button("🧃 Hitung Berapa Kamu Harus Minum Hari Ini!"):
    if berat > 0:
        total = hitung_air(berat, aktivitas, cuaca, jenis_kelamin, usia)
        st.markdown(f"<h3 style='color: #ff69b4;'>🚰 Kamu butuh minum sekitar <span style='color:#1e90ff;'>{total:.2f} liter</span> air hari ini! 🍹</h3>", unsafe_allow_html=True)

        # Progress bar simulasi gelas air dari total kebutuhan 3 liter
        progress = min(total / 3.0, 1.0)  # batasi maksimal 100%
        st.progress(progress)

        # Notifikasi berdasarkan jumlah air
        if total < 1.5:
            st.markdown("<div class='highlight-box' style='background-color:#fff0f0;'>🥵 <b>Kurang banget!</b> Minum lagi, kamu kayak daun kering! 💧</div>", unsafe_allow_html=True)
        elif total < 2.5:
            st.markdown("<div class='highlight-box' style='background-color:#f0fff0;'>😎 <b>Cukup!</b> Tetap jaga kebiasaan minummu yaa! 🧃</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='highlight-box' style='background-color:#e0f7ff;'>💪 <b>Hidrasi Sultan!</b> Kamu aktif banget, keren! Bawa botol air terus ya! 🍼</div>", unsafe_allow_html=True)

        # Tips lucu
        st.markdown("<h4 style='color:#20B2AA;'>✨ Tips dari para profesional H2Oni:</h4>", unsafe_allow_html=True)
        st.markdown("""
        <div class='highlight-box'>
            <ul>
                <li>🐣 Minum segelas air setelah bangun tidur biar nggak ngelantur pas praktik.</li>
                <li>🍉 Makan buah-buahan berair seperti semangka dan jeruk, biar pipimu makin segar!</li>
                <li>⏰ Pasang alarm minum biar nggak lupa pas lagi kerjain laprak.</li>
                <li>🚰 Bawa botol tumblr ke mana pun, agar mengurangi limbah plastik!</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("⚠ Masukkan berat badan yang valid dulu yaa jangan bohongg~")

# FOOTER lucu
st.markdown("---")
st.markdown("<p style='text-align: center; color: grey;'>🐬 Dibuat oleh tim <b>LPK 7 Daviona😊, Ifta😍, Nadila🤡, Vania😡, Sulthan🥸</b> yang haus ide & air 💡💧</p>", unsafe_allow_html=True)


# FOOTER lucu
st.markdown("---")
st.markdown("<p style='text-align: center; color: grey;'>🐬 Dibuat oleh tim <b>LPK 7 Daviona😊, Ifta😍, Nadila🤡, Vania😡, Sulthan🥸</b> yang haus ide & air 💡💧</p>", unsafe_allow_html=True)

