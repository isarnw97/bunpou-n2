import streamlit as st

st.set_page_config(page_title="Susun Kata Jepang - Bab 7", layout="centered")

# --- DATABASE SOAL (BERDASARKAN BUKU TEKS ASLI) ---
if "database_soal" not in st.session_state:
    st.session_state.database_soal = [
        # ==================== POIN 1: ～際（に） ====================
        {
            "id": 1,
            "pola": "1. ～際（に）",
            "kanji": "この整理券は、商品受け取りの際、必要です。",
            "hiragana": "このせいりけんは、しょうひんうけとりのさい、ひつようです。",
            "arti": "Kupon ini diperlukan saat mengambil barang.",
            "soal": ["この", "せいりけん", "は", "、", "しょうひん", "うけとり", "の", "さい", "、", "ひつようです", "。"],
            "kunci": ["この", "せいりけん", "は", "、", "しょうひん", "うけとり", "の", "さい", "、", "ひつようです", "。"]
        },
        {
            "id": 2,
            "pola": "1. ～際（に）",
            "kanji": "こちらの会議室をご利用になる際は、受付で必要事項をご記入ください。",
            "hiragana": "こちらのかいぎしつをごりようになるさいは、うけつけでひつようじこうをごきにゅうください。",
            "arti": "Saat akan menggunakan ruang rapat ini, silakan isi informasi yang diperlukan di resepsionis.",
            "soal": ["こちら", "の", "かいぎしつ", "を", "ごりよう", "に", "なる", "さい", "は", "、", "うけつけ", "で", "ひつようじこう", "を", "ごきにゅうください", "。"],
            "kunci": ["こちら", "の", "かいぎしつ", "を", "ごりよう", "に", "なる", "さい", "は", "、", "うけつけ", "で", "ひつようじこう", "を", "ごきにゅうください", "。"]
        },
        {
            "id": 3,
            "pola": "1. ～際（に）",
            "kanji": "アメリカの大統領は来日した際に、わたしたちの大学でスピーチを行った。",
            "hiragana": "あめりかのだいとうりょうはらいにちしたさいに、わたしたちのだいがくですぴーちをおこなった。",
            "arti": "Saat Presiden Amerika berkunjung ke Jepang, beliau berpidato di universitas kami.",
            "soal": ["あめりか", "の", "だいとうりょう", "は", "らいにち", "した", "さい", "に", "、", "わたしたち", "の", "だいがく", "で", "すぴーち", "を", "おこなった", "。"],
            "kunci": ["あめりか", "の", "だいとうりょう", "は", "らいにち", "した", "さい", "に", "、", "わたしたち", "の", "だいがく", "で", "すぴーち", "を", "おこなった", "。"]
        },

        # ==================== POIN 2: ～に際して・～にあたって ====================
        {
            "id": 4,
            "pola": "2. ～に際して・～にあたって",
            "kanji": "工事関係者は工事を始めるに際して、近所の住民であいさつをして回った。",
            "hiragana": "こうじかんけいしゃはこうじをはじめるにさいして、きんじょのじゅうみんにあいさつをしてまわった。",
            "arti": "Pihak konstruksi berkeliling menyampaikan salam kepada warga sekitar saat akan memulai pembangunan.",
            "soal": ["こうじかんけいしゃ", "は", "こうじ", "を", "はじめる", "にさいして", "、", "きんじょ", "の", "じゅうみん", "に", "あいさつ", "を", "して", "まわった", "。"],
            "kunci": ["こうじかんけいしゃ", "は", "こうじ", "を", "はじめる", "にさいして", "、", "きんじょ", "の", "じゅうみん", "に", "あいさつ", "を", "して", "まわった", "。"]
        },
        {
            "id": 5,
            "pola": "2. ～に際して・～にあたって",
            "kanji": "当ショッピングサイトのご利用に際して、以下のご利用条件をよくお読みください。",
            "hiragana": "とうしょっぴんぐさいとのごりようにさいして、いかのごりようじょうけんをよくおよみください。",
            "arti": "Saat akan menggunakan situs belanja ini, harap baca syarat dan ketentuan penggunaan di bawah ini dengan cermat.",
            "soal": ["とうしょっぴんぐさいと", "の", "ごりよう", "にさいして", "、", "いかの", "ごりようじょうけん", "を", "よく", "およみください", "。"],
            "kunci": ["とうしょっぴんぐさいと", "の", "ごりよう", "にさいして", "、", "いかの", "ごりようじょうけん", "を", "よく", "およみください", "。"]
        },
        {
            "id": 6,
            "pola": "2. ～に際して・～にあたって",
            "kanji": "新しく事業を始めるにあたって、しっかりと準備をしようと思っております。",
            "hiragana": "あたらしくじぎょうをはじめるにあたって、しっかりとじゅんびをしようとおもっております。",
            "arti": "Dalam rangka memulai bisnis baru, kami berniat untuk melakukan persiapan dengan matang.",
            "soal": ["あたらしく", "じぎょう", "を", "はじめる", "にあたって", "、", "しっかり", "と", "じゅんび", "を", "しよう", "と", "おもっております", "。"],
            "kunci": ["あたらしく", "じぎょう", "を", "はじめる", "にあたって", "、", "しっかり", "と", "じゅんび", "を", "しよう", "と", "おもっております", "。"]
        },
        {
            "id": 7,
            "pola": "2. ～に際して・～にあたって",
            "kanji": "お二人の門出にあたりまして、お祝いのお言葉を申し上げます。",
            "hiragana": "おふたりのかどであたりまして、おいわいのおことばをもうしあげます。",
            "arti": "Menyambut lembaran baru Anda berdua, saya ingin menyampaikan ucapan selamat.",
            "soal": ["おふたり", "の", "かどで", "にあたりまして", "、", "おいわい", "の", "おことば", "を", "もうしあげます", "。"],
            "kunci": ["おふたり", "の", "かどで", "にあたりまして", "、", "おいわい", "の", "おことば", "を", "もうしあげます", "。"]
        },
        {
            "id": 8,
            "pola": "2. ～に際して・～にあたって",
            "kanji": "日本で開催する国際会議にあたり、関係各方面からの協力を得た。",
            "hiragana": "にほんてかいさいするこくさいかいぎにあたり、かんけいかくほうめんからのきょうりょくをえた。",
            "arti": "Menjelang penyelenggaraan konferensi internasional di Jepang, kami mendapatkan kerja sama dari berbagai pihak terkait.",
            "soal": ["にほん", "で", "かいさいする", "こくさいかいぎ", "にあたり", "、", "かんけいかくほうめん", "からの", "きょうりょく", "を", "えた", "。"],
            "kunci": ["にほん", "で", "かいさいする", "こくさいかいぎ", "にあたり", "、", "かんけいかくほうめん", "からの", "きょうりょく", "を", "えた", "。"]
        },

        # ==================== POIN 3: ～たとたん（に） ====================
        {
            "id": 9,
            "pola": "3. ～たとたん（に）",
            "kanji": "山の頂上でワインを一口飲んだ途端に、めまいがした。",
            "hiragana": "やまのちょうじょうでわいんをひとくちのんだたとたんに、めまいがした。",
            "arti": "Begitu meminum seteguk anggur di puncak gunung, saya langsung merasa pusing.",
            "soal": ["やま", "の", "ちょうじょう", "で", "わいん", "を", "ひとくち", "のんだ", "たとたんに", "、", "めまい", "が", "した", "。"],
            "kunci": ["やま", "の", "ちょうじょう", "で", "わいん", "を", "ひとくち", "のんだ", "たとたんに", "、", "めまい", "が", "した", "。"]
        },
        {
            "id": 10,
            "pola": "3. ～たとたん（に）",
            "kanji": "結婚前は優しかった夫が、結婚した途端に態度が変わった。",
            "hiragana": "けっこんまえはやさしかったおっとが、けっこんしたたとたんにたいどかわった。",
            "arti": "Suami yang sangat baik sebelum menikah, begitu setelah menikah sikapnya langsung berubah.",
            "soal": ["けっこん", "まえ", "は", "やさしかった", "おっと", "が", "、", "けっこん", "した", "たとたん", "に", "たいど", "が", "かわった", "。"],
            "kunci": ["けっこん", "まえ", "は", "やさしかった", "おっと", "が", "、", "けっこん", "した", "たとたん", "に", "たいど", "が", "かわった", "。"]
        },
        {
            "id": 11,
            "pola": "3. ～たとたん（に）",
            "kanji": "国の母に電話をかけた。母の声を聞いた途端に、涙があふれてきた。",
            "hiragana": "くにのははにでんわをかけた。ははのこえをきいたたとたんに、なみだがあふれてきた。",
            "arti": "Saya menelepon ibu di kampung halaman. Begitu mendengar suara ibu, air mata saya langsung menetes deras.",
            "soal": ["くに", "の", "はは", "に", "でんわ", "を", "かけた", "。", "はは", "の", "こえ", "を", "きいた", "たとたん", "に", "、", "なみだ", "が", "あふれてきた", "。"],
            "kunci": ["くに", "の", "はは", "に", "でんわ", "を", "かけた", "。", "はは", "の", "こえ", "を", "きいた", "たとたん", "に", "、", "なみだ", "が", "あふれてきた", "。"]
        },
        {
            "id": 12,
            "pola": "3. ～たとたん（に）",
            "kanji": "ぼくが「さよなら」と言った途端、彼女は走っていってしまった。",
            "hiragana": "ぼくが「さよなら」といったら、かのじょははしっていってしまった。",
            "arti": "Sesaat setelah saya mengucapkan 'selamat tinggal', dia langsung berlari pergi.",
            "soal": ["ぼく", "が", "「さよなら」", "と", "いった", "たとたん", "、", "かのじょ", "は", "はしって", "いってしまった", "。"],
            "kunci": ["ぼく", "が", "「さよらな」", "と", "いった", "たとたん", "、", "かのじょ", "は", "はしって", "いってしまった", "。"]
        },

        # ==================== POIN 4: ～（か）と思うと・～（か）と思ったら ====================
        {
            "id": 13,
            "pola": "4. ～（か）と思うと・～（か）と思ったら",
            "kanji": "林さんが部屋の窓を全部開けたかと思うと、いきなり入ってきた。",
            "hiragana": "はやしさんがへやのまどをぜんぶあけたかとおもうと、いきなりはいってきた。",
            "arti": "Baru saja Hayashi-san membuka semua jendela kamar, tiba-tiba dia langsung masuk.",
            "soal": ["はやしさん", "が", "へや", "の", "まど", "を", "ぜんぶ", "あけた", "かとおもうと", "、", "いきなり", "はいってきた", "。"],
            "kunci": ["はやしさん", "が", "へや", "の", "まど", "を", "ぜんぶ", "あけた", "かとおもうと", "、", "いきなり", "はいってきた", "。"]
        },
        {
            "id": 14,
            "pola": "4. ～（か）と思うと・～（か）と思ったら",
            "kanji": "赤ちゃんは今笑っていると思ったら、もう泣いた。",
            "hiragana": "あかちゃんはいままわらっているとおもったら、もうないた。",
            "arti": "Bayi itu baru saja tertawa, tetapi seketika itu juga langsung menangis.",
            "soal": ["あかちゃん", "は", "いま", "わらっている", "とおもったら", "、", "もう", "ないた", "。"],
            "kunci": ["あかちゃん", "は", "いま", "わらっている", "とおもったら", "、", "もう", "ないた", "。"]
        },
        {
            "id": 15,
            "pola": "4. ～（か）と思うと・～（か）と思ったら",
            "kanji": "子供たちが散らかした部屋がやっと片付いたと思ったら、またすぐ散らかした。",
            "hiragana": "こどもたちがちらかしたへやがやっとかたづいたとおもったら、またすぐちらかした。",
            "arti": "Kamar yang diacak-acak anak-anak baru saja selesai dibersihkan, eh langsung berantakan lagi.",
            "soal": ["こどもたち", "が", "ちらかした", "へや", "が", "やっと", "かたづいた", "とおもったら", "、", "また", "すぐ", "ちらかした", "。"],
            "kunci": ["こどもたち", "が", "ちらかした", "へや", "が", "やっと", "かたづいた", "とおもったら", "、", "また", "すぐ", "ちらかした", "。"]
        },
        {
            "id": 16,
            "pola": "4. ～（か）と思うと・～（か）と思ったら",
            "kanji": "この頃は気温の差が大きい。昨日は涼しいかと思ったら、今日は暑くなった。",
            "hiragana": "このごろはきおんのさがおおきい。きのうはすずしいかとおもったら、きょうはあつくなった。",
            "arti": "Akhir-akhir ini perbedaan suhunya lumayan ekstrem. Kemarin rasanya sejuk, eh hari ini malah jadi panas.",
            "soal": ["このごろ", "は", "きおん", "の", "さ", "が", "おおきい", "。", "きのう", "は", "すずしい", "かとおもったら", "、", "きょう", "は", "あつくなった", "。"],
            "kunci": ["このごろ", "は", "きおん", "の", "さ", "が", "おおきい", "。", "きのう", "は", "すずしい", "かとおもったら", "、", "きょう", "は", "あつくなった", "。"]
        },

        # ==================== POIN 5: ～か～ないかのうちに ====================
        {
            "id": 17,
            "pola": "5. ～か～ないかのうちに",
            "kanji": "一郎はベッドに横になるかないかのうちに、ぐっすり眠ってしまった。",
            "hiragana": "いちろうはべっどによこになるかないかのうちに、ぐっすりねむってしまった。",
            "arti": "Ichiro baru saja berbaring di tempat tidur, dia sudah tertidur nyenyak.",
            "soal": ["いちろう", "は", "べっど", "に", "よこになる", "か", "ないかのうちに", "、", "ぐっすり", "ねむってしまった", "。"],
            "kunci": ["いちろう", "は", "べっど", "に", "よこになる", "か", "ないかのうちに", "、", "ぐっすり", "ねむってしまった", "。"]
        },
        {
            "id": 18,
            "pola": "5. ～か～ないかのうちに",
            "kanji": "わたしは夜が明けるか明けないかのうちに家を出て、空港へ向かった。",
            "hiragana": "わたしはよるがあけるかあけないかのうちにいえをでて、くうこうへむかった。",
            "arti": "Bahkan sebelum fajar menyingsing, saya sudah keluar rumah dan berangkat menuju bandara.",
            "soal": ["わたし", "は", "よる", "が", "あける", "か", "あけない", "かのうちに", "いえ", "を", "でて", "、", "くうこう", "へ", "むかった", "。"],
            "kunci": ["わたし", "は", "よる", "が", "あける", "か", "あけない", "かのうちに", "いえ", "を", "でて", "、", "くうこう", "へ", "むかった", "。"]
        },
        {
            "id": 19,
            "pola": "5. ～か～ないかのうちに",
            "kanji": "あの話題作の売れっ子作家は作品を発表したかないかのうちに、もう次に取りかかっているそうだ。",
            "hiragana": "あのわだいさくのうれっこさっかはさくひんをはっぴょうしたかないかのうちに、もうつぎにとりかかっているそうだ。",
            "arti": "Penulis populer itu kabarnya baru saja merilis karya barunya, tetapi langsung sibuk mengerjakan karya berikutnya.",
            "soal": ["あの", "わだいさく", "の", "うれっこ", "さっか", "は", "さくひん", "を", "はっぴょうした", "か", "ないかのうちに", "、", "もう", "つぎ", "に", "とりかかっている", "そうだ", "。"],
            "kunci": ["あの", "わだいさく", "の", "うれっこ", "さっか", "は", "さくひん", "を", "はっぴょうした", "か", "ないかのうちに", "、", "もう", "つぎ", "に", "とりかかっている", "そうだ", "。"]
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

soal_sekarang = st.session_state.database_soal[st.session_state.index_soal]

if not st.session_state.bank_kata and not st.session_state.jawaban_user:
    import random
    soal_acak = list(soal_sekarang["soal"])
    random.seed(42) # Agar hasil acakan stabil
    random.shuffle(soal_acak)
    st.session_state.bank_kata = [{"id": i, "teks": kata, "dipakai": False} for i, kata in enumerate(soal_acak)]

# --- STYLING CSS ---
st.markdown("""
<style>
    div[data-testid="stStatusWidget"] + div div[data-testid="stWidgetLabel"] {
        display: none;
    }
    [data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: wrap !important;
        gap: 6px !important;
    }
    [data-testid="stHorizontalBlock"] > div {
        flex: 1 1 22% !important; 
        min-width: 70px !important; 
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
    div.stButton > button {
        border-radius: 12px !important;
        font-weight: bold !important;
        padding: 6px 10px !important;
    }
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
st.title("🦉 Bunpou Master (BAB 7)")
st.caption(f"Soal {st.session_state.index_soal + 1} dari {len(st.session_state.database_soal)}")
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
            st.markdown(f'<div class="swap-indicator">📍 Kata [{kata_terpilih}] terpilih. Sekarang klik kata tujuan untuk bertukar posisi!</div>', unsafe_allow_html=True)
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
        st.success(f"🎉 **正解 (Benar)!** Susunan bunpou kamu sudah sempurna!\n\n**🇯🇵 Kanji:** {soal_sekarang['kanji']}\n\n**💡 Hiragana:** {soal_sekarang['hiragana']}")
    else:
        st.error(f"❌ **残念 (Kurang Tepat).**\n\n**Susunan yang benar:**\n\n`{' '.join(kunci_strings)}`\n\n**🇯🇵 Kanji asli:** {soal_sekarang['kanji']}\n\n**💡 Hiragana:** {soal_sekarang['hiragana']}")
