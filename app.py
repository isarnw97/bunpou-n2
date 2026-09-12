import streamlit as st

st.set_page_config(page_title="Susun Kata Jepang - Bab 7", layout="centered")

# --- DATABASE SOAL (BAB 7: POIN 1 - 5) ---
if "database_soal" not in st.session_state:
    st.session_state.database_soal = [
        # --- POIN 1: 〜に際して / 〜際 ---
        {
            "id": 1,
            "pola": "1. 〜際（に）",
            "kanji": "この商品のお受け取りの際は、整理券が必要です。",
            "hiragana": "このしょうひんのおうけとりのさいは、せいりけんがひつようです。",
            "arti": "Saat menerima barang ini, diperlukan kupon/nomor antrean.",
            "kunci": ["この", "しょうひん", "の", "お受け取り", "の", "さい", "は", "、", "せいりけん", "が", "ひつようです", "。"],
            "soal": ["この", "さい", "ひつようです", "うけとり", "しょうひん", "の", "せいりけん", "は", "、", "が", "お", "の"]
        },
        {
            "id": 2,
            "pola": "1. 〜際（に）",
            "kanji": " me! 会議室をご利用の際は、 me! こちらで必要事項をご記入ください。",
            "hiragana": "かいぎしつをごりようのさいは、こちらでひつようじこうをごきにゅうください。",
            "arti": "Saat menggunakan ruang rapat, silakan isi formulir informasi yang diperlukan di sini.",
            "kunci": ["かいぎしつ", "を", "ごりよう", "の", "さい", "は", "、", "こちら", "で", "ひつようじこう", "を", "ごきにゅうください", "。"],
            "soal": ["ひつようじこう", "を", "うけつけ", "かいぎしつ", "に", "こちら", "で", "さい", "の", "ごきにゅうください", "ごりよう", "は", "、", "を", "になる"]
        },
        {
            "id": 3,
            "pola": "1. 〜際（に）",
            "kanji": "アメリカ大統領が来日した際、 me! わたしたちの大学でスピーチを行った。",
            "hiragana": "あめりくだいとうりょうがらいにちしたさい、わたしたちのだいがくですぴーちをおこなった。",
            "arti": "Saat Presiden Amerika berkunjung ke Jepang, beliau berpidato di universitas kami.",
            "kunci": ["あめりか", "だいとうりょう", "が", "らいにち", "した", "さい", "、", "わたしたち", "の", "だいがく", "で", "すぴーち", "を", "おこなった", "。"],
            "soal": ["だいがく", "わたしたち", "だいとうりょう", "で", "すぴーち", "に", "らいにち", "の", "を", "おこなった", "あめりか", "さい", "した", "、", "が"]
        },

        # --- POIN 2: 〜に際して・〜にあたって ---
        {
            "id": 4,
            "pola": "2. 〜に際して・〜にあたって",
            "kanji": "工事を始めるに際して、 me! 近所の住民にご挨拶に回った。",
            "hiragana": "こうじをはじめるにさいして、きんじょのじゅうみんにあいさつにまわった。",
            "arti": "Saat akan memulai pembangunan, kami berkeliling menyampaikan salam kepada warga sekitar.",
            "kunci": ["こうじ", "を", "はじめる", "にさいして", "、", "きんじょ", "の", "じゅうみん", "に", "あいさつ", "に", "まわった", "。"],
            "soal": ["こうじ", "こうじかんけいしゃ", "に", "まわった", "あいさつ", "を", "きんじょ", "はじめる", "じゅうみん", "にさいして", "の", "は", "して", "、", "に"]
        },
        {
            "id": 5,
            "pola": "2. 〜に際して・〜にあたって",
            "kanji": "当ショッピングサイトのご利用に際して、 me! 以下のご利用条件をよくお読みください。",
            "hiragana": "とうしょっぴんぐさいとのごりようにさいして、いかのごりようじょうけんをよくおよみください。",
            "arti": "Saat akan menggunakan situs belanja ini, harap baca syarat dan ketentuan penggunaan di bawah ini dengan cermat.",
            "kunci": ["とうしょっぴんぐさいと", "の", "ごりよう", "にさいして", "、", "いかの", "ごりようじょうけん", "を", "よく", "およみください", "。"],
            "soal": ["よく", "いかの", "とうしょっぴんぐさいと", "にさいして", "ごりようじょうけん", "およみください", "を", "の", "ごりよう", "、", "を"]
        },
        {
            "id": 6,
            "pola": "2. 〜に際して・〜にあたって",
            "kanji": " me! 新しく事業を始めるにあたって、 me! しっかり準備をしようと思っております。",
            "hiragana": "あたらしくじぎょうをはじめるにあたって、しっかりじゅんびをしようとおもっております。",
            "arti": "Dalam rangka memulai bisnis baru, kami berniat untuk mempersiapkannya dengan matang.",
            "kunci": ["あたらしく", "じぎょう", "を", "はじめる", "にあたって", "、", "しっかり", "じゅんび", "を", "しよう", "と", "おもっております", "。"],
            "soal": ["じぎょう", "じゅんび", "しっかり", "を", "あたって", "に", "はじめる", "あたらしく", "とおもっております", "しよう", "、", "を"]
        },
        {
            "id": 7,
            "pola": "2. 〜に際して・〜にあたって",
            "kanji": "お二人の門出にあたりまして、 me! お祝いのお言葉を申し上げます。",
            "hiragana": "おふたりのかどであたりまして、おいわいのおことばをもうしあげます。",
            "arti": "Menyambut lembaran baru bagi Anda berdua, saya ingin menyampaikan patah kata ucapan selamat.",
            "kunci": ["おふたりの", "かどで", "に", "あたりまして", "、", "おいわい", "の", "ことば", "を", "もうしあげます", "。"],
            "soal": ["おふたりの", "もうしあげます", "おいわい", "あたりまして", "かどで", "に", "ことば", "を", "、", "の"]
        },
        {
            "id": 8,
            "pola": "2. 〜に際して・〜にあたって",
            "kanji": "日本で開催する国際会議にあたり、 me! 関係各方面からの me! 協力を me! 得た。",
            "hiragana": "にほんでかいさいするこくさいかいぎにあたり、かんけいかくほうめんからのきょうりょくをおえた。",
            "arti": "Menjelang penyelenggaraan konferensi internasional di Jepang, kami mendapatkan kerja sama dari berbagai pihak terkait.",
            "kunci": ["にほん", "で", "かいさいする", "こくさいかいぎ", "に", "あたり", "、", "かんけいかくほうめん", "からの", "きょうりょく", "を", "えた", "。"],
            "soal": ["こくさいかいぎ", "にほん", "きょうりょくをえた", "あたり", "かいさいする", "で", "からの", "に", "かんけいかくほうめん", "を", "、", "えた"]
        },

        # --- POIN 3: 〜たとたん（に） ---
        {
            "id": 9,
            "pola": "3. 〜たとたん（に）",
            "kanji": "山の頂上でワインを一口飲んだ途端に、 me! めまいがした。",
            "hiragana": "やまのちょうじょうでわいんをひとくちのんだたとたんに、めまいがした。",
            "arti": "Begitu meminum seteguk anggur di puncak gunung, saya langsung merasa pusing.",
            "kunci": ["やま", "の", "ちょうじょう", "で", "わいん", "を", "ひとくち", "のんだ", "たとたんに", "、", "めまい", "が", "した", "。"],
            "soal": ["の", "やま", "めまい", "のんだ", "ちょうじょう", "ひとくち", "わいん", "で", "たとたんに", "が", "を", "した", "、"]
        },
        {
            "id": 10,
            "pola": "3. 〜たとたん（に）",
            "kanji": "結婚前は優しかった夫が、 me! 結婚した途端に me! 態度が変わった。",
            "hiragana": "けっこんまえはやさしかったおっとが、けっこんしたたとたんにたいどかわった。",
            "arti": "Suami yang sangat baik sebelum menikah, begitu setelah menikah sikapnya langsung berubah.",
            "kunci": ["けっこん", "まえ", "は", "やさしかった", "おっと", "が", "、", "けっこん", "した", "たとたん", "に", "たいど", "が", "かわった", "。"],
            "soal": ["おっと", "が", "かわった", "たいど", "やさしかった", "たとたん", "けっこん", "は", "が", "、", "に", "けっこん", "した", "まえ"]
        },
        {
            "id": 11,
            "pola": "3. 〜たとたん（に）",
            "kanji": "国の母に電話をかけた。 me! 母の声を聞いた途端に、 me! 涙があふれてきた。",
            "hiragana": "くにのははにでんわをかけた。ははのこえをきいたたとたんに、なみだがあふれてきた。",
            "arti": "Saya menelepon ibu di kampung halaman. Begitu mendengar suara ibu, air mata saya langsung menetes deras.",
            "kunci": ["くに", "の", "はは", "に", "でんわ", "を", "かけた", "。", "はは", "の", "こえ", "を", "きいた", "たとたん", "に", "、", "なみだ", "が", "あふれてきた", "。"],
            "soal": ["でんわ", "はは", "を", "かけた", "たとたん", "の", "あふれてきた", "なみだ", "に", "はは", "くに", "こえ", "きいた", "の", "が", "、", "を"]
        },
        {
            "id": 12,
            "pola": "3. 〜たとたん（に）",
            "kanji": " me! 「さよなら」と言った途端、 me! 彼女は走っていってしまった。",
            "hiragana": "「さよなら」といったたとたん、かのじょははしっていってしまった。",
            "arti": "Sesaat setelah saya mengucapkan 'selamat tinggal', dia langsung berlari pergi.",
            "kunci": ["ぼく", "が", "「 さよなら 」", "と", "いった", "たとたん", "、", "かのじょ", "は", "はしっていってしまった", "。"],
            "soal": ["はしって", "いった", "「 さよなら 」", "かのじょ", "たとたん", "ぼく", "は", "と", "が", "いってしまった", "、"]
        },

        # --- POIN 4: 〜（か）と思うと・〜（か）と思ったら ---
        {
            "id": 13,
            "pola": "4. 〜（か）と思うと・〜（か）と思ったら",
            "kanji": "林さんが部屋の窓を全部開けたかと思うと、 me! いきなり me! 入ってきた。",
            "hiragana": "はやしさんがへやのまどをぜんぶあけたかとおもうと、いきなりはいってきた。",
            "arti": "Baru saja Hayashi-san membuka semua jendela kamar, tiba-tiba dia langsung masuk.",
            "kunci": ["はやしさん", "が", "へや", "の", "まど", "を", "ぜんぶ", "あけた", "か", "とおもうと", "、", "いきなり", "はいってきた", "。"],
            "soal": ["はいってきた", "あけた", "まど", "はやしさん", "とおもうと", "へや", "いきなり", "は", "を", "に", "ぜんぶ", "、", "か"]
        },
        {
            "id": 14,
            "pola": "4. 〜（か）と思うと・〜（か）と思ったら",
            "kanji": "赤ちゃんは今笑っていると思ったら、 me! もう me! 泣いた。",
            "hiragana": "あかちゃんはいままわらっているとおもったら、もうないた。",
            "arti": "Bayi itu baru saja tertawa, tetapi seketika itu juga langsung menangis.",
            "kunci": ["あかちゃん", "は", "いま", "わらっている", "と", "おもったら", "、", "もう", "ないた", "。"],
            "soal": ["わらっている", "いま", "とおもったら", "もう", "あかちゃん", "ないた", "は", "、", "と"]
        },
        {
            "id": 15,
            "pola": "4. 〜（か）と思うと・〜（か）と思ったら",
            "kanji": "子供たちが散らかした部屋が me! やっと片付いたと思ったら、 me! また me! すぐ散らかした。",
            "hiragana": "こどもたちがちらかしたへやがやっとかたづいたとおもったら、またすぐちらかした。",
            "arti": "Kamar yang diacak-acak anak-anak baru saja selesai dibersihkan, eh langsung berantakan lagi.",
            "kunci": ["こどもたち", "が", "ちらかした", "へや", "が", "やっと", "かたづいた", "か", "とおもったら", "、", "また", "すぐ", "ちらかした", "。"],
            "soal": ["ちらかした", "へや", "やっと", "が", "こどもたち", "かたづいた", "とおもったら", "すぐ", "が", "また", "か", "、", "ちらかした"]
        },
        {
            "id": 16,
            "pola": "4. 〜（か）と思うと・〜（か）と思ったら",
            "kanji": "この頃は me! 気温の差が大きい。 me! 昨日は me! 涼しいかと思ったら、 me! 今日は me! 暑くなった。",
            "hiragana": "このごろはきおんのさがおおきい。きのうはすずしいかとおもったら、きょうはあつくなった。",
            "arti": "Akhir-akhir ini perbedaan suhunya lumayan ekstrem. Kemarin rasanya sejuk, eh hari ini malah jadi panas.",
            "kunci": ["このごろ", "は", "きおん", "の", "さ", "が", "おおきい", "。", "きのう", "は", "すずしい", "か", "とおもったら", "、", "きょう", "は", "あつくなった", "。"],
            "soal": ["きょう", "このごろ", "さ", "おおきい", "すずしい", "きおん", "あつくなった", "きのう", "が", "は", "は", "とおもったら", "か", "、", "。", "の"]
        },

        # --- POIN 5: 〜か〜ないかのうちに ---
        {
            "id": 17,
            "pola": "5. 〜か〜ないかのうちに",
            "kanji": "一郎は me! ベッドに me! 横になるか me! ならないかのうちに、 me! ぐっすり me! 眠ってしまった。",
            "hiragana": "いちろうはべっどによこになるかならないかのうちに、ぐっすりねむってしまった。",
            "arti": "Ichiro baru saja berbaring di tempat tidur, dia sudah tertidur nyenyak.",
            "kunci": ["いちろう", "は", "べっど", "に", "よこになる", "か", "ならないかのうちに", "、", "ぐっすり", "ねむってしまった", "。"],
            "soal": ["よこになる", "ねむってしまった", "いちろう", "べっど", "ないかのうちに", "は", "か", "ぐっすり", "に", "、", "ならないかのうちに"]
        },
        {
            "id": 18,
            "pola": "5. 〜か〜ないかのうちに",
            "kanji": "わたしは me! 夜が me! 明けるか me! 明けないかのうちに me! 家を出て、 me! 空港へ me! 向かった。",
            "hiragana": "わたしはよるがあけるかあけないかのうちにいえをでて、くうこうへむかった。",
            "arti": "Bahkan sebelum fajar menyingsing, saya sudah keluar rumah dan berangkat menuju bandara.",
            "kunci": ["わたし", "は", "よる", "が", "あける", "か", "あけない", "かのうちに", "、", "いえ", "を", "でて", "、", "くうこう", "へ", "むかった", "。"],
            "soal": ["むかった", "くうこう", "よる", "あけた", "わたし", "いえ", "でて", "ないかのうちに", "へ", "は", "か", "を", "あけない", "、", "が", "あける", "かのうちに"]
        },
        {
            "id": 19,
            "pola": "5. 〜か〜ないかのうちに",
            "kanji": "あの me! 売れっ子作家は me! 新しい作品を me! 発表したか me! 発表しないかのうちに、 me! もう me! 次の me! 話題作に me! 取りかかっているそうだ。",
            "hiragana": "あのうれっこさっかはあたらしいさくひんをはっぴょうしたからはっぴょうしないかのうちに、もうつぎのわだいさくにとりかかっているそうだ。",
            "arti": "Penulis populer itu kabarnya baru saja merilis karya barunya, tetapi langsung sibuk mengerjakan karya populer berikutnya.",
            "kunci": ["あの", "うれっこ", "さっか", "は", "あたらしい", "さくひん", "を", "はっぴょうした", "か", "はっぴょうしない", "かのうちに", "、", "もう", "つぎ", "の", "わだいさく", "に", "とりかかっている", "そうだ", "。"],
            "soal": ["あの", "いま", "とりかかっている", "わだいさく", "うれっこ", "さくひん", "だ", "はっぴょうした", "そうだ", "さっか", "つぎ", "に", "か", "もう", "は", "ないかのうちに", "し", "の", "を", "、", "あたらしい", "はっぴょうしない", "かのうちに"]
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
    st.session_state.bank_kata = [{"id": i, "teks": kata, "dipakai": False} for i, kata in enumerate(soal_sekarang["soal"])]

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
    
    user_joined = "".join(user_strings).replace(" ", "").replace("、", "").replace("。", "")
    kunci_joined = "".join(kunci_strings).replace(" ", "").replace("、", "").replace("。", "")
    
    if user_joined == kunci_joined:
        st.success(f"🎉 **正解 (Benar)!** Susunan bunpou kamu sudah sempurna!\n\n**🇯🇵 Kanji:** {soal_sekarang['kanji']}\n\n**💡 Hiragana:** {soal_sekarang['hiragana']}")
    else:
        st.error(f"❌ **残念 (Kurang Tepat).**\n\n**Susunan yang benar:**\n\n`{' '.join(kunci_strings)}`\n\n**🇯🇵 Kanji asli:** {soal_sekarang['kanji']}\n\n**💡 Hiragana:** {soal_sekarang['hiragana']}")
