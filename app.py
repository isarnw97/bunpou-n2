import streamlit as st

st.set_page_config(page_title="Susun Kata Jepang - Bab 2", layout="centered")

# --- DATABASE SOAL BAB 2 ---
if "database_soal" not in st.session_state:
    st.session_state.database_soal = [
        # === POLA 1: ～最中に ===
        {
            "id": 1,
            "pola": "Pola 1: ～最中に",
            "kanji": "田中さんは今考えごとをしている最中だから、じゃましないほうがいい。",
            "hiragana": "たなかさんはいまかんがえごとをしているさいちゅうだから、じゃましないほうがいい。",
            "arti": "Tanaka-san sedang berpikir saat ini, jadi sebaiknya jangan diganggu.",
            "kunci": ["たなかさん", "は", "いま", "かんがえごと", "を している", "さいちゅうだ", "から", "、", "じゃましない", "ほう が", "いい", "。"],
            "soal": ["いま", "は", "かんがえごと", "いい", "たなかさん", "ほう が", "から", "じゃましない", "さいちゅうだ", "を している", "、"]
        },
        {
            "id": 2,
            "pola": "Pola 1: ～最中に",
            "kanji": "浜辺でバーベキューをやっている最中に、急に雨が降り出した。",
            "hiragana": "はまべでばーべきゅーをやっているさいちゅうに、きゅうにあめがふりだした。",
            "arti": "Di tengah-tengah barbecue di pantai, tiba-tiba hujan mulai turun.",
            "kunci": ["はまべ で", "ばーべきゅー", "を やっている", "さいちゅうに", "、", "きゅうに", "あめ が", "ふりだした", "。"],
            "soal": ["きゅうに", "を やっている", "ばーべきゅー", "さいちゅうに", "ふりだした", "あめ が", "はまべ で", "、"]
        },
        {
            "id": 3,
            "pola": "Pola 1: ～最中に",
            "kanji": "スピーチの最中に、突然電気消えた。",
            "hiragana": "すぴーちのさいちゅうに、とつぜんでんききえた。",
            "arti": "Di tengah-tengah pidato, tiba-tiba listrik padam.",
            "kunci": ["すぴーち", "の", "さいちゅうに", "、", "とつぜん", "でんき が", "きえた", "。"],
            "soal": ["とつぜん", "すぴーち", "きえた", "でんき が", "さいちゅうに", "の", "、"]
        },

        # === POLA 2: ～うちに ===
        {
            "id": 4,
            "pola": "Pola 2: ～うちに",
            "kanji": "家事は、子供が眠っているうちに、全部やってしまった。",
            "hiragana": "かじは、こどもがねむっているうちに、ぜんぶやってしまった。",
            "arti": "Pekerjaan rumah tangga sudah saya selesaikan semua selagi anak-anak sedang tidur.",
            "kunci": ["かじ", "は", "、", "こども が", "ねむっている", "うちに", "、", "ぜんぶ", "やっ てしまった", "。"],
            "soal": ["かじ", "ねむっている", "うちに", "は", "ぜんぶ", "こども が", "やっ てしまった", "、"]
        },
        {
            "id": 5,
            "pola": "Pola 2: ～うちに",
            "kanji": "忘れないうちに、カレンダーにメモしておこう。",
            "hiragana": "わすれないうちに、かれんだーにめもしておこう。",
            "arti": "Sebelum lupa, mari kita catat di kalender.",
            "kunci": ["わすれ ない", "うちに", "、", "かれんだー", "に", "めもして おこう", "。"],
            "soal": ["かれんだー", "めもして おこう", "に", "うちに", "わすれ ない", "、"]
        },
        {
            "id": 6,
            "pola": "Pola 2: ～うちに",
            "kanji": "足が丈夫なうちに、ヒマラヤ登山を計画したい。",
            "hiragana": "あしがじょうぶなうちに、ひまらやとざんをけいかくしたい。",
            "arti": "Selagi kaki masih kuat, saya ingin merencanakan pendakian ke Himalaya.",
            "kunci": ["あし が", "じょうぶな", "うちに", "、", "ひまらやとざん", "を", "けいかくしたい", "。"],
            "soal": ["けいかくしたい", "うちに", "ひまらやとざん", "じょうぶな", "あし が", "を", "、"]
        },
        {
            "id": 7,
            "pola": "Pola 2: ～うちに",
            "kanji": "学生のうちに車の運転免許を取ろうと思っています。",
            "hiragana": "がくせいのうちにくるまのうんてんめんきょをとろうとおもっています。",
            "arti": "Selagi masih mahasiswa, saya berniat untuk mengambil SIM mobil.",
            "kunci": ["がくせい", "の", "うちに", "くるま", "の", "うんてん", "めんきょ", "を", "とろう", "とおもっております", "。"],
            "soal": ["めんきょ", "くるま", "うんてん", "がくせい", "うちに", "とおもっております", "の", "を", "とろう", "の", "、"]
        },
        {
            "id": 8,
            "pola": "Pola 2: ～うちに",
            "kanji": "インターネットで調べにいるうちに、いろいろなことがわかってきた。",
            "hiragana": "いんたーねっとでしらべているうちに、いろいろなことがわかってきた。",
            "arti": "Saat sedang mencari tahu di internet, saya jadi memahami berbagai macam hal.",
            "kunci": ["いんたーねっと", "で", "しらべている", "うちに", "、", "いろいろな こと", "が", "わかってきた", "。"],
            "soal": ["しらべている", "わかってきた", "いろいろな こと", "いんたーねっと", "うちに", "で", "が", "、"]
        },
        {
            "id": 9,
            "pola": "Pola 2: ～うちに",
            "kanji": "この携帯電話は、長い間使っているうちに、もう自分の体の一部ようになった。",
            "hiragana": "このけいたいでんわは、ながいあいだつかっているうちに、もうじぶんのからだのいちぶのようになった。",
            "arti": "Ponsel ini, seiring lama digunakannya, sudah terasa seperti bagian dari tubuh saya sendiri.",
            "kunci": ["この", "けいたいでんわ", "は", "、", "ながいあいだ", "つかっている", "うちに", "、", "もう", "じぶん", "の", "からだ の", "いちぶ", "ように なった", "。"],
            "soal": ["けいたいでんわ", "この", "うちに", "いちぶ", "じぶん", "もう", "ように なった", "の", "ながいあいだ", "つかっている", "は", "からだ の", "、"]
        },
        {
            "id": 10,
            "pola": "Pola 2: ～うちに",
            "kanji": "知らないうちに、雨が降り始めていた。",
            "hiragana": "しらないうちに、あめがふりはじめていた。",
            "arti": "Tanpa disadari, hujan sudah mulai turun.",
            "kunci": ["しらない", "うちに", "、", "あめ が", "ふりはじめていた", "。"],
            "soal": ["あめ が", "しらない", "ふりはじめていた", "うちに", "、"]
        },

        # === POLA 3: ～ばかりだ・～一方だ ===
        {
            "id": 11,
            "pola": "Pola 3: ～ばかりだ・～一方だ",
            "kanji": "このごろは仕事が多くて残業が増えるばかりだ。",
            "hiragana": "このごろはしごとがおおくてざんぎょうがふえるばかりだ。",
            "arti": "Akhir-akhir ini pekerjaan banyak sehingga lembur terus bertambah saja.",
            "kunci": ["このごろ", "は", "しごと が", "おおくて", "ざんぎょう", "ふえる", "ばかりだ", "。"],
            "soal": ["このごろ", "ざんぎょう", "は", "ふえる", "おおくて", "しごと が", "ばかりだ", "、"]
        },
        {
            "id": 12,
            "pola": "Pola 3: ～ばかりだ・～一方だ",
            "kanji": "東京の交通機関は複雑になるばかりで、わたしはよくわからなくなってきた。",
            "hiragana": "とうきょうのこうつうきかんはふくざつになるばかりで、わたしはよくわからなくなってきた。",
            "arti": "Sistem transportasi di Tokyo terus menjadi rumit saja, dan saya makin tidak mengerti.",
            "kunci": ["とうきょう", "の", "こうつうきかん", "は", "ふくざつになる", "ばかりで", "、", "わたし", "は", "よく", "わからなくなってきた", "。"],
            "soal": ["とうきょう", "こうつうきかん", "ふくざつになる", "わたし", "は", "わからなくなってきた", "ばかりで", "の", "は", "よく", "、"]
        },
        {
            "id": 13,
            "pola": "Pola 3: ～ばかりだ・～一方だ",
            "kanji": "一度問題が起きてから、彼との人間関係は悪くなる一方だ。",
            "hiragana": "いちどもんだいがおきてから、かれとのにんげんかんけいはわるくなるいっぽうだ。",
            "arti": "Sejak masalah terjadi sekali, hubungan dengannya terus memburuk.",
            "kunci": ["いちど", "もんだい", "が", "おきて", "から", "、", "かれ", "と の", "にんげんかんけい", "は", "わるくなる", "いっぽうだ", "。"],
            "soal": ["かれ", "わるくなる", "いちど", "にんげんかんけい", "もんだい", "は", "いっぽうだ", "から", "と の", "が", "おきて", "、"]
        },
        {
            "id": 14,
            "pola": "Pola 3: ～ばかりだ・～一方だ",
            "kanji": "牛や豚の病気が広がる一方なので、国中の人が心配している。",
            "hiragana": "うしやぶたのびょうきがひろがるいっぽうなので、くにじゅうのひとがしんぱいしている。",
            "arti": "Karena penyakit sapi dan babi terus menyebar, seluruh masyarakat merasa khawatir.",
            "kunci": ["うし", "や", "びょうき", "の", "が", "ひろがる", "いっぽう なので", "、", "くにじゅう", "の", "ひと が", "しんぱいしている", "。"],
            "soal": ["しんぱいしている", "くにじゅう", "ひろがる", "うし", "びょうき", "いっぽう なので", "の", "や", "ひと が", "が", "、"]
        },

        # === POLA 4: ～（よ）うとしている ===
        {
            "id": 15,
            "pola": "Pola 4: ～（よ）うとしている",
            "kanji": "さあ、決勝戦が今、始まろうとしています。みんな緊張しています。",
            "hiragana": "さあ、けっしょうせんがいま、はじまろうとしています。みんなきんちょうしています。",
            "arti": "Nah, pertandingan babak final akan segera dimulai sekarang. Semuanya merasa tegang.",
            "kunci": ["さあ", "、", "けっしょうせん が", "いま", "、", "はじまろう", "としています", "。", "みんな", "きんちょうしています", "。"],
            "soal": ["いま", "さあ", "きんちょうしています", "はじまろう", "みんな", "けっしょうせん が", "としています", "、", "。"]
        },
        {
            "id": 16,
            "pola": "Pola 4: ～（よ）うとしている",
            "kanji": "駅前に30階建ての高級マンションが完成しようとしている。",
            "hiragana": "えきまえにさんじゅうかいだてのこうきゅうまんしょんがかんせいしようとしている。",
            "arti": "Apartemen mewah 30 lantai di depan stasiun akan segera selesai dibangun.",
            "kunci": ["えきまえ", "に", "さんじゅうかいだて", "の", "こうきゅうまんしょん", "が", "かんせい", "しよう", "としている", "。"],
            "soal": ["かんせい", "さんじゅうかいだて", "えきまえ", "こうきゅうまんしょん", "に", "しよう", "の", "が", "としている", "。"]
        },
        {
            "id": 17,
            "pola": "Pola 4: ～（よ）うとしている",
            "kanji": "桜が満開になろうとしているとき、雪が降った。",
            "hiragana": "さくらがまんかいになろうとしているとき、ゆきがふった。",
            "arti": "Saat bunga sakura hendak mekar sempurna, salju turun.",
            "kunci": ["さくら が", "まんかい に", "なろう", "としている とき", "、", "ゆき が", "ふった", "。"],
            "soal": ["まんかい に", "ゆき が", "さくら が", "としている とき", "なろう", "ふった", "、"]
        },

        # === POLA 5: ～つつある ===
        {
            "id": 18,
            "pola": "Pola 5: ～つつある",
            "kanji": "次第に暖かくなりつつあります。春はもうすぐです。",
            "hiragana": "しだいにあたたかくなりつつあります。はるはもうすぐです。",
            "arti": "Secara bertahap mulai terasa hangat. Musim semi sudah dekat.",
            "kunci": ["しだい に", "あたたかく", "なり", "つつ", "あり ます", "。", "はる", "は", "もうすぐです", "。"],
            "soal": ["はる", "しだい に", "あたたかく", "あり ます", "は", "つつ", "もうすぐです", "、", "。"]
        },
        {
            "id": 19,
            "pola": "Pola 5: ～つつある",
            "kanji": "この会社は現在発展しつつあり、将来が期待される。",
            "hiragana": "このかいしゃはげんざいはってんしつつあり、しょうらいがきたいされる。",
            "arti": "Perusahaan ini sedang berkembang saat ini, dan masa depannya sangat diharapkan.",
            "kunci": ["この", "かいしゃ", "は", "げんざい", "はってんし", "つつあり", "、", "しょうらい が", "きたいされる", "。"],
            "soal": ["きたいされる", "かいしゃ", "げんざい", "しょうらい が", "この", "は", "はってんし", "つつあり", "、"]
        },
        {
            "id": 20,
            "pola": "Pola 5: ～つつある",
            "kanji": "明治時代の初め、日本は急速に近代化しつつあった。",
            "hiragana": "めいじじだいのはじめ、にほんはきゅうそくにきんだいかしつつあった。",
            "arti": "Pada awal zaman Meiji, Jepang sedang mengalami modernisasi dengan pesat.",
            "kunci": ["めいじじだい", "の", "はじめ", "、", "にほん", "は", "きゅうそく に", "きんだいかし", "つつあった", "。"],
            "soal": ["きんだいかし", "にほん", "つつあった", "きゅうそく に", "めいじじだい", "の", "はじめ", "は", "、"]
        },

        # === POLA 6: ～つつ ===
        {
            "id": 21,
            "pola": "Pola 6: ～つつ",
            "kanji": "この空き地をどうするかについては、住民と話し合いつつ、計画を立てていきたい。",
            "hiragana": "このあきちをどうするかについては、じゅうみんとはなしあいつつ、けいかくをたてていきたい。",
            "arti": "Mengenai apa yang harus dilakukan pada tanah kosong ini, kami ingin membuat rencana sambil berdiskusi dengan warga.",
            "kunci": ["この", "あきち", "を", "どうするか", "について は", "、", "じゅうみん", "と", "はなしあい", "つつ", "、", "けいかく", "を", "たてていきたい", "。"],
            "soal": ["この", "について は", "じゅうみん", "はなしあい", "どうするか", "けいかく", "あきち", "を", "と", "つつ", "を", "たてていきたい", "、"]
        },
        {
            "id": 22,
            "pola": "Pola 6: ～つつ",
            "kanji": "将来の仕事のこと、お金のことなどを考えつつ、進路を選ばなければならない。",
            "hiragana": "しょうらいのしごとのこと、おかねのことなどをかんがえつつ、しんろをえらばなければならない。",
            "arti": "Sambil memikirkan hal-hal seperti pekerjaan masa depan dan uang, saya harus memilih jalan hidup.",
            "kunci": ["しょうらい", "の", "しごと", "の", "こと", "、", "おかね", "の", "こと", "など", "を", "かんがえ", "つつ", "、", "しんろ", "を", "えらばなければならない", "。"],
            "soal": ["しょうらい", "しんろ", "など", "かんがえ", "を", "おかね", "しごと", "の", "を", "えらばなければならない", "の", "こと", "こと", "つつ", "、"]
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

if "idx_kata_dipilih" not in st.session_state:
    st.session_state.idx_kata_dipilih = None

if "mode_tukar" not in st.session_state:
    st.session_state.mode_tukar = False

soal_sekarang = st.session_state.database_soal[st.session_state.index_soal]

if not st.session_state.bank_kata and not st.session_state.jawaban_user:
    st.session_state.bank_kata = [{"id": i, "teks": kata, "dipakai": False} for i, kata in enumerate(soal_sekarang["soal"])]

# --- CSS KHUSUS UNTUK TAMPILAN KAPSU/PILL KATA SEPERTI GAMBAR ---
st.markdown("""
<style>
    /* Mengubah Container Tombol Bank Kata menjadi Inline Flex ke samping */
    div[data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-wrap: wrap !important;
        gap: 8px 10px !important;
        align-items: center !important;
    }
    
    div[data-testid="stHorizontalBlock"] > div {
        flex: 0 0 auto !important;
        width: auto !important;
        min-width: 0 !important;
    }

    /* Tampilan Kotak Kapsul / Pill Sesuai Gambar */
    div[data-testid="stHorizontalBlock"] button {
        border-radius: 50px !important;            /* Bulat lonjong sempurna */
        border: 1px solid #cccccc !important;       /* Garis tepi tipis abu-abu */
        background-color: #ffffff !important;      /* Warna dasar putih */
        color: #333333 !important;                 /* Warna teks gelap */
        font-size: 1.1rem !important;
        padding: 6px 18px !important;               /* Jarak dalam yang empuk */
        box-shadow: none !important;
        transition: all 0.2s ease-in-out !important;
    }

    /* Efek saat tombol di-hover / diklik */
    div[data-testid="stHorizontalBlock"] button:hover {
        border-color: #888888 !important;
        background-color: #f7f7f7 !important;
    }

    /* Kotak Info Soal */
    .info-box {
        background-color: #e8f4fd;
        padding: 15px;
        border-radius: 12px;
        border-left: 5px solid #1fa2ff;
        margin-bottom: 20px;
    }
    .text-bunpou { font-size: 1.05rem; font-weight: bold; color: #1fa2ff; margin: 0 0 6px 0; }
    .text-arti { font-size: 1.2rem; font-weight: bold; color: #1a1a1a; margin: 0; }

    /* Indikator Mode Tukar */
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

# Tampilan Atas
st.title("🦉 Bunpou Master (BAB 2)")
st.caption(f"Soal {soal_sekarang['id']} dari {len(st.session_state.database_soal)}")
st.markdown("---")

# Kotak Petunjuk Soal
st.markdown(f"""
<div class="info-box">
    <p class="text-bunpou">📖 {soal_sekarang['pola']}</p>
    <p class="text-arti">🇮🇩 {soal_sekarang['arti']}</p>
</div>
""", unsafe_allow_html=True)

# --- MENU UTAMA INTERAKTIF (FRAGMENT) ---
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
            st.markdown(f'<div class="swap-indicator">📍 Kata [{kata_terpilih}] terpilih. Klik kata tujuan untuk bertukar posisi!</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="swap-indicator">💡 Klik kata pertama yang ingin ditukar posisinya...</div>', unsafe_allow_html=True)
    else:
        st.session_state.mode_tukar = False
        st.session_state.idx_kata_dipilih = None

    # 1. PAPAN JAWABAN (ST.PILLS)
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

    # 2. BANK KATA PILIHAN (Bentuk Kapsul & Berjajar Alami Ke Samping)
    st.write("### Pilihan Kata:")
    
    cols = st.columns(len(st.session_state.bank_kata))
    for idx, item in enumerate(st.session_state.bank_kata):
        with cols[idx]:
            if item["dipakai"]:
                st.button(" ", key=f"disabled_{item['id']}", disabled=True)
            else:
                if st.button(item["teks"], key=f"pilih_{item['id']}"):
                    item["dipakai"] = True
                    st.session_state.jawaban_user.append(item)
                    st.rerun()

# Jalankan Komponen Utama Kuis
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
    user_joined = "".join(user_strings).replace(" ", "").replace("、", "").replace("。", "")
    kunci_joined = "".join(kunci_strings).replace(" ", "").replace("、", "").replace("。", "")
    
    if user_joined == kunci_joined:
        st.success(f"🎉 **正解 (Benar)!** Susunan bunpou kamu sudah sempurna!\n\n**🇯🇵 Kanji:** {soal_sekarang['kanji']}\n\n**💡 Hiragana:** {soal_sekarang['hiragana']}")
    else:
        st.error(f"❌ **残念 (Kurang Tepat).**\n\n**Susunan yang benar:**\n\n`{' '.join(kunci_strings)}`\n\n**🇯🇵 Kanji asli:** {soal_sekarang['kanji']}\n\n**💡 Hiragana:** {soal_sekarang['hiragana']}")
