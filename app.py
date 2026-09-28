import streamlit as st

st.set_page_config(page_title="Susun Kata Jepang - Bunpou Master", layout="centered")

# --- DATABASE SOAL (6 POLA GRAMMAR LENGKAP) ---
if "database_soal" not in st.session_state:
    st.session_state.database_soal = [
        # === POLA 1: ～をはじめ（として） ===
        {
            "id": 1,
            "pola": "1. ～をはじめ（として）",
            "kanji": "この体育館では水泳をはじめ、いろいろなスポーツが楽しめる。",
            "hiragana": "この たいいくかんでは すいえいを はじめ、 いろいろな スポーツが たのしめる。",
            "arti": "Di gedung olahraga ini, kita bisa menikmati berbagai macam olahraga, dimulai dari renang.",
            "kunci": ["この", "体育館", "では", "水泳", "を", "はじめ", "、", "いろいろな", "スポーツ", "が", "楽しめる", "。"],
            "soal": ["たのしめる", "すいえい", "いろいろな", "スポーツ", "はじめ", "この", "が", "を", "たいいくかん", "で", "は", "、"。"]
        },
        {
            "id": 2,
            "pola": "1. ～をはじめ（として）",
            "kanji": "日本には「桃太郎」をはじめとして、おじいさん、おばあさんが出てくる昔話が多い。",
            "hiragana": "にほんには 「ももたろう」を はじめとして、 おじいさん、 おばあさんが でてくる むかしばなしが おおい。",
            "arti": "Di Jepang ada banyak cerita rakyat yang menampilkan kakek dan nenek, dimulai dari \"Momotaro\".",
            "kunci": ["日本", "に", "は", "「桃太郎」", "を", "はじめとして", "、", "おじいさん", "、", "おばあさん", "が", "出てくる", "昔話", "が", "多い", "。"],
            "soal": ["おばあさん", "ももたろう", "に", "が", "でてくる", "は", "むかしばなし", "おじいさん", "にっぽん", "おおい", "を", "はじめとして", "が", "、", "、"]
        },
        {
            "id": 3,
            "pola": "1. ～をはじめ（として）",
            "kanji": "このあたりには、市役所をはじめとする市の公共の建物が多い。",
            "hiragana": "この あたりには、 しやくしょを はじめとする しの こうきょうの たてものが おおい。",
            "arti": "Di sekitar daerah ini, ada banyak bangunan publik kota, dimulai dari kantor balai kota.",
            "kunci": ["この", "あたり", "に", "は", "、", "市役所", "を", "はじめとする", "市", "の", "公共", "の", "建物", "が", "多い", "。"],
            "soal": ["しの", "おおい", "はじめとする", "この", "あたり", "に", "しやくしょ", "を", "こうきょう", "の", "たてもの", "が", "は", "、"]
        },

        # === POLA 2: ～からして ===
        {
            "id": 4,
            "pola": "2. ～からして",
            "kanji": "この旅行の計画には無理がある。出発時間からして早すぎる。",
            "hiragana": "この りょこうの けいかくには むりが ある。 しゅっぱつじかん からして はやすぎる。",
            "arti": "Rencana perjalanan ini tidak masuk akal. Dari waktu keberangkatannya saja sudah terlalu pagi.",
            "kunci": ["この", "旅行", "の", "計画", "に", "は", "無理", "が", "ある", "。", "出発時間", "からして", "早すぎる", "。"],
            "soal": ["で", "は", "はやすぎる", "しゅっぱつじかん", "りょこう", "の", "からして", "むり", "の", "けいかく", "に", "この", "が", "ある"]
        },
        {
            "id": 5,
            "pola": "2. ～からして",
            "kanji": "わたしはどうも猫が苦手だ。あの光る目からして何となく怖い感じがする。",
            "hiragana": "わたしは どうも ねこが にがてだ。 あの ひかる めからして なんとなく こわい かんじが する。",
            "arti": "Saya sepertinya kurang suka kucing. Dari matanya yang bersinar saja entah kenapa terasa menakutkan.",
            "kunci": ["わたし", "は", "どうも", "猫", "が", "苦手だ", "。", "あの", "光る", "目", "からして", "何となく", "怖い", "感じ", "が", "する", "。"],
            "soal": ["こわい", "ねこ", "からして", "にがてだ", "の", "かんじ", "わたし", "が", "どうも", "あかるい", "め", "が", "する"]
        },
        {
            "id": 6,
            "pola": "2. ～からして",
            "kanji": "わたしと夫とは似ているところが少ない。第一、食べ物の好みからして正反対だ。",
            "hiragana": "わたしと おっととは にている ところが すくない。 だいいち、 たべものの このみからして せいはんたいだ。",
            "arti": "Saya dan suami punya sedikit kemiripan. Pertama-tama, dari selera makanan saja sudah bertolak belakang.",
            "kunci": ["わたし", "と", "夫", "と", "は", "似ている", "ところ", "が", "少ない", "。", "第一", "、", "食べ物", "の", "好み", "からして", "正反対だ", "。"],
            "soal": ["と", "にた", "たべもの", "せいはんたいだ", "わたし", "ところ", "の", "おっと", "は", "が", "だ", "の", "すくない", "だいいち", "からして", "このみ", "、"]
        },
        {
            "id": 7,
            "pola": "2. ～からして",
            "kanji": "さすがプロの選手は走り方からしてわたしたちとは違う。",
            "hiragana": "さすが プロの せんしゅは はしりがた からして わたしたちとは ちがう。",
            "arti": "Seperti yang diharapkan dari atlet profesional, dari cara larinya saja sudah berbeda dari kita.",
            "kunci": ["さすが", "プロ", "の", "選手", "は", "走り方", "からして", "わたし・たち", "と", "は", "違う", "。"],
            "soal": ["はしりがた", "さすが", "と", "ちがう", "プロ", "の", "は", "せんしゅ", "わたし・たち", "からして"]
        },

        # === POLA 3: ～にわたって ===
        {
            "id": 8,
            "pola": "3. ～にわたって",
            "kanji": "連休の最終日、高速道路は20キロにわたって渋滞が続いた。",
            "hiragana": "れんきゅうの さいしゅうび、 こうそくどうろは にじゅっキロに わたって じゅうたいが つづいた。",
            "arti": "Pada hari terakhir libur panjang, kemacetan berlanjut sepanjang 20 km di jalan tol.",
            "kunci": ["連休", "の", "最終日", "、", "高速道路", "は", "２０キロ", "に", "わたって", "渋滞", "が", "づづいた", "。"],
            "soal": ["じゅうたい", "に", "さいしゅうび", "こうそくどうろ", "れんきゅう", "２０キロ", "の", "わたって", "づづいた", "が", "は", "、"]
        },
        {
            "id": 9,
            "pola": "3. ～にわたって",
            "kanji": "彼はいろいろなジャンルにわたり、たくさんの本を読んでいる。",
            "hiragana": "かれは いろいろな ジャンルに わたり、 たくさんの ほんを よんでいる。",
            "arti": "Dia membaca banyak buku yang mencakup berbagai macam genre.",
            "kunci": ["彼", "は", "いろいろな", "ジャンル", "に", "わたり", "、", "たくさん", "の", "本", "を", "読んでいる", "。"],
            "soal": ["かれ", "を", "に", "たくさん", "いろいろな", "ほん", "よんでいる", "ジャンル", "わたし", "の", "、"]
        },
        {
            "id": 10,
            "pola": "3. ～にわたって",
            "kanji": "3日間にわたる研究発表大会が、無事終了しました。",
            "hiragana": "みっかかんに わたる けんきゅう はっぴょう たいかいが、 ぶじ しゅうりょう しました。",
            "arti": "Konferensi presentasi penelitian yang berlangsung selama 3 hari telah selesai dengan lancar.",
            "kunci": ["さんにちかん", "に", "わたる", "研究発表大会", "が", "、", "むじ事", "完了しました", "。"],
            "soal": ["かんりょうしました", "けんきゅうひょうひょうたいかい", "が", "さんにちかん", "むじ事", "に", "わたる", "、"]
        },

        # === POLA 4: ～を通じて/を通して ===
        {
            "id": 11,
            "pola": "4. ～を通じて/を通して",
            "kanji": "この町には四季を通じて観光客が訪れる。",
            "hiragana": "この まちには しきを つうじて かんこうきゃくが おとずれる。",
            "arti": "Wisatawan mengunjungi kota ini sepanjang empat musim.",
            "kunci": ["この", "町", "に", "は", "四季", "を", "を通じて", "観光客", "が", "訪れる", "。"],
            "soal": ["かんこうきゃく", "この", "は", "しき", "に", "まち", "を", "おとずれる", "つうじて", "が", "、"]
        },
        {
            "id": 12,
            "pola": "4. ～を通じて/を通して",
            "kanji": "在職期間を通して皆様には大変お世話になりました。",
            "hiragana": "ざいしょく きかんを とおして みなさまには たいへん おせわに なりました。",
            "arti": "Selama masa jabatan saya, terima kasih banyak atas segala bantuan dari Anda sekalian.",
            "kunci": ["在職期間", "を", "を通して", "皆様", "に", "は", "大変", "お世話", "に", "なりました", "。"],
            "soal": ["みなさま", "ざいしょくきかん", "に", "お世話", "たいへん", "を", "に", "とおして", "は", "なりました", "、"]
        },
        {
            "id": 13,
            "pola": "4. ～を通じて/を通して",
            "kanji": "この10年間を通じ、彼はいつも新しいことに挑戦していた。",
            "hiragana": "この じゅうねんかんを つうじ、 かれは いつも あたらしい ことに ちょうせん していた。",
            "arti": "Sepanjang 10 tahun ini, dia selalu menantang hal-hal baru.",
            "kunci": ["この", "１０年間", "を", "通じ", "、", "彼", "は", "いつも", "新しい", "こと", "に", "挑戦", "していた", "。"],
            "soal": ["ちょうせん", "いつも", "に", "は", "あたらしい", "かれ", "この", "１０ねんかん", "を", "つうじ", "していた", "こと", "、"]
        },
        {
            "id": 14,
            "pola": "4. ～を通じて/を通して",
            "kanji": "今日では、インターネットを通じて世界中の情報が手に入る。",
            "hiragana": "こんにちでは、 インターネットを つうじて せかいじゅうの じょうほうが てに はいる。",
            "arti": "Hari ini, informasi dari seluruh dunia dapat diperoleh melalui internet.",
            "kunci": ["日々に", "で", "は", "、", "インターネット", "を", "通じて", "世界中", "の", "情報", "が", "手", "に", "入る", "。"],
            "soal": ["てに", "つうじて", "じょうほう", "はじる", "にちにち", "が", "インターネット", "せかいじゅう", "を", "の", "では", "、"]
        },
        {
            "id": 15,
            "pola": "4. ～を通じて/を通して",
            "kanji": "わたしたちは、ボランティア活動を通していろいろな国の人たちと交流を深めている。",
            "hiragana": "わたしたちは、 ボランティア かつどうを とおして いろいろな くにの ひとたちと こうりゅうを ふかめている。",
            "arti": "Kami mempererat pertukaran budaya dengan orang-orang dari berbagai negara melalui kegiatan sukarela.",
            "kunci": ["わたし・たち", "は", "、", "ボランティア活動", "を", "通して", "いろいろな", "国", "の", "人・たち", "と", "交流", "を", "深めている", "。"],
            "soal": ["わたしたち", "こうりゅう", "を", "ボランティアかつどう", "くに", "ふかめている", "いろいろな", "と", "の", "とおして", "ひと・たち", "は", "、"]
        },

        # === POLA 5: ～限り ===
        {
            "id": 16,
            "pola": "5. ～限り",
            "kanji": "環境を守るためにわたしもできる限りことをしたい。",
            "hiragana": "かんきょうを まもる ために わたしも できる かぎりの ことを したい。",
            "arti": "Saya ingin melakukan hal-hal semampu saya untuk melindungi環境 (lingkungan).",
            "kunci": ["環境", "を", "守る", "ため", "に", "わたし", "も", "できる", "限り", "の", "こと", "を", "したい", "。"],
            "soal": ["まもる", "こと", "かんきょう", "の", "を", "わたし", "できる", "かぎり", "も", "ため", "を", "に", "したい", "、"]
        },
        {
            "id": 17,
            "pola": "5. ～限り",
            "kanji": "君が知っている限りのことを全部わたしに話してほしい。",
            "hiragana": "きみが しっている かぎりの ことを ぜんぶ わたしに はなして ほしい。",
            "arti": "Saya ingin kamu menceritakan semua hal sebatas yang kamu ketahui kepada saya.",
            "kunci": ["君", "が", "知って・いる", "限り", "の", "こと", "を", "全部", "わたし", "に", "話して", "ほしい", "。"],
            "soal": ["の", "かぎり", "ぜんぶ", "はなし", "きみ", "わたし", "こと", "ほしい", "が", "を", "に", "しって・いる", "て", "、"]
        },
        {
            "id": 18,
            "pola": "5. ～限り",
            "kanji": "あしたはいよいよ試合だ。力の限り頑張ろう。",
            "hiragana": "あしたは いよいよ しあいだ。 ちからの かぎり がんばろう。",
            "arti": "Besok akhirnya pertandingan. Mari berjuang sekuat tenaga.",
            "kunci": ["あした", "は", "いよいよ", "試合", "だ", "。", "力", "の", "限り", "頑張ろう", "。"],
            "soal": ["ちから", "あした", "だ", "しあわせ", "いよいよ", "は", "の", "かぎり", "がんばろう", "、"]
        },

        # === POLA 6: ～だけ ===
        {
            "id": 19,
            "pola": "6. ～だけ",
            "kanji": "ここにあるダンボールを、車に積めるだけ積んで持って帰ってください。",
            "hiragana": "ここに ある ダンボールを、 くるまに つめるだけ つんで もって かえってください。",
            "arti": "Silakan muat kardus yang ada di sini sebanyak yang muat di mobil lalu bawa pulang.",
            "kunci": ["ここ", "に", "ある", "ダンボール", "を", "、", "車", "に", "積めるだけ", "積んで", "持って", "帰ってください", "。"],
            "soal": ["くろ", "つめる", "だんぼーる", "ここ", "に", "つんで", "もって", "ある", "かえってください", "だけ", "を", "くるま", "に", "、"]
        },
        {
            "id": 20,
            "pola": "6. ～だけ",
            "kanji": "父は働くだけ働いて、定年前に退職してしまった。",
            "hiragana": "ちちは はたらくだけ はたらいて、 ていねんまえに たいしょく して しまった。",
            "arti": "Ayah bekerja keras sebisanya, lalu pensiun sebelum usianya.",
            "kunci": ["父", "は", "働くだけ", "働いて", "、", "定年前", "に", "退職して", "しまった", "。"],
            "soal": ["はたらくだけ", "ていねんまえ", "ちち", "はたらいて", "に", "しまった", "たいしょくして", "は", "、"]
        },
        {
            "id": 21,
            "pola": "6. ～だけ",
            "kanji": "今日は部長に言いたいだけの不満を全部言って、すっきりした。",
            "hiragana": "きょうは ぶちょうに いいたいだけ の ふまんを ぜんぶ いって、 すっきりした。",
            "arti": "Hari ini saya merasa lega setelah mengungkapkan semua ketidakpuasan sepuasnya kepada manajer.",
            "kunci": ["今日", "は", "部長", "に", "言いたいだけ", "の", "不満", "を", "全部", "言って", "、", "すっきりした", "。"],
            "soal": ["いいたい", "いって", "ぶちょう", "ふまん", "ぜんぶ", "きょう", "だけ", "の", "は", "に", "を", "すっきりした", "、"]
        },
        {
            "id": 22,
            "pola": "6. ～だけ",
            "kanji": "バイキング形式の食事ですから、好きなものを好きなだけ取ってお召し上がりください。",
            "hiragana": "バイキング けいしきの しょくじ ですから、 すきな ものを すきなだけ とって おめしあがり ください。",
            "arti": "Karena ini makanan prasmanan, silakan ambil dan nikmati apa yang Anda sukai sebanyak yang Anda suka.",
            "kunci": ["バイキング形式", "の", "食事", "ですから", "、", "好きな", "もの", "を", "好きなだけ", "取って", "お召し上がり", "ください", "。"],
            "soal": ["おめしあがり", "バイキングけいしき", "すきな", "を", "すきな", "ですから", "ください", "だけ", "とって", "の", "しょくじ", "、"]
        }
    ]

# --- INISIALISASI STATE ---
if "pola_terpilih" not in st.session_state:
    st.session_state.pola_terpilih = "Semua Pola"

if "index_soal_lokal" not in st.session_state:
    st.session_state.index_soal_lokal = 0

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

# --- CUSTOM CSS ---
st.markdown("""
<style>
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

    div[data-testid="stHorizontalBlock"] button {
        border-radius: 50px !important;
        border: 1px solid #cccccc !important;
        background-color: #ffffff !important;
        color: #333333 !important;
        font-size: 1.1rem !important;
        padding: 6px 18px !important;
        box-shadow: none !important;
        transition: all 0.2s ease-in-out !important;
    }

    div[data-testid="stHorizontalBlock"] button:hover {
        border-color: #888888 !important;
        background-color: #f7f7f7 !important;
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

# Tampilan Header
st.title("🦉 Bunpou Master")

# --- DROPDOWN PILIH POLA GRAMMAR ---
daftar_pola_unik = list(dict.fromkeys([item["pola"] for item in st.session_state.database_soal]))
opsi_pola = ["Semua Pola"] + daftar_pola_unik

pola_terpilih = st.selectbox(
    "📖 **Pilih Pola Grammar:**",
    options=opsi_pola,
    index=opsi_pola.index(st.session_state.pola_terpilih) if st.session_state.pola_terpilih in opsi_pola else 0,
    key="select_pola"
)

# Cek pergantian filter
if pola_terpilih != st.session_state.pola_terpilih:
    st.session_state.pola_terpilih = pola_terpilih
    st.session_state.index_soal_lokal = 0
    st.session_state.jawaban_user = []
    st.session_state.bank_kata = []
    st.session_state.idx_kata_dipilih = None
    st.session_state.status_periksa = False
    st.rerun()

# Filter Soal
if st.session_state.pola_terpilih == "Semua Pola":
    soal_terfilter = st.session_state.database_soal
else:
    soal_terfilter = [s for s in st.session_state.database_soal if s["pola"] == st.session_state.pola_terpilih]

if st.session_state.index_soal_lokal >= len(soal_terfilter):
    st.session_state.index_soal_lokal = 0

soal_sekarang = soal_terfilter[st.session_state.index_soal_lokal]

# Inisialisasi Bank Kata
if not st.session_state.bank_kata and not st.session_state.jawaban_user:
    st.session_state.bank_kata = [{"id": i, "teks": kata, "dipakai": False} for i, kata in enumerate(soal_sekarang["soal"])]

st.markdown("---")

# Tampilkan Informasi Soal
st.caption(f"Menampilkan Soal **{st.session_state.index_soal_lokal + 1}** dari **{len(soal_terfilter)}** untuk kategori ini (ID Soal: #{soal_sekarang['id']})")

# Kotak Petunjuk
st.markdown(f"""
<div class="info-box">
    <p class="text-bunpou">📖 {soal_sekarang['pola']}</p>
    <p class="text-arti">🇮🇩 {soal_sekarang['arti']}</p>
</div>
""", unsafe_allow_html=True)

# --- FRAGMENT KUIS ---
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

    # 2. BANK KATA PILIHAN
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

render_kuis_lengkap()

st.markdown("<br><hr>", unsafe_allow_html=True)

# 3. TOMBOL NAVIGASI
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
        st.session_state.index_soal_lokal = (st.session_state.index_soal_lokal + 1) % len(soal_terfilter)
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
