# TAB 1: TIMER & ALARM LONCENG
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
        
        # Progress bar biar lebih keren
        progress_bar = st.progress(0)
        
        while total_detik > 0:
            menit = total_detik // 60
            detik = total_detik % 60
            tempat_timer.header(f"⏳ {menit:02d}:{detik:02d}")
            
            # Update progress bar
            progress_bar.progress(1 - (total_detik / (menit_target * 60)))
            
            time.sleep(1)
            total_detik -= 1
            
        tempat_timer.header("🎉 Waktu Habis!")
        progress_bar.empty()
        
        # ===== PERBAIKAN AUDIO =====
        # Pake Base64 encoding biar pasti kedengeran
        import base64
        
        def play_sound():
            # Bunyi lonceng sederhana pake JavaScript + Web Audio API
            js_code = """
            <script>
            (function() {
                try {
                    // Pake Web Audio API buat bunyi lonceng
                    var audioCtx = new (window.AudioContext || window.webkitAudioContext)();
                    
                    function playBell() {
                        // Frekuensi nada lonceng (440Hz = nada A)
                        var frequencies = [523.25, 659.25, 783.99, 1046.50]; // C5, E5, G5, C6
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
                    }
                    
                    // Bunyikan 3 kali
                    playBell();
                    setTimeout(playBell, 1000);
                    setTimeout(playBell, 2000);
                    
                } catch(e) {
                    console.log('Audio error:', e);
                }
            })();
            </script>
            """
            return js_code
        
        # Tampilkan tombol play manual (biar gak diblokir browser)
        st.warning("🔔 Klik tombol di bawah untuk bunyi lonceng!")
        if st.button("🔊 Bunyikan Lonceng", key="bell_button"):
            st.components.v1.html(play_sound(), height=0)
            st.success("🔔 Lonceng berbunyi!")
        
        # Juga tampilkan audio alternatif (opsional)
        st.caption("Atau klik play di bawah ini (versi audio file):")
        st.audio("https://www.soundjay.com/misc/sounds/bell-ringing-05.mp3", format="audio/mp3")
        
        if "Belajar" in mode:
            st.session_state.pomodoro_counter += 1
            st.success("Hebat banget! Satu sesi belajar selesai. Sekarang waktunya istirahat! ☕")
        else:
            st.success("Istirahat selesai! Yuk, kembali fokus belajar! 📚")
