import streamlit as st
from PIL import Image
import os
import base64

# --- 1. KONFIGURASI HALAMAN & CSS ---
# Mengatur konfigurasi halaman. Harus menjadi perintah st pertama.
st.set_page_config(page_title="321 TSD", layout="wide", initial_sidebar_state="collapsed")

# CSS tema koran - hitam putih minimalis
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=Roboto:wght@300;400;500&display=swap');
    
    .main {
        background: #f5f5f5;
        font-family: 'Roboto', sans-serif;
    }
    
    .block-container {
        padding: 2rem 1rem;
        max-width: 1400px;
    }
    
    h1 {
        color: #000 !important;
        text-align: center;
        font-size: 4em !important;
        font-weight: 900 !important;
        font-family: 'Playfair Display', serif !important;
        letter-spacing: 3px;
        border-top: 4px solid #000;
        border-bottom: 4px solid #000;
        padding: 20px 0;
        margin-bottom: 10px !important;
        background: white;
    }
    
    .subtitle {
        text-align: center;
        color: #333;
        font-size: 1.1em;
        margin-bottom: 2rem;
        font-style: italic;
        font-weight: 300;
        letter-spacing: 1px;
    }
    
    .header-line {
        width: 100%;
        height: 2px;
        background: #000;
        margin: 20px 0;
    }
    
    .card {
        background: white;
        border: 2px solid #000;
        padding: 25px;
        margin-bottom: 20px;
        box-shadow: 8px 8px 0px #000;
    }
    
    /* CSS .question-card ini tidak lagi digunakan untuk membungkus, 
       tapi saya biarkan jika Anda ingin menggunakannya di tempat lain.
       Jika tidak, Anda bisa menghapusnya. */
    .question-card {
        background: #fff;
        border: 2px solid #000;
        padding: 20px;
        margin-bottom: 20px;
        position: relative;
        transition: all 0.2s;
    }
    
    .question-card:hover {
        box-shadow: 4px 4px 0px #000;
        transform: translate(-2px, -2px);
    }
    
    .question-number {
        color: #000;
        font-weight: 700;
        font-size: 1.3em;
        margin-bottom: 10px;
        font-family: 'Playfair Display', serif;
    }
    
    .cipher-row {
        display: flex;
        flex-wrap: wrap;
        gap: 5px;
        margin: 15px 0;
        padding: 15px;
        background: #f9f9f9;
        border: 1px solid #ddd;
        justify-content: center;
    }
    
    h2, h3 {
        color: #000 !important;
        font-weight: 700 !important;
        font-family: 'Playfair Display', serif !important;
        letter-spacing: 2px;
        border-bottom: 3px solid #000;
        padding-bottom: 10px;
        margin-bottom: 20px !important;
    }
    
    .stTextInput input {
        border: 2px solid #000 !important;
        border-radius: 0px !important;
        padding: 12px !important;
        font-size: 1em !important;
        font-family: 'Roboto', sans-serif !important;
        background: white !important;
        transition: all 0.2s;
    }
    
    .stTextInput input:focus {
        box-shadow: 4px 4px 0px #000 !important;
        transform: translate(-2px, -2px);
    }
    
    .stButton > button {
        background: #000;
        color: white;
        border: 3px solid #000;
        border-radius: 0px;
        padding: 10px 30px;
        font-size: 1em;
        font-weight: 700;
        font-family: 'Playfair Display', serif;
        letter-spacing: 1px;
        transition: all 0.2s;
        width: 100%; /* Membuat tombol Cek sama lebar */
        height: 48px; /* Menyamakan tinggi dengan input text */
    }
    
    .stButton > button:hover {
        background: white;
        color: #000;
        box-shadow: 6px 6px 0px #000;
        transform: translate(-3px, -3px);
    }
    
    .status-correct {
        background: #d4edda;
        border: 2px solid #28a745;
        padding: 10px;
        margin-top: 10px;
        font-weight: 600;
        color: #155724;
    }
    
    .status-incorrect {
        background: #f8d7da;
        border: 2px solid #dc3545;
        padding: 10px;
        margin-top: 10px;
        font-weight: 600;
        color: #721c24;
    }
    
    /* CSS BARU UNTUK GRID TTS */
    .tts-grid {
        display: inline-block;
        border: 4px solid #000;
        margin: 0 auto;
    }
    .tts-row {
        display: flex;
    }
    .tts-cell {
        width: 35px; /* Ukuran cell */
        height: 35px;
        background: white;
        border: 1px solid #000;
        position: relative;
        font-size: 1.2em;
        font-weight: 700;
        font-family: 'Roboto', sans-serif;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #000; /* Warna huruf jawaban */
    }
    .tts-cell.black {
        background: #000;
    }
    .tts-cell span.number {
        position: absolute;
        top: 1px;
        left: 2px;
        font-size: 10px;
        font-weight: bold;
        color: #333;
        font-family: 'Playfair Display', serif;
    }
    /* END CSS BARU */

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    hr {
        border: none;
        border-top: 2px solid #000;
        margin: 30px 0;
    }
    
    /* CSS untuk st.radio horizontal */
    div[role="radiogroup"] {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 10px;
        margin-bottom: 20px;
    }
    
    @media (max-width: 768px) {
        h1 {
            font-size: 2.5em !important;
            letter-spacing: 1px;
        }
        .card {
            padding: 15px;
            box-shadow: 4px 4px 0px #000;
        }
        .tts-cell {
            width: 22px;
            height: 22px;
            font-size: 0.8em;
        }
        .tts-cell span.number {
            font-size: 8px;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. HEADER & INSTRUKSI ---
st.markdown("<h1>321 TSD</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Decode the Cipher. Solve the Puzzle. Escape the Room.</p>", unsafe_allow_html=True)
st.markdown("<div class='header-line'></div>", unsafe_allow_html=True)

with st.expander("📖 CARA BERMAIN", expanded=False):
    st.markdown("""
    **Langkah-langkah:**
    
    1. Decode pertanyaan yang ada
    2. Temukan jawaban dari pertanyaan tersebut
    3. Encode jawaban sebelum dimasukkan
    4. Masukkan hasil enkripsi ke dalam kotak input
    5. Klik tombol "Cek" untuk memeriksa jawaban
                
    **Petunjuk:**
    1. Setiap simbol merepresentasikan satu huruf
    2. Tanda "|" adalah pemisah kata
    3. Perhatikan kata pertama
    """)

# --- 3. FUNGSI-FUNGSI INTI ---

# Fungsi Vigenere Cipher
def vigenere_encrypt(text, key):
    text = text.upper().replace(" ", "")
    key = key.upper().replace(" ", "")
    result = ''
    for i in range(len(text)):
        if text[i].isalpha():
            text_char = ord(text[i]) - 65
            key_char = ord(key[i % len(key)]) - 65
            result += chr(((text_char + key_char) % 26) + 65)
        else:
            result += text[i]
    return result

# Fungsi untuk menampilkan cipher dalam gambar
def display_cipher_text(text, folder="images"):
    """Menampilkan teks cipher menggunakan gambar pigpen"""
    cipher_html = '<div class="cipher-row">'
    for char in text:
        if char == ' ':
            cipher_html += '<div style="width: 20px; height: 40px; display: flex; align-items: center; justify-content: center; font-size: 20px; font-weight: bold;">|</div>'
        else:
            img_path = os.path.join(folder, f"{char.upper()}.png")
            if os.path.exists(img_path):
                import base64
                with open(img_path, "rb") as f:
                    img_data = base64.b64encode(f.read()).decode()
                cipher_html += f'<img src="data:image/jpeg;base64,{img_data}" style="width: 40px; height: 40px; object-fit: contain; border: 1px solid #ddd;" />'
            else:
                cipher_html += f'<div style="width: 40px; height: 40px; border: 2px solid #000; display: flex; align-items: center; justify-content: center; font-size: 14px; background: #f0f0f0; font-weight: bold;">{char}</div>'
    cipher_html += '</div>'
    return cipher_html

# --- 4. DATA PERTANYAAN & JAWABAN ---

mendatar = {
    '1': {'question': 'ANGKATAN KITA YANG BOTAK', 'length': 5, 'answer': 'YAHYA'},
    '2': {'question': 'WARNA BU MAR GA SUKA', 'length': 4, 'answer': 'PINK'},
    '4': {'question': 'JUARA SATU DANCE SYNREACH', 'length': 4, 'answer': 'DSDC'},
    '7': {'question': 'SOLUSI ANDALAN BU MAR', 'length': 11, 'answer': 'BASEDONCASE'},
    '9': {'question': 'NAMA ANAK PAK RUZZA', 'length': 5, 'answer': 'WYNNE'}
}

menurun = {
    '3': {'question': 'NEGARA PAK GHANI PHD', 'length': 8, 'answer': 'TIONGKOK'},
    '5': {'question': 'HARI SAINS DATA', 'length': 6, 'answer': 'SELASA'},
    '6': {'question': 'TSD GOES TO INTERNATIONAL', 'length': 5, 'answer': 'EDRIC'},
    '8': {'question': 'SEMESTER SIBUK', 'length': 4, 'answer': 'LIMA'},
    '10': {'question': 'DANUS JUALAN FADLI', 'length': 5, 'answer': 'SANDO'}
}

all_questions = {**mendatar, **menurun}

# Menghitung jawaban Vigenere yang benar
correct_answers = {}
for num, data in all_questions.items():
    key = data['question'].split()[0]
    correct_answers[num] = vigenere_encrypt(data['answer'], key)

answer_map = {
    # MENDATAR
    '9': {'data': mendatar['9'], 'dir': 'M', 'r': 0, 'c': 3},   # WYNNE (baris 0, mulai kolom 3) - geser kanan 1
    '4': {'data': mendatar['4'], 'dir': 'M', 'r': 1, 'c': 7},   # DSDC (baris 1, mulai kolom 7) - geser kiri 1
    '7': {'data': mendatar['7'], 'dir': 'M', 'r': 4, 'c': 0},   # BASEDONCASE (baris 4, tulang punggung)
    '2': {'data': mendatar['2'], 'dir': 'M', 'r': 6, 'c': 0},   # PINK (baris 6, mulai kolom 0) - geser kiri 1
    '1': {'data': mendatar['1'], 'dir': 'M', 'r': 8, 'c': 9},   # YAHYA (baris 8, mulai kolom 9)

    # MENURUN
    '8': {'data': menurun['8'], 'dir': 'D', 'r': 1, 'c': 1},    # LIMA (kolom 1, dari baris 1) - geser kanan 1
    '10': {'data': menurun['10'], 'dir': 'D', 'r': 4, 'c': 2},  # SANDO (kolom 2, dari baris 4)
    '3': {'data': menurun['3'], 'dir': 'D', 'r': 2, 'c': 5},    # TIONGKOK (kolom 5, dari baris 2)
    '6': {'data': menurun['6'], 'dir': 'D', 'r': 0, 'c': 7},    # EDRIC (kolom 7, dari baris 0) - geser kiri 1
    '5': {'data': menurun['5'], 'dir': 'D', 'r': 3, 'c': 10}    # SELASA (kolom 10, dari baris 3) - geser naik 1
}

# Initialize session state
if 'status' not in st.session_state:
    st.session_state.status = {str(i): None for i in range(1, 11)}
    
if 'grid_cells' not in st.session_state:
    st.session_state.grid_cells = [['' for _ in range(15)] for _ in range(15)]

# REVISI: Tambahkan state untuk melacak pertanyaan yang dipilih
if 'selected_question' not in st.session_state:
    st.session_state.selected_question = '1' # Default ke pertanyaan 1

# Fungsi untuk membangun layout grid statis (Nomor & Kotak Hitam)
def build_grid_layout(grid_size=15):
    layout = [['X' for _ in range(grid_size)] for _ in range(grid_size)]
    
    for num, info in answer_map.items():
        r, c = info['r'], info['c']
        length = info['data']['length']
        layout[r][c] = num 
        for i in range(1, length):
            if info['dir'] == 'M':
                if c + i < grid_size: layout[r][c + i] = ' '
            elif info['dir'] == 'D':
                if r + i < grid_size: layout[r + i][c] = ' '
    return layout

# Fungsi untuk memperbarui huruf di grid_cells state
def update_grid_cells():
    st.session_state.grid_cells = [['' for _ in range(15)] for _ in range(15)]
    
    for num, is_correct in st.session_state.status.items():
        if is_correct:
            info = answer_map[num]
            r, c = info['r'], info['c']
            answer = info['data']['answer']
            
            for i, letter in enumerate(answer):
                if info['dir'] == 'M':
                    st.session_state.grid_cells[r][c + i] = letter
                elif info['dir'] == 'D':
                    st.session_state.grid_cells[r + i][c] = letter

# Fungsi untuk menggambar Grid HTML
def render_grid_html(grid_layout):
    grid_html = '<div class="tts-grid">'
    for r, row in enumerate(grid_layout):
        grid_html += '<div class="tts-row">'
        for c, cell_type in enumerate(row):
            letter = st.session_state.grid_cells[r][c]
            
            if cell_type == 'X':
                grid_html += '<div class="tts-cell black"></div>'
            else:
                number_html = ''
                if cell_type.isdigit():
                    number_html = f'<span class="number">{cell_type}</span>'
                grid_html += f'<div class="tts-cell">{number_html}{letter}</div>'
        grid_html += '</div>'
    grid_html += '</div>'
    return grid_html

# --- 6. TAMPILAN APLIKASI ---

# Grid TTS tetap ditampilkan seperti sebelumnya
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>GRID TTS</h3>", unsafe_allow_html=True)

static_layout = build_grid_layout()
grid_html = render_grid_html(static_layout)
st.markdown(f'<div style="text-align: center;">{grid_html}</div>', unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# --- REVISI: Tampilan Pertanyaan Interaktif ---
# Kita gabungkan semua pertanyaan menjadi satu boks interaktif
# Hapus col1 dan col2

# Siapkan data untuk radio button
question_options = []
for num in sorted(mendatar.keys(), key=int):
    question_options.append((num, f"{num} Mendatar"))
for num in sorted(menurun.keys(), key=int):
    question_options.append((num, f"{num} Menurun"))

# Urutkan berdasarkan nomor
question_options.sort(key=lambda x: int(x[0]))

# Buat dictionary untuk mapping key ke label
options_keys = [q[0] for q in question_options]
options_labels = {q[0]: q[1] for q in question_options}

st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown("<h3>SOAL PERTANYAAN</h3>", unsafe_allow_html=True)

# Buat st.radio untuk memilih pertanyaan
st.radio(
    "Pilih Pertanyaan:",
    options=options_keys,
    format_func=lambda x: options_labels[x], # Tampilkan "1 Mendatar"
    key='selected_question', # Hubungkan ke session state
    horizontal=True,
    label_visibility="collapsed"
)

st.markdown("<hr>", unsafe_allow_html=True) # Pemisah

# Ambil data pertanyaan yang sedang dipilih
num = st.session_state.selected_question
data = all_questions[num]

# Tampilkan form HANYA untuk pertanyaan yang dipilih
st.markdown(f"<div class='question-number'>{options_labels[num]}</div>", unsafe_allow_html=True)
st.markdown(display_cipher_text(data['question']), unsafe_allow_html=True)

col_input, col_button = st.columns([3, 1])
with col_input:
    answer = st.text_input(
        f"Jawaban {num}:", 
        key=f"input_{num}", 
        label_visibility="collapsed", 
        placeholder=f"Jawaban terenkripsi ({data['length']} huruf)..."
    )
with col_button:
    if st.button("Cek", key=f"btn_{num}"):
        user_answer = answer.upper().replace(" ", "")
        if user_answer == correct_answers[num]:
            st.session_state.status[num] = True
            update_grid_cells()
        else:
            st.session_state.status[num] = False
        st.rerun()

if st.session_state.status[num] is True:
    st.markdown("<div class='status-correct'>✅ BENAR!</div>", unsafe_allow_html=True)
elif st.session_state.status[num] is False:
    st.markdown("<div class='status-incorrect'>❌ Salah, coba lagi!</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# --- 7. PROGRESS & FOOTER ---
# (Tidak ada perubahan di bagian ini, semua fungsionalitas dipertahankan)
st.markdown("<br>", unsafe_allow_html=True)
correct_count = sum(1 for status in st.session_state.status.values() if status is True)
if correct_count == 10:
    st.markdown("<div class='card' style='border-color: #28a745;'>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: #28a745; border: none;'>🎉 SELAMAT! KAMU BERHASIL MENYELESAIKAN PUZZLE! 🎉</h2>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
elif correct_count > 0:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; font-size: 1.2em;'>Progress: <strong>{correct_count}/10</strong> jawaban benar</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# # Petunjuk
# st.markdown("<br>", unsafe_allow_html=True)
# with st.expander("💡 PETUNJUK & BANTUAN"):
#     st.markdown("""
#     ### Cara Decode Pertanyaan
#     - Setiap simbol merepresentasikan satu huruf.
#     - Tanda "|" adalah pemisah kata.
    
#     ### Cara Encode Jawaban
#     - Gunakan metode Vigenere Cipher.
#     - **Kata pertama** dari pertanyaan (setelah di-decode) adalah **kunci** enkripsi.
#     - Contoh: Jika pertanyaan dimulai dengan "ANGKATAN", gunakan "ANGKATAN" sebagai kunci.
    
#     ### Format Jawaban
#     - HURUF KAPITAL semua
#     - Tanpa spasi
#     - Sesuai panjang yang diminta
#     """)

# Footer
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<div class='header-line'></div>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #333; font-size: 0.9em; font-style: italic;'>321 TSD - Kelompok 5</p>", unsafe_allow_html=True)