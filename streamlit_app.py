import streamlit as st
import time

# --- PENGATURAN HALAMAN WEB ---
st.set_page_config(page_title="Nadia's Pink Pomodoro 🎀", page_icon="🎀")

# --- MERACIK BACKGROUND & MODIFIKASI WARNA PINK (CSS) ---
st.markdown("""
    <style>
    .stApp {
        background-color: #FFE5EC;
    }
    h1 {
        color: #800F2F !important;
        font-family: 'Helvetica', sans-serif;
        text-align: center;
        text-shadow: 1px 1px 2px #FFB3C6;
    }
    .kotak-timer {
        font-size: 80px !important;
        font-weight: bold;
        color: #FB6F92;
        text-align: center;
        background-color: #FFFFFF;
        border-radius: 20px;
        padding: 20px;
        margin: 20px 0;
        box-shadow: 0px 4px 15px rgba(251, 111, 146, 0.2);
    }
    </style>
    """, unsafe_allow_html=True)

# --- TAMPILAN UTAMA WEBSITE ---
st.title("🎀 PINK POMODORO WEBPAGE 🎀")
st.write("<p style='text-align: center; color: #800F2F;'>Yuk fokus belajar bareng Nadia!</p>", unsafe_allow_html=True)

# Tempat menaruh angka jam digital di web
tempat_jam = st.empty()

# Tombol interaktif untuk Mulai
if st.button("Mulai Sesi Fokus (25 Menit)"):
    total_detik = 25 * 60 
    
    while total_detik > 0:
        menit = total_detik // 60
        detik = total_detik % 60
        
        # Masukkan angka jam ke dalam kotak putih estetik
        tempat_jam.markdown(f"<div class='kotak-timer'>{menit:02d}:{detik:02d}</div>", unsafe_allow_html=True)
        
        time.sleep(1)
        total_detik -= 1
        
    # Efek seru kalau waktu belajar sudah habis
    tempat_jam.markdown("<div class='kotak-timer'>🎉 WAKTU ISTIRAHAT! 🎉</div>", unsafe_allow_html=True)
    st.balloons() 
else:
    # Tampilan awal sebelum tombol diklik
    tempat_jam.markdown("<div class='kotak-timer'>25:00</div>", unsafe_allow_html=True)
