import streamlit as st
import time
import random
import base64  # ✅ Pindah ke atas biar gak error

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
    </style>
""", unsafe_allow_html=True)

# --- INISIALISASI SESSION STATE ---
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

# ===== TAB 1: TIMER =====
with tab1:
    st.subheader("⏱️ Sesi Pomodoro")
    st.metric(label="🌸 Sesi Fokus Berhasil Hari Ini", value=st.session_state.pomodoro_counter)
    
    mode = st.radio("Pilih Mode:", ["Belajar 📚", "Istirahat ☕"])
    menit_target = durasi_belajar if "Belajar" in mode else durasi_istirahat
    
    tombol_start = st.button("Mulai Timer ▶️")
    
    if tombol_start:
        st.info(random.choice(quotes))
        tempat_timer = st.empty()
        progress_bar = st.progress(0)
        total_detik = menit_target * 60
        
        while total_detik > 0:
            menit = total_detik // 60
            detik = total_detik % 60
            tempat_timer.header(f"⏳ {menit:02d}:{detik:02d}")
            progress_bar.progress(1 - (total_detik / (menit_target * 60)))
            time.sleep(1)
            total_detik -= 1
            
        tempat_timer.header("🎉 Waktu Habis!")
        progress_bar.empty()
        
        # ===== FITUR LONCENG (PAKE JAVASCRIPT) =====
        st.warning("🔔 Klik tombol di bawah untuk bunyi lonceng!")
        
        # Fungsi buat bunyi lonceng pake Web Audio API
        bell_js = """
        <script>
        function playBell() {
            try {
                var audioCtx = new (window.AudioContext || window.webkitAudioContext)();
                var frequencies = [523.25, 659.25, 783.99, 1046.50];
                var duration = 0.3;
                
                frequencies.forEach(function(freq, index) {
                    setTimeout(function() {
                        var oscillator = audioCtx.createOscillator();
                        var gainNode = audioCtx.createGain();
                        oscillator.connect(gainNode);
                        gainNode.connect(audioCtx.destination);
                        oscillator.frequency.value = freq;
                        oscillator.type = 'sine';
                        gainNode.gain.setValueAtTime(0.3, audioCtx.currentTime);
                        gainNode.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + duration);
                        oscillator.start(audioCtx.currentTime);
                        oscillator.stop(audioCtx.currentTime + duration);
                    }, index * 200);
                });
            } catch(e) {
                console.log('Audio error:', e);
            }
        }
        
        // Bunyiin 3 kali
        playBell();
        setTimeout(playBell, 1000);
        setTimeout(playBell, 2000);
        </script>
        """
        
        if st.button("🔊 Bunyikan Lonceng", key="bell_button"):
            st.components.v1.html(bell_js, height=0)
            st.success("🔔 Lonceng berbunyi! (cek suara device-mu)")
        
        # Opsi audio alternatif
        st.caption("Atau klik play di bawah ini (audio file):")
        st.audio("https://www.soundjay.com/misc/sounds/bell-ringing-05.mp3", format="audio/mp3")
        
        if "Belajar" in mode:
            st.session_state.pomodoro_counter += 1
            st.success("Hebat banget! Satu sesi belajar selesai. Sekarang waktunya istirahat! ☕")
        else:
            st.success("Istirahat selesai! Yuk, kembali fokus belajar! 📚")

# ===== TAB 2: MUSIK YOUTUBE =====
with tab2:
    st.subheader("🎵 Pilihan Musik Lo-Fi YouTube")
    st.write("Silakan pilih tema musik favoritmu, lalu tekan tombol **Play** pada pemutar video di bawah:")
    
    pilihan_yt = st.selectbox(
        "Pilih Link Live / Video YouTube:",
        [
            "1. Lofi Girl - Chill Lofi Study Beats (Live 24/7)",
            "2. Lofi Girl - Synthwave Radio (Fokus Retro)",
            "3. Cafe Music BGM - Cozy Jazz Piano",
            "4. Piano Relaxing - Studio Ghibli Collection"
        ]
    )
    
    youtube_urls = {
        "1. Lofi Girl - Chill Lofi Study Beats (Live 24/7)": "https://www.youtube.com/watch?v=jfKfPfyJRdk",
        "2. Lofi Girl - Synthwave Radio (Fokus Retro)": "https://www.youtube.com/watch?v=4xDzrJKXOOY",
        "3. Cafe Music BGM - Cozy Jazz Piano": "https://www.youtube.com/watch?v=2gteF6s0uP4",
        "4. Piano Relaxing - Studio Ghibli Collection": "https://www.youtube.com/watch?v=WZrqhllir4Y"
    }
    
    st.video(youtube_urls[pilihan_yt])
    st.caption("✨ *Tips: Putar videonya di tab ini, lalu klik tab 'Timer Pomodoro' untuk mulai belajar. Musiknya akan tetap menyala mengiringi fokusmu!*")

# ===== TAB 3: TO-DO LIST =====
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
