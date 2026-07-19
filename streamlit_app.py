import streamlit as st
import time
import random

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Pink Pomodoro", page_icon="🌸", layout="centered")

# --- STYLE AESTHETIC PINK ---
st.markdown("""
    <style>
    .stApp {
        background-color: #FFF0F5;
    }
    h1, h2, h3, p {
        color: #DB7093 !important;
        font-family: 'Courier New', Courier, monospace;
    }
    .stButton>button {
        background-color: #FFB6C1;
        color: white;
        border-radius: 20px;
        border: 2px solid #FF69B4;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #FF69B4;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# --- FUNGSI AUDIO (Lonceng Otomatis) ---
def play_bell():
    bell_html = """
        <audio autoplay>
            <source src="https://actions.google.com/sounds/v1/alarms/digital_watch_alarm_long.ogg" type="audio/ogg">
        </audio>
    """
    st.markdown(bell_html, unsafe_allow_html=True)

# --- INISIALISASI SESSION STATE ---
if 'todo_list' not in st.session_state:
    st.session_state.todo_list = []
if 'pomodoro_counter' not in st.session_state:
    st.session_state.pomodoro_counter = 0

# --- JUDUL UTAMA ---
st.title("🌸 Pink Pomodoro Timer 🌸")
st.write("Kelola waktu belajarmu dengan lebih estetik dan produktif!")

# --- RANDOM QUOTE MOTIVASI ---
quotes = [
    "Semangat belajarnya, Nadia! Langkah kecil hari ini adalah kesuksesan masa depan. ✨",
    "Fokus yuk! Kamu lebih kuat dari rasa malasmu. 🌸",
    "Nikmati prosesnya. Istirahat sejenak, lalu melangkah lagi! 💖",
    "Satu sesi Pomodoro lagi menuju impianmu! 🚀"
]

# --- SIDEBAR: PENGATURAN FITUR ---
st.sidebar.header("⚙️ Pengaturan Fitur")

# 1 & 2. Kustomisasi Waktu Belajar & Istirahat sendiri
st.sidebar.subheader("⏳ Durasi Waktu (Menit)")
durasi_belajar = st.sidebar.number_input("Waktu Belajar:", min_value=1, max_value=120, value=25)
durasi_istirahat = st.sidebar.number_input("Waktu Istirahat:", min_value=1, max_value=60, value=5)

# 3. 10 Pilihan Backsound Musik & Suara Alam
st.sidebar.subheader("🎵 Musik Pendukung (10 Pilihan)")
pilihan_musik = st.sidebar.selectbox(
    "Pilih Suara Latar:", 
    [
        "Tanpa Musik", 
        "1. Lo-Fi Calm Beats", 
        "2. Cozy Cafe Jazz", 
        "3. Studio Ghibli Piano Vibe", 
        "4. Rain & Thunder (Hujan)", 
        "5. Forest Birds (Suara Hutan)", 
        "6. Ocean Waves (Ombak Laut)", 
        "7. White Noise (Fokus Maksimal)", 
        "8. Alpha Waves (Otak Cerdas)", 
        "9. Aesthetic Ambient Pop", 
        "10. Campfire Crackle (Api Unggun)"
    ]
)

# Link audio publik bebas hak cipta untuk variasi suara
audio_urls = {
    "1. Lo-Fi Calm Beats": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
    "2. Cozy Cafe Jazz": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
    "3. Studio Ghibli Piano Vibe": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3",
    "4. Rain & Thunder (Hujan)": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3",
    "5. Forest Birds (Suara Hutan)": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-5.mp3",
    "6. Ocean Waves (Ombak Laut)": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-6.mp3",
    "7. White Noise (Fokus Maksimal)": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-7.mp3",
    "8. Alpha Waves (Otak Cerdas)": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-8.mp3",
    "9. Aesthetic Ambient Pop": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-9.mp3",
    "10. Campfire Crackle (Api Unggun)": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-10.mp3"
}

if pilihan_musik != "Tanpa Musik":
    st.audio(audio_urls[pilihan_musik])

# --- MAIN INTERFACE (TABS) ---
tab1, tab2 = st.tabs(["📝 Tugas Hari Ini", "⏱️ Timer Pomodoro"])

# 4. Fitur To Do List
with tab1:
    st.subheader("📌 To-Do List")
    with st.form(key='todo_form', clear_on_submit=True):
        tugas_baru = st.text_input("Tambah tugas baru kamu di sini:")
        submit_tugas = st.form_submit_button(label='Tambah')
        
        if submit_tugas and tugas_baru:
            st.session_state.todo_list.append({"task": tugas_baru, "done": False})
            
    if st.session_state.todo_list:
        for i, item in enumerate(st.session_state.todo_list):
            item["done"] = st.checkbox(item["task"], value=item["done"], key=f"task_{i}")
    else:
        st.write("Belum ada tugas. Yuk tulis target belajarmu!")

# 5. Timer Interface
with tab2:
    st.subheader("⏱️ Sesi Pomodoro")
    st.metric(label="🌸 Sesi Fokus Berhasil Hari Ini", value=st.session_state.pomodoro_counter)
    
    mode = st.radio("Pilih Mode:", ["Belajar 📚", "Istirahat ☕"])
    menit_target = durasi_belajar if "Belajar" in mode else durasi_istirahat
    
    tombol_start = st.button("Mulai Timer ▶️")
    
    if tombol_start:
        quote_pilihan = random.choice(quotes)
        st.info(quote_pilihan)
        
        tempat_timer = st.empty()
        total_detik = menit_target * 60
        
        while total_detik > 0:
            menit = total_detik // 60
            detik = total_detik % 60
            tempat_timer.header(f"⏳ {menit:02d}:{detik:02d}")
            time.sleep(1)
            total_detik -= 1
            
        tempat_timer.header("🎉 Waktu Habis!")
        play_bell()  # Fitur Bunyi Lonceng Otomatis
        
        if "Belajar" in mode:
            st.session_state.pomodoro_counter += 1
            st.success("Hebat banget! Satu sesi belajar selesai. Sekarang waktunya istirahat! ☕")
            st.rerun()
        else:
            st.success("Istirahat selesai! Yuk, kembali fokus belajar! 📚")
       
