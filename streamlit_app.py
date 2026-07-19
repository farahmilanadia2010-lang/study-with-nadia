import streamlit as st
import time
import random

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Pink Pomodoro", page_icon="🌸", layout="centered")

# --- STYLE AESTHETIC PINK KEMBALI KACAU ---
st.markdown("""
    <style>
    .stApp {
        background-color: #FFF0F5;
    }
    h1, h2, h3, p, label, .stMarkdown {
        color: #DB7093 !important;
        font-family: 'Courier New', Courier, monospace;
    }
    .stButton>button {
        background-color: #FFB6C1;
        color: white;
        border-radius: 20px;
        border: 2px solid #FF69B4;
        font-weight: bold;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #FF69B4;
        color: white;
    }
    div[data-baseweb="tab-list"] {
        background-color: #FFB6C1;
        border-radius: 10px;
        padding: 5px;
    }
    button[data-baseweb="tab"] {
        color: white !important;
        font-weight: bold;
    }
    button[aria-selected="true"] {
        background-color: #FF69B4 !important;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# --- FUNGSI ALARM LONCENG ---
def play_bell():
    js_bell = """
    <script>
    var audio = new Audio('https://upload.wikimedia.org/wikipedia/commons/5/5c/Analog-watch-alarm_rolling.ogg');
    audio.play();
    </script>
    """
    st.components.v1.html(js_bell, height=0, width=0)

# --- INISIALISASI ---
if 'todo_list' not in st.session_state:
    st.session_state.todo_list = []
if 'pomodoro_counter' not in st.session_state:
    st.session_state.pomodoro_counter = 0

# --- JUDUL UTAMA ---
st.title("🌸 Pink Pomodoro Timer 🌸")
st.write("Kelola waktu belajarmu dengan lebih estetik dan produktif!")

quotes = [
    "Semangat belajarnya, Nadia! Langkah kecil hari ini adalah kesuksesan masa depan. ✨",
    "Fokus yuk! Kamu lebih kuat dari rasa malasmu. 🌸",
    "Nikmati prosesnya. Istirahat sejenak, lalu melangkah lagi! 💖",
    "Satu sesi Pomodoro lagi menuju impianmu! 🚀"
]

# --- SIDEBAR PENGATURAN WAKTU ---
st.sidebar.header("⚙️ Pengaturan Waktu")
durasi_belajar = st.sidebar.number_input("Waktu Belajar (Menit):", min_value=1, max_value=120, value=25)
durasi_istirahat = st.sidebar.number_input("Waktu Istirahat (Menit):", min_value=1, max_value=60, value=5)

# --- TABS UTAMA ---
tab1, tab2, tab3 = st.tabs(["⏱️ Timer Pomodoro", "🎵 10 Musik Latar", "📝 Tugas Hari Ini"])

# TAB 1: TIMER
with tab1:
    st.subheader("⏱️ Sesi Pomodoro")
    st.metric(label="🌸 Sesi Fokus Berhasil Hari Ini", value=st.session_state.pomodoro_counter)
    
    mode = st.radio("Pilih Mode:", ["Belajar 📚", "Istirahat ☕"])
    menit_target = durasi_belajar if "Belajar" in mode else durasi_istirahat
    
    tombol_start = st.button("Mulai Timer ▶️")
    
    if tombol_start:
        st.info(random.choice(quotes))
        tempat_timer = st.empty()
        total_detik = menit_target * 60
        
        while total_detik > 0:
            menit = total_detik // 60
            detik = total_detik % 60
            tempat_timer.header(f"⏳ {menit:02d}:{detik:02d}")
            time.sleep(1)
            total_detik -= 1
            
        tempat_timer.header("🎉 Waktu Habis!")
        play_bell()
        
        if "Belajar" in mode:
            st.session_state.pomodoro_counter += 1
            st.success("Hebat banget! Satu sesi belajar selesai. Sekarang waktunya istirahat! ☕")
        else:
            st.success("Istirahat selesai! Yuk, kembali fokus belajar! 📚")

# TAB 2: 10 PILIHAN MUSIK YANG SUDAH DIPERBAIKI (LINK STABIL WIKIMEDIA)
with tab2:
    st.subheader("🎵 10 Pilihan Musik Latar & Alam")
    pilihan_musik = st.selectbox(
        "Pilih Suara Latar:", 
        [
            "Tanpa Musik", 
            "1. Cozy Cafe Jazz Piano", 
            "2. Classical Focus Study (Chopin)", 
            "3. Relaxing Nature Ambient", 
            "4. Soft Rain Sound (Suara Hujan)", 
            "5. Forest Birds (Suara Burung Hutan)", 
            "6. Ocean Waves (Ombak Laut)", 
            "7. Deep Meditation Alpha Waves", 
            "8. Peaceful Temple Meditation", 
            "9. Cinematic Chill Ambient", 
            "10. Classic Music Focus"
        ]
    )
    
    # Semua link di bawah ini diganti ke format .mp3/.ogg yang lolos blokir browser
    audio_urls = {
        "1. Cozy Cafe Jazz Piano": "https://upload.wikimedia.org/wikipedia/commons/f/f3/Jesper_Ankarfeldt_-_04_-_Coffee_Shop.mp3",
        "2. Classical Focus Study (Chopin)": "https://upload.wikimedia.org/wikipedia/commons/a/a9/Frederic_Chopin_-_Nocturne_Op_9_No_2_E_flat_Major.mp3",
        "3. Relaxing Nature Ambient": "https://upload.wikimedia.org/wikipedia/commons/8/87/Ambient_nature_soundscape.ogg",
        "4. Soft Rain Sound (Suara Hujan)": "https://upload.wikimedia.org/wikipedia/commons/0/05/Rain_on_roof_1.ogg",
        "5. Forest Birds (Suara Burung Hutan)": "https://upload.wikimedia.org/wikipedia/commons/e/e3/Forest_birds_singing.ogg",
        "6. Ocean Waves (Ombak Laut)": "https://upload.wikimedia.org/wikipedia/commons/1/18/Ocean_waves_at_the_beach.ogg",
        "7. Deep Meditation Alpha Waves": "https://upload.wikimedia.org/wikipedia/commons/0/08/Binaural_Alpha_Waves_8Hz.ogg",
        "8. Peaceful Temple Meditation": "https://upload.wikimedia.org/wikipedia/commons/b/b5/Meditation_Bell_Sound.ogg",
        "9. Cinematic Chill Ambient": "https://upload.wikimedia.org/wikipedia/commons/b/b7/Epic_Cinematic_Ambient.mp3",
        "10. Classic Music Focus": "https://upload.wikimedia.org/wikipedia/commons/2/21/Mozart_-_Symphony_No._40_in_G_minor%2C_K._550_-_I._Molto_allegro.mp3"
    }
    
    if pilihan_musik != "Tanpa Musik":
        st.audio(audio_urls[pilihan_musik])
        st.caption("✨ *Tips: Klik tombol play di atas, musik akan terus berputar walaupun kamu pindah ke tab Timer!*")

# TAB 3: TO-DO LIST
with tab3:
    st.subheader("📌 Target & Tugas Hari Ini")
    with st.form(key='todo_form', clear_on_submit=True):
        tugas_baru = st.text_input("Tulis tugas baru kamu:")
        submit_tugas = st.form_submit_button(label='Tambah')
        
        if submit_tugas and tugas_baru:
            st.session_state.todo_list.append({"task": tugas_baru, "done": False})
            
    if st.session_state.todo_list:
        for i, item in enumerate(st.session_state.todo_list):
            item["done"] = st.checkbox(item["task"], value=item["done"], key=f"task_{i}")
    else:
        st.write("Belum ada target tugas tertulis.")
