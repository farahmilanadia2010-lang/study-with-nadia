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
        padding: 10px;
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
    iframe {
        border-radius: 15px;
        border: 3px solid #FFB6C1;
    }
    </style>
""", unsafe_allow_html=True)

# --- INISIALISASI ---
if 'todo_list' not in st.session_state:
    st.session_state.todo_list = []
if 'pomodoro_counter' not in st.session_state:
    st.session_state.pomodoro_counter = 0

# --- JUDUL UTAMA ---
st.title("🌸 Pink Pomodoro Timer 🌸")
st.write("Kelola waktu belajarmu dengan iringan musik YouTube Lofi Estetik!")

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
tab1, tab2, tab3 = st.tabs(["⏱️ Timer Pomodoro", "🎵 Musik YouTube", "📝 Tugas Hari Ini"])

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
        
        # SOLUSI PASTI BERBUNYI: Widget audio resmi yang muncul di akhir sesi
        st.error("⏰ WAKTU HABIS! Silakan klik tombol PLAY di bawah untuk mematikan alarm/mendengar lonceng:")
        st.audio("https://upload.wikimedia.org/wikipedia/commons/5/5c/Analog-watch-alarm_rolling.ogg")
        
        if "Belajar" in mode:
            st.session_state.pomodoro_counter += 1
            st.success("Hebat banget! Satu sesi belajar selesai. Sekarang waktunya istirahat! ☕")
        else:
            st.success("Istirahat selesai! Yuk, kembali fokus belajar! 📚")

# TAB 2: MUSIK DARI YOUTUBE
with tab2:
    st.subheader("🎵 Pilihan Musik Lo-Fi YouTube")
    st.write("Pilih tema musik kesukaanmu, lalu klik tombol **Play** pada pemutar di bawah:")
    
    pilihan_yt = st.selectbox(
        "Pilih Playlist / Video YouTube:",
        [
            "1. Lofi Girl - Chill Lofi Study Beats",
            "2. Pink Aesthetic Lofi Beats",
            "3. Studio Ghibli Piano Comforting Music",
            "4. Coffee Shop Piano Jazz Loop",
            "5. Cute & Relaxing Animal Crossing Music"
        ]
    )
    
    youtube_ids = {
        "1. Lofi Girl - Chill Lofi Study Beats": "jfKfPfyJRdk",
        "2. Pink Aesthetic Lofi Beats": "5wRWniH7avc",
        "3. Studio Ghibli Piano Comforting Music": "WZrqhllir4Y",
        "4. Coffee Shop Piano Jazz Loop": "2gteF6s0uP4",
        "5. Cute & Relaxing Animal Crossing Music": "f4CclhUenP0"
    }
    
    video_id = youtube_ids[pilihan_yt]
    
    embed_code = f"""
    <iframe width="100%" height="315" 
    src="https://www.youtube.com/embed/{video_id}" 
    title="YouTube video player" frameborder="0" 
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
    allowfullscreen></iframe>
    """
    
    st.components.v1.html(embed_code, height=330)
    st.caption("✨ *Tips: Putar musiknya di sini, lalu kamu bisa pindah ke tab 'Timer Pomodoro' untuk mulai belajar tanpa menghentikan lagunya!*")

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
