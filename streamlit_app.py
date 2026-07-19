import streamlit as st
import time
import random

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Pink Pomodoro", page_icon="🌸", layout="centered")

# --- STYLE AESTHETIC PINK ---
st.markdown("""
    <style>
    .stApp { background-color: #FFF0F5; }
    h1, h2, h3, p, label { color: #DB7093 !important; font-family: 'Courier New', Courier, monospace; }
    .stButton>button { background-color: #FFB6C1; color: white; border-radius: 20px; border: 2px solid #FF69B4; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# --- INISIALISASI ---
if 'todo_list' not in st.session_state: st.session_state.todo_list = []
if 'pomodoro_counter' not in st.session_state: st.session_state.pomodoro_counter = 0

st.title("🌸 Pink Pomodoro Timer 🌸")

# --- TABS ---
tab1, tab2, tab3 = st.tabs(["⏱️ Timer", "🎵 Musik", "📝 Tugas"])

with tab1:
    st.subheader("Sesi Pomodoro")
    st.metric("Sesi Fokus Berhasil", st.session_state.pomodoro_counter)
    
    durasi = st.number_input("Durasi (Menit):", min_value=1, max_value=60, value=25)
    if st.button("Mulai Timer ▶️"):
        total_detik = durasi * 60
        tempat_timer = st.empty()
        while total_detik > 0:
            menit, detik = divmod(total_detik, 60)
            tempat_timer.header(f"⏳ {menit:02d}:{detik:02d}")
            time.sleep(1)
            total_detik -= 1
        tempat_timer.header("🎉 Waktu Habis!")
        st.session_state.pomodoro_counter += 1
        st.balloons()

with tab2:
    st.subheader("Musik Latar")
    st.write("Silakan pilih dan tekan tombol Play pada pemutar di bawah:")
    opsi = st.selectbox("Pilih Suara:", ["Tanpa Musik", "Lo-Fi Beats", "Rain Sound"])
    if opsi == "Lo-Fi Beats":
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
    elif opsi == "Rain Sound":
        st.audio("https://upload.wikimedia.org/wikipedia/commons/0/05/Rain_on_roof_1.ogg")

with tab3:
    st.subheader("To-Do List")
    tugas = st.text_input("Tambah tugas:")
    if st.button("Tambah"):
        st.session_state.todo_list.append(tugas)
    for t in st.session_state.todo_list:
        st.checkbox(t)
