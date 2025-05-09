import streamlit as st

# ------------------------------
# Konfigurasi Halaman
# ------------------------------
st.set_page_config(
    page_title="🐧 Kalkulator Minum Air Harian Lucu",
    layout="centered"
)

# ------------------------------
# Styling dan Background
# ------------------------------
st.markdown("""
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
""", unsafe_allow_html=True)

# ------------------------------
# Header
# ------------------------------
st.markdown("<h1 style='text-align: center; color: #00CFFF;'>🐧💦 Berapa Banyak Air yang Harus Kamu Minum Hari Ini?</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Biar nggak jadi kaktus kering, yuk hitung kebutuhan air kamu hari ini! 🌵➡💧</p>", unsafe_allow_html=True)

# ------------------------------
# Input Form
# ------------------------------
st.markdown("<div class='highlight-box'><b>🥤 Isi dulu datanya yaa, biar tahu kamu butuh berapa galon! 😄</b></div>", unsafe_allow_html=True)

berat = st.number_input("⚖ Berat badan kamu (kg):", min_value=1.0, step=0.5)
aktivitas = st.selectbox("💃 Seberapa aktif kamu hari ini?", [
    "Hari ini cuma matkul teori 😴",
    "Cukup banyak praktik 🧘",
    "Lari Kejar deadline laprak 🏃‍♂💨"
])
cuaca = st.selectbox("☀ Cuaca di luar gimana?", [
    "❄ Dingin Brrrr",
    "🌤 Normal Aja",
    "🔥 Panas Terik!"
])
jenis_kelamin = st.selectbox("🚻 Jenis kelamin kamu apa?", [
    "👦 Laki-laki",
    "👧 Perempuan"
])
usia = st.number_input("🎂 Umur kamu (biar nggak salah ngitung):", min_value=1, max_value=120, step=1)

# ------------------------------
# Fungsi Perhitungan Kebutuhan Air
# ------------------------------
def hitung_kebutuhan_air(berat, aktivitas, cuaca, jenis_kelamin, usia):
    kebutuhan_ml = berat * 30

    # Aktivitas
    if aktivitas == "Hari ini cuma matkul teori 😴":
        kebutuhan_ml += 300
    elif aktivitas == "Lari Kejar deadline laprak 🏃‍♂💨":
        kebutuhan_ml += 600

    # Cuaca
    if cuaca == "🔥 Panas Terik!":
        kebutuhan_ml += 400
    elif cuaca == "❄ Dingin Brrrr":
        kebutuhan_ml -= 200

    # Jenis kelamin
    if jenis_kelamin == "👦 Laki-laki":
        kebutuhan_ml += 200
    else:
        kebutuhan_ml -= 100

    # Usia
    if usia < 18:
        kebutuhan_ml -= 300

    return kebutuhan_ml / 1000  # Liter

# ------------------------------
# Tombol dan Output
# ------------------------------
if st.button("🧃 Hitung Berapa Kamu Harus Minum Hari Ini!"):
    if berat > 0:
        total_liter = hitung_kebutuhan_air(berat, aktivitas, cuaca, jenis_kelamin, usia)

        # Hasil utama
        st.markdown(
            f"<h3 style='color: #ff69b4;'>🚰 Kamu butuh minum sekitar <span style='color:#1e90ff;'>{total_liter:.2f} liter</span> air hari ini! 🍹</h3>",
            unsafe_allow_html=True
        )

        # Progress bar berdasarkan kebutuhan 3 liter
        st.progress(min(total_liter / 3.0, 1.0))

        # Notifikasi
        if total_liter < 1.5:
            st.markdown("<div class='highlight-box' style='background-color:#fff0f0;'>🥵 <b>Kurang banget!</b> Minum lagi, kamu kayak daun kering! 💧</div>", unsafe_allow_html=True)
        elif total_liter < 2.5:
            st.markdown("<div class='highlight-box' style='background-color:#f0fff0;'>😎 <b>Cukup!</b> Tetap jaga kebiasaan minummu yaa! 🧃</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='highlight-box' style='background-color:#e0f7ff;'>💪 <b>Hidrasi Sultan!</b> Kamu aktif banget, keren! Bawa botol air terus ya! 🍼</div>", unsafe_allow_html=True)

        # Tips
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

# ------------------------------
# Footer
# ------------------------------
st.markdown("---")
st.markdown("<p style='text-align: center; color: grey;'>🐬 Dibuat oleh tim <b>LPK 7 Daviona😊, Ifta😍, Nadila🤡, Vania😡, Sulthan🥸</b> yang haus ide & air 💡💧</p>", unsafe_allow_html=True)



