import random
import streamlit as st

st.set_page_config(page_title="Susun Kata Jepang - Bab 2", layout="centered")

# --- DATABASE SOAL BAB 2 ---
if "database_soal" not in st.session_state:
    st.session_state.database_soal = [
        # ==================== POIN 1: ～最中だ ====================
        {
            "id": 1,
            "pola": "1. ～最中だ",
            "kanji": "田中さんは今考え事をしている最中だから...",
            "hiragana": "たなかさん は いま かんがえごと を している さいちゅうだ から 、 じゃましない ほう が いい",
            "arti": "Karena Tanaka-san sedang sibuk berpikir saat ini, sebaiknya jangan diganggu.",
            "soal": ["いま", "は", "かんがえごと", "いい", "たなかさん", "ほう が", "から", "じゃましない", "さいちゅうだ", "を している", "、"],
            "kunci": ["たなかさん", "は", "いま", "かんがえごと", "を している", "さいちゅうだ", "から", "、", "じゃましない", "ほう が", "いい"]
        },
        {
            "id": 2,
            "pola": "1. ～最中だ",
            "kanji": "浜辺でバーベキューをやっている最中に...",
            "hiragana": "はまべ で ばーべきゅー を やっている さいちゅうに 、 きゅうに あめ が ふりだした",
            "arti": "Di tengah-tengah melakukan BBQ di pantai, tiba-tiba hujan mulai turun.",
            "soal": ["きゅうに", "を やっている", "ばーべきゅー", "さいちゅうに", "ふりだした", "あめ が", "はまべ で", "、"],
            "kunci": ["はまべ で", "ばーべきゅー", "を やっている", "さいちゅうに", "、", "きゅうに", "あめ が", "ふりだした"]
        },
        {
            "id": 3,
            "pola": "1. ～最中だ",
            "kanji": "スピーチの最中に...",
            "hiragana": "すぴーち の さいちゅうに 、 とつぜん でんき が きえた",
            "arti": "Di tengah-tengah pidato, tiba-tiba lampunya padam.",
            "soal": ["とつぜん", "すぴーち", "きえた", "でんき が", "さいちゅうに", "の", "、"],
            "kunci": ["すぴーち", "の", "さいちゅうに", "、", "とつぜん", "でんき が", "きえた"]
        },

        # ==================== POIN 2: ～うちに ====================
        {
            "id": 4,
            "pola": "2. ～うちに",
            "kanji": "子供が眠っているうちに...",
            "hiragana": "こども が ねむっている うちに 、 かじ は ぜんぶ やっ てしまった",
            "arti": "Selagi anak sedang tidur, pekerjaan rumah tangga sudah saya selesaikan semuanya.",
            "soal": ["かじ", "ねむっている", "うちに", "は", "ぜんぶ", "こども が", "やっ てしまった", "、"],
            "kunci": ["こども が", "ねむっている", "うちに", "、", "かじ", "は", "ぜんぶ", "やっ てしまった"]
        },
        {
            "id": 5,
            "pola": "2. ～うちに",
            "kanji": "忘れないうちに...",
            "hiragana": "わすれ ない うちに 、 かれんだー に めもして おこう",
            "arti": "Selagi belum lupa, mari mencatatnya di kalender.",
            "soal": ["かれんだー", "めもして おこう", "に", "うちに", "わすれ ない", "、"],
            "kunci": ["わすれ ない", "うちに", "、", "かれんだー", "に", "めもして おこう"]
        },
        {
            "id": 6,
            "pola": "2. ～うちに",
            "kanji": "足が丈夫なうちに...",
            "hiragana": "あし が じょうぶな うちに 、 ひまらやとざん を けいかくしたい",
            "arti": "Selagi kaki masih kuat, saya ingin merencanakan pendakian Gunung Himalaya.",
            "soal": ["けいかくしたい", "うちに", "ひまらやとざん", "じょうぶな", "あし が", "を", "、"],
            "kunci": ["あし が", "じょうぶな", "うちに", "、", "ひまらやとざん", "を", "けいかくしたい"]
        },
        {
            "id": 7,
            "pola": "2. ～うちに",
            "kanji": "学生のうちに...",
            "hiragana": "がくせい の うちに 、 くるま の うんてん めんきょ を とろう とおもっております",
            "arti": "Selagi masih menjadi mahasiswa, saya berniat untuk mengambil SIM mobil.",
            "soal": ["めんきょ", "くるま", "うんてん", "がくせい", "うちに", "とおもっております", "の", "を", "とろう", "の", "、"],
            "kunci": ["がくせい", "の", "うちに", "、", "くるま", "の", "うんてん", "めんきょ", "を", "とろう", "とおもっております"]
        },
        {
            "id": 8,
            "pola": "2. ～うちに",
            "kanji": "調べたうちに...",
            "hiragana": "いんたーねっと で しらべている うちに 、 いろいろな こと が わかってきた",
            "arti": "Selagi/saat mencari tahu di internet, berbagai hal menjadi semakin terungkap/diketahui.",
            "soal": ["しらべている", "わかってきた", "いろいろな こと", "いんたーねっと", "うちに", "で", "が", "、"],
            "kunci": ["いんたーねっと", "で", "しらべている", "うちに", "、", "いろいろな こと", "が", "わかってきた"]
        },
        {
            "id": 9,
            "pola": "2. ～うちに",
            "kanji": "使っているうちに...",
            "hiragana": "この けいたいでんわ は ながいあいだ つかっている うちに 、 もう じぶん の からだ の いちぶ の ように なった",
            "arti": "HP ini selama digunakan dalam waktu lama, rasanya sudah menjadi seperti bagian dari tubuh sendiri.",
            "soal": ["けいたいでんわ", "この", "うちに", "いちぶ", "じぶん", "もう", "ように なった", "の", "ながいあいだ", "つかっている", "は", "からだ の", "、"],
            "kunci": ["この", "けいたいでんわ", "は", "ながいあいだ", "つかっている", "うちに", "、", "もう", "じぶん", "の", "からだ の", "いちぶ", "ように なった"]
        },
        {
            "id": 10,
            "pola": "2. ～うちに",
            "kanji": "知らないうちに...",
            "hiragana": "しらない うちに 、 あめ が ふりはじめていた",
            "arti": "Tanpa disadari/diketahui, ternyata hujan sudah mulai turun.",
            "soal": ["あめ が", "しらない", "ふりはじめていた", "うちに", "、"],
            "kunci": ["しらない", "うちに", "、", "あめ が", "ふりはじめていた"]
        },

        # ==================== POIN 3: ～ばかりだ・～一方だ ====================
        {
            "id": 11,
            "pola": "3. ～ばかりだ・～一方だ",
            "kanji": "増えるばかりだ...",
            "hiragana": "このごろ は しごと が おおくて 、 ざんぎょう は ふえる ばかりだ",
            "arti": "Akhir-akhir ini karena pekerjaan banyak, kerja lembur terus-menerus bertambah.",
            "soal": ["このごろ", "ざんぎょう", "は", "ふえる", "おおくて", "しごと が", "ばかりだ", "、"],
            "kunci": ["このごろ", "は", "しごと が", "おおくて", "、", "ざんぎょう", "は", "ふえる", "ばかりだ"]
        },
        {
            "id": 12,
            "pola": "3. ～ばかりだ・～一方だ",
            "kanji": "複雑になるばかりで...",
            "hiragana": "とうきょう の こうつうきかん は ふくざつになる ばかりで 、 わたし は よく わからなくなってきた",
            "arti": "Sistem transportasi Tokyo terus bertambah rumit, sehingga saya semakin tidak paham.",
            "soal": ["とうきょう", "こうつうきかん", "ふくざつになる", "わたし", "は", "わからなくなってきた", "ばかりで", "の", "は", "よく", "、"],
            "kunci": ["とうきょう", "の", "こうつうきかん", "は", "ふくざつになる", "ばかりで", "、", "わたし", "は", "よく", "わからなくなってきた"]
        },
        {
            "id": 13,
            "pola": "3. ～ばかりだ・～一方だ",
            "kanji": "悪くなる一方だ...",
            "hiragana": "かれ と の にんげんかんけい は いちど もんだい が おきて から 、 わるくなる いっぽうだ",
            "arti": "Hubungan antarmanusia dengan dia, sejak timbul masalah sekali, makin ke sini makin memburuk.",
            "soal": ["かれ", "わるくなる", "いちど", "にんげんかんけい", "もんだい", "は", "いっぽうだ", "から", "と の", "が", "おきて", "、"],
            "kunci": ["かれ", "と の", "にんげんかんけい", "は", "いちど", "もんだい", "が", "おきて", "から", "、", "わるくなる", "いっぽうだ"]
        },
        {
            "id": 14,
            "pola": "3. ～ばかりだ・～一方だ",
            "kanji": "広がる一方なので...",
            "hiragana": "うし の びょうき が くにじゅう に ひろがる いっぽう なので 、 ひと が しんぱいしている",
            "arti": "Karena penyakit sapi terus meluas ke seluruh negeri, orang-orang menjadi cemas.",
            "soal": ["しんぱいしている", "くにじゅう", "ひろがる", "うし", "びょうき", "いっぽう なので", "の", "に", "ひと が", "が", "、"],
            "kunci": ["うし", "の", "びょうき", "が", "くにじゅう", "に", "ひろがる", "いっぽう なので", "、", "ひと が", "しんぱいしている"]
        },

        # ==================== POIN 4: ～（よ）うとしている ====================
        {
            "id": 15,
            "pola": "4. ～（よ）うとしている",
            "kanji": "始まろうとしている...",
            "hiragana": "さあ 、 いま けっしょうせん が はじまろう としています 、 みんな きんちょうしています 。",
            "arti": "Nah, sekarang babak final akan segera dimulai, semuanya merasa tegang.",
            "soal": ["いま", "さあ", "きんちょうしています", "はじまろう", "みんな", "けっしょうせん が", "としています", "、", "。"],
            "kunci": ["さあ", "、", "いま", "けっしょうせん が", "はじまろう", "としています", "、", "みんな", "きんちょうしています", "。"]
        },
        {
            "id": 16,
            "pola": "4. ～（よ）うとしている",
            "kanji": "完成しようとしている...",
            "hiragana": "えきまえ に さんじゅうかいだて の こうきゅうまんしょん が かんせい しよう としている 。",
            "arti": "Apartemen mewah 30 lantai di depan stasiun hampir/akan segera selesai dibangun.",
            "soal": ["かんせい", "さんじゅうかいだて", "えきまえ", "こうきゅうまんしょん", "に", "しよう", "の", "が", "としている", "。"],
            "kunci": ["えきまえ", "に", "さんじゅうかいだて", "の", "こうきゅうまんしょん", "が", "かんせい", "しよう", "としている", "。"]
        },
        {
            "id": 17,
            "pola": "4. ～（よ）うとしている",
            "kanji": "満開になろうとしているとき...",
            "hiragana": "さくら が まんかい に なろう としている とき 、 ゆき が ふった",
            "arti": "Saat bunga sakura hendak mekar penuh, salju justru turun.",
            "soal": ["まんかい に", "ゆき が", "さくら が", "としている とき", "なろう", "ふった", "、"],
            "kunci": ["さくら が", "まんかい に", "なろう", "としている とき", "、", "ゆき が", "ふった"]
        },

        # ==================== POIN 5: ～つつある ====================
        {
            "id": 18,
            "pola": "5. ～つつある",
            "kanji": "暖かくなりつつあります...",
            "hiragana": "はる は しだい に あたたかく なり つつ あり ます 、 もうすぐです 。",
            "arti": "Musim semi secara bertahap semakin hangat, sebentar lagi tiba.",
            "soal": ["はる", "しだい に", "あたたかく", "あり ます", "は", "つつ", "なり", "もうすぐです", "、", "。"],
            "kunci": ["はる", "は", "しだい に", "あたたかく", "なり", "つつ", "あり ます", "、", "もうすぐです", "。"]
        },
        {
            "id": 19,
            "pola": "5. ～つつある",
            "kanji": "発展しつつあり...",
            "hiragana": "げんざい この かいしゃ は はってんし つつあり 、 しょうらい が きたいされる",
            "arti": "Saat ini perusahaan ini sedang terus berkembang, dan masa depannya sangat diandalkan.",
            "soal": ["きたいされる", "かいしゃ", "げんざい", "しょうらい が", "この", "は", "はってんし", "つつあり", "、"],
            "kunci": ["げんざい", "この", "かいしゃ", "は", "はってんし", "つつあり", "、", "しょうらい が", "きたいされる"]
        },
        {
            "id": 20,
            "pola": "5. ～つつある",
            "kanji": "近代化しつつあった...",
            "hiragana": "めいじじだい の はじめ 、 にほん は きゅうそく に きんだいかし つつあった",
            "arti": "Pada awal zaman Meiji, Jepang sedang dalam proses modernisasi secara cepat.",
            "soal": ["きんだいかし", "にほん", "つつあった", "きゅうそく に", "めいじじだい", "の", "はじめ", "は", "、"],
            "kunci": ["めいじじだい", "の", "はじめ", "、", "にほん", "は", "きゅうそく に", "きんだいかし", "つつあった"]
        },

        # ==================== POIN 6: ～つつ ====================
        {
            "id": 21,
            "pola": "6. ～つつ",
            "kanji": "話し合いつつ...",
            "hiragana": "この あきち を どうするか について は 、 じゅうみん と はなしあい つつ 、 けいかく を たてていきたい",
            "arti": "Mengenai lahan kosong ini hendak dijadikan apa, saya ingin membuat rencana sambil berdiskusi dengan warga.",
            "soal": ["この", "について は", "じゅうみん", "はなしあい", "どうするか", "けいかく", "あきち", "を", "と", "つつ", "を", "たてていきたい", "、"],
            "kunci": ["この", "あきち", "を", "どうするか", "について は", "、", "じゅうみん", "と", "はなしあい", "つつ", "、", "けいかく", "を", "たてていきたい"]
        },
        {
            "id": 22,
            "pola": "6. ～つつ",
            "kanji": "考えつつ...",
            "hiragana": "しょうらい の こと など かんがえ つつ 、 おかね の こと や しごと の こと を えらばなければならない",
            "arti": "Sambil memikirkan hal-hal seperti masa depan, kita harus memilih hal terkait uang maupun pekerjaan.",
            "soal": ["しょうらい", "の", "こと", "など", "かんがえ", "つつ", "、", "おかね", "の", "こと", "や", "しごと", "を", "えらばなければならない"],
            "kunci": ["しょうらい", "の", "こと", "など", "かんがえ", "つつ", "、", "おかね", "の", "こと", "や", "しごと", "を", "えらばなければならない"]
        },
        {
            "id": 23,
            "pola": "6. ～つつ",
            "kanji": "楽しみつつ...",
            "hiragana": "にほん の せいかつ に いろいろな たいけん を たのしみ つつ 、 なれていった",
            "arti": "Sambil menikmati berbagai pengalaman dalam kehidupan di Jepang, saya pun menjadi terbiasa.",
            "soal": ["たいけん", "たのしみ", "せいかつ に", "にほん", "いろいろな", "なれていった", "の", "を", "つつ", "、"],
            "kunci": ["にほん", "の", "せいかつ に", "いろいろな", "たいけん", "を", "たのしみ", "つつ", "、", "なれていった"]
        }
    ]

# Inisialisasi State
if "index_soal" not in st.session_state:
    st.session_state.index_soal = 0
if "jawaban_user" not in st.session_state:
    st.session_state.jawaban_user = []
if "bank_kata" not in st.session_state:
    st.session_state.bank_kata = []
if "status_periksa" not in st.session_state:
    st.session_state.status_periksa = False

# State untuk Fitur Swap
if "idx_kata_dipilih" not in st.session_state:
    st.session_state.idx_kata_dipilih = None
if "mode_tukar" not in st.session_state:
    st.session_state.mode_tukar = False

# --- FITUR PILIH NOMOR SOAL ---
total_soal = len(st.session_state.database_soal)
list_nomor_soal = [i + 1 for i in range(total_soal)]

def ubah_nomor_soal():
    # Mengisi ulang bank kata dan mereset state saat nomor soal diganti
    st.session_state.index_soal = st.session_state.pilih_no_soal - 1
    st.session_state.jawaban_user = []
    st.session_state.bank_kata = []
    st.session_state.idx_kata_dipilih = None
    st.session_state.status_periksa = False

col_head1, col_head2 = st.columns([2, 1])
with col_head1:
    st.title("🦉 Bunpou Master - Bab 2")
with col_head2:
    st.selectbox(
        "Pilih Nomor Soal:",
        options=list_nomor_soal,
        index=st.session_state.index_soal,
        key="pilih_no_soal",
        on_change=ubah_nomor_soal
    )

soal_sekarang = st.session_state.database_soal[st.session_state.index_soal]
st.caption(f"Soal {st.session_state.index_soal + 1} dari {total_soal}")
st.markdown("---")

# Memasukkan kata langsung dari array `soal` tanpa dirubah urutannya
if not st.session_state.bank_kata and not st.session_state.jawaban_user:
    st.session_state.bank_kata = [{"id": i, "teks": kata, "dipakai": False} for i, kata in enumerate(soal_sekarang["soal"])]

# --- CSS KHUSUS ---
st.markdown("""
<style>
    div[data-testid="stStatusWidget"] + div div[data-testid="stWidgetLabel"] {
        display: none;
    }
    
    /* Papan Kolom Fleksibel */
    [data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: wrap !important;
        gap: 6px !important;
    }
    
    [data-testid="stHorizontalBlock"] > div {
        flex: 1 1 21% !important; 
        min-width: 0 !important;
    }
    
    /* MENGATASI SOLUSI TITIK-TITIK: Teks dipaksa membungkus (wrap) ke bawah */
    div.stButton > button {
        border-radius: 8px !important;
        font-weight: bold !important;
        padding: 4px 2px !important;
        font-size: clamp(0.65rem, 2.2vw, 0.88rem) !important;
        line-height: 1.25 !important;
        height: auto !important;
        min-height: 42px !important;
        white-space: normal !important;
        word-break: break-all !important;
    }

    div.stButton > button p, div.stButton > button div, div.stButton > button span {
        white-space: normal !important;
        word-break: break-all !important;
        text-overflow: clip !important;
        overflow: visible !important;
    }

    .info-box {
        background-color: #e8f4fd;
        padding: 15px;
        border-radius: 12px;
        border-left: 5px solid #1fa2ff;
        margin-bottom: 20px;
    }
    .text-bunpou { font-size: 1.05rem; font-weight: bold; color: #1fa2ff; margin: 0 0 6px 0; }
    .text-arti { font-size: 1.2rem; font-weight: bold; color: #1a1a1a; margin: 0; }
    
    .swap-indicator {
        background-color: #e6fffa;
        border: 1px dashed #319795;
        padding: 10px;
        border-radius: 8px;
        color: #234e52;
        font-weight: bold;
        margin-bottom: 10px;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

# Petunjuk Soal
st.markdown(f"""
<div class="info-box">
    <p class="text-bunpou">📖 {soal_sekarang['pola']}</p>
    <p class="text-arti">🇮🇩 {soal_sekarang['arti']}</p>
</div>
""", unsafe_allow_html=True)

# --- RENDERING KUIS UTAMA ---
@st.fragment
def render_kuis_lengkap():
    st.write("### Kalimat Susunanmu:")
    
    mode = st.radio(
        "Aksi Sentuhan Papan:",
        ["Copot Kata (Normal)", "Tukar Posisi 2 Kata 🔄"],
        horizontal=True,
        label_visibility="collapsed"
    )
    
    if mode == "Tukar Posisi 2 Kata 🔄":
        st.session_state.mode_tukar = True
        if st.session_state.idx_kata_dipilih is not None:
            kata_terpilih = st.session_state.jawaban_user[st.session_state.idx_kata_dipilih]["teks"]
            st.markdown(f'<div class="swap-indicator">📍 Kata [{kata_terpilih}] terpilih. Klik kata tujuan untuk menukar!</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="swap-indicator">💡 Klik kata pertama yang ingin ditukar posisinya...</div>', unsafe_allow_html=True)
    else:
        st.session_state.mode_tukar = False
        st.session_state.idx_kata_dipilih = None

    # 1. PAPAN JAWABAN
    if not st.session_state.jawaban_user:
        st.markdown("<div style='border-bottom: 2px solid #e5e5e5; padding-bottom: 15px; margin-bottom: 20px; color:#aaaaaa; font-style:italic;'>Klik kata di bawah untuk mulai menyusun...</div>", unsafe_allow_html=True)
    else:
        opsi_papan = [f"{idx}. {item['teks']}" for idx, item in enumerate(st.session_state.jawaban_user)]
        format_papan = {opt: opt.split(". ", 1)[1] for opt in opsi_papan}
        
        klik_papan = st.pills(
            label="Papan Jawaban",
            options=opsi_papan,
            format_func=lambda x: format_papan[x],
            selection_mode="single",
            label_visibility="collapsed"
        )
        st.markdown("<div style='border-bottom: 2px solid #e5e5e5; margin-top: -10px; margin-bottom: 25px;'></div>", unsafe_allow_html=True)
        
        if klik_papan:
            idx_klik = int(klik_papan.split(". ")[0])
            
            if st.session_state.mode_tukar:
                if st.session_state.idx_kata_dipilih is None:
                    st.session_state.idx_kata_dipilih = idx_klik
                    st.rerun()
                else:
                    idx1 = st.session_state.idx_kata_dipilih
                    idx2 = idx_klik
                    if idx1 != idx2:
                        st.session_state.jawaban_user[idx1], st.session_state.jawaban_user[idx2] = st.session_state.jawaban_user[idx2], st.session_state.jawaban_user[idx1]
                    st.session_state.idx_kata_dipilih = None
                    st.rerun()
            else:
                kata_dicopot = st.session_state.jawaban_user.pop(idx_klik)
                for kata_bank in st.session_state.bank_kata:
                    if kata_bank["id"] == kata_dicopot["id"]:
                        kata_bank["dipakai"] = False
                st.rerun()

    # 2. BANK KATA PILIHAN
    st.write("### Pilihan Kata:")
    cols_pilihan = st.columns(4)
    for idx, item in enumerate(st.session_state.bank_kata):
        posisi_kolom = idx % 4
        with cols_pilihan[posisi_kolom]:
            if item["dipakai"]:
                st.button(" ", key=f"disabled_{item['id']}", disabled=True, use_container_width=True)
            else:
                if st.button(item["teks"], key=f"pilih_{item['id']}", use_container_width=True):
                    item["dipakai"] = True
                    st.session_state.jawaban_user.append(item)
                    st.rerun()

render_kuis_lengkap()

st.markdown("<br><hr>", unsafe_allow_html=True)

# 3. TOMBOL NAVIGASI UTAMA
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Reset 🔄", use_container_width=True):
        st.session_state.jawaban_user = []
        for kata in st.session_state.bank_kata:
            kata["dipakai"] = False
        st.session_state.idx_kata_dipilih = None
        st.session_state.status_periksa = False
        st.rerun()
with col2:
    if st.button("PERIKSA ✅", type="primary", use_container_width=True):
        st.session_state.status_periksa = True
with col3:
    if st.button("Lanjut ➡️", use_container_width=True):
        st.session_state.index_soal = (st.session_state.index_soal + 1) % len(st.session_state.database_soal)
        st.session_state.jawaban_user = []
        st.session_state.bank_kata = []
        st.session_state.idx_kata_dipilih = None
        st.session_state.status_periksa = False
        st.rerun()

# VALIDASI JAWABAN
if st.session_state.status_periksa:
    user_strings = [x["teks"] for x in st.session_state.jawaban_user]
    kunci_strings = soal_sekarang["kunci"]
    
    user_joined = "".join(user_strings)
    kunci_joined = "".join(kunci_strings)
    
    if user_joined == kunci_joined:
        st.success(f"🎉 **正解 (Benar)!** Susunan bunpou kamu sudah sempurna!\n\n**🇯🇵 Kanji/Kalimat:** {soal_sekarang['kanji']}\n\n**💡 Hiragana:** {soal_sekarang['hiragana']}")
    else:
        st.error(f"❌ **残念 (Kurang Tepat).**\n\n**Susunan yang benar:**\n\n`{' '.join(kunci_strings)}`\n\n**🇯🇵 Kanji/Kalimat:** {soal_sekarang['kanji']}\n\n**💡 Hiragana:** {soal_sekarang['hiragana']}")
