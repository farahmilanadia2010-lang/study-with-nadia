import streamlit as st
import time
import random

# --- KONFIGURASI ---
st.set_page_config(page_title="Pink Pomodoro", page_icon="🌸", layout="centered")

# --- STYLE PINK ---
st.markdown("""
    <style>
    .stApp { background-color: #FFF0F5; }
    h1, h2, h3, p, label { color: #DB7093 !important; font-family: 'Courier New', Courier, monospace; }
    .stButton>button { background-color: #FFB6C1; color: white; border-radius: 20px; border: 2px solid #FF69B4; font-weight: bold; width: 100%; padding: 10px; }
    .stButton>button:hover { background-color: #FF69B4; color: white; }
    </style>
""", unsafe_allow_html=True)

# --- STATE ---
if 'todo_list' not in st.session_state:
    st.session_state.todo_list = []
if 'pomodoro_counter' not in st.session_state:
    st.session_state.pomodoro_counter = 0

# --- JUDUL ---
st.title("🌸 Pink Pomodoro Timer 🌸")
st.write("Kelola waktu belajarmu dengan musik Synthwave!")

quotes = [
    "Semangat belajarnya, Nadia! ✨",
    "Fokus yuk! Kamu lebih kuat dari rasa malasmu. 🌸",
    "Nikmati prosesnya! 💖"
]

# --- SIDEBAR ---
st.sidebar.header("⚙️ Pengaturan Waktu")
durasi_belajar = st.sidebar.number_input("Waktu Belajar (Menit):", min_value=1, max_value=120, value=25)
durasi_istirahat = st.sidebar.number_input("Waktu Istirahat (Menit):", min_value=1, max_value=60, value=5)

# --- TABS ---
tab1, tab2, tab3 = st.tabs(["⏱️ Timer", "🎵 Synthwave", "📝 To-Do"])

# ===== TAB 1: TIMER =====
with tab1:
    st.subheader("⏱️ Sesi Pomodoro")
    st.metric("🌸 Sesi Fokus", st.session_state.pomodoro_counter)
    
    mode = st.radio("Pilih Mode:", ["Belajar 📚", "Istirahat ☕"])
    menit_target = durasi_belajar if "Belajar" in mode else durasi_istirahat
    
    if st.button("Mulai Timer ▶️"):
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
        
        # Lonceng OTOMATIS
        bell_js = """
        <script>
        (function() {
            try {
                var audioCtx = new (window.AudioContext || window.webkitAudioContext)();
                function playBell() {
                    var freqs = [523.25, 659.25, 783.99, 1046.50];
                    freqs.forEach(function(freq, i) {
                        setTimeout(function() {
                            var osc = audioCtx.createOscillator();
                            var gain = audioCtx.createGain();
                            osc.connect(gain);
                            gain.connect(audioCtx.destination);
                            osc.frequency.value = freq;
                            osc.type = 'sine';
                            gain.gain.setValueAtTime(0.3, audioCtx.currentTime);
                            gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.3);
                            osc.start(audioCtx.currentTime);
                            osc.stop(audioCtx.currentTime + 0.3);
                        }, i * 200);
                    });
                }
                playBell();
                setTimeout(playBell, 1000);
                setTimeout(playBell, 2000);
            } catch(e) {}
        })();
        </script>
        """
        st.components.v1.html(bell_js, height=0)
        
        if "Belajar" in mode:
            st.session_state.pomodoro_counter += 1
            st.success("🎉 Selesai! Istirahat dulu ya! ☕")
            st.balloons()
        else:
            st.success("☕ Istirahat selesai! Lanjut belajar! 📚")

# ===== TAB 2: SYNTHWAVE RADIO =====
with tab2:
    st.subheader("🎵 Backsound - Synthwave Radio")
    st.write("Musik Synthwave 24/7 dari Lofi Girl!")
    
    # Tampilin cover art biar aesthetic
    st.image("https://i.ytimg.com/vi/4xDzrJKXOOY/maxresdefault.jpg", use_column_width=True)
    
    # Video player
    st.video("https://www.youtube.com/watch?v=4xDzrJKXOOY")
    
    st.success("💡 Klik PLAY di video, lalu pindah ke tab Timer. Musik tetap nyala!")

# ===== TAB 3: TO-DO =====
with tab3:
    st.subheader("📌 Tugas Hari Ini")
    with st.form(key='todo_form', clear_on_submit=True):
        tugas_baru = st.text_input("Tugas baru:")
        if st.form_submit_button('Tambah') and tugas_baru:
            st.session_state.todo_list.append({"task": tugas_baru, "done": False})
    
    for i, item in enumerate(st.session_state.todo_list):
        item["done"] = st.checkbox(item["task"], value=item["done"], key=f"task_{i}")
