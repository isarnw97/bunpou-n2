import streamlit as st

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
            "kunci": ["この", "たいいくかん", "で", "は", "すいえい", "を", "はじめ", "、", "いろいろな", "スポーツ", "が", "たのしめる", "。"],
            "soal": ["たのしめる", "すいえい", "いろいろな", "スポーツ", "はじめ", "この", "が", "を", "たいいくかん", "で", "は", "、", "。"]
        },
        {
            "id": 2,
            "pola": "1. ～をはじめ（として）",
            "kanji": "日本には「桃太郎」をはじめとして、おじいさん、おばあさんが出てくる昔話が多い。",
            "hiragana": "にほんには 「ももたろう」を はじめとして、 おじいさん、 おばあさんが でてくる むかしばなしが おおい。",
            "arti": "Di Jepang ada banyak cerita rakyat yang menampilkan kakek dan nenek, dimulai dari \"Momotaro\".",
            "kunci": ["にっぽん", "に", "は", "「ももたろう」", "を", "はじめとして", "、", "おじいさん", "、", "おばあさん", "が", "でてくる", "むかしばなし", "が", "おおい", "。"],
            "soal": ["おばあさん", "ももたろう", "に", "が", "でてくる", "は", "むかしばなし", "おじいさん", "にっぽん", "おおい", "を", "はじめとして", "が", "、", "、"]
        },
        {
            "id": 3,
            "pola": "1. ～をはじめ（として）",
            "kanji": "このあたりには、市役所をはじめとする市の公共の建物が多い。",
            "hiragana": "この あたりには、 しやくしょを はじめとする しの こうきょうの たてものが おおい。",
            "arti": "Di sekitar daerah ini, ada banyak bangunan publik kota, dimulai dari kantor balai kota.",
            "kunci": ["この", "あたり", "に", "は", "、", "しやくしょ", "を", "はじめとする", "しの", "こうきょう", "の", "たてもの", "が", "おおい", "。"],
            "soal": ["しの", "おおい", "はじめとする", "この", "あたり", "に", "しやくしょ", "を", "こうきょう", "の", "たてもの", "が", "は", "、"]
        },
        {
            "id": 4,
            "pola": "2. ～からして",
            "kanji": "この旅行の計画には無理がある。出発時間からして早すぎる。",
            "hiragana": "この りょこうの けいかくには むりが ある。 しゅっぱつじかん からして はやすぎる。",
            "arti": "Rencana perjalanan ini tidak masuk akal. Dari waktu keberangkatannya saja sudah terlalu pagi.",
            "kunci": ["この", "りょこう", "の", "けいかく", "に", "は", "むり", "が", "ある", "。", "しゅっぱつじかん", "からして", "はやすぎる", "。"],
            "soal": ["で", "は", "はやすぎる", "しゅっぱつじかん", "りょこう", "の", "からして", "むり", "の", "けいかく", "に", "この", "が", "ある"]
        },
        {
            "id": 5,
            "pola": "2. ～からして",
            "kanji": "わたしはどうも猫が苦手だ。あの光る目からして何となく怖い感じがする。",
            "hiragana": "わたしは どうも ねこが にがてだ。 あの ひかる めからして なんとなく こわい かんじが する。",
            "arti": "Saya sepertinya kurang suka kucing. Dari matanya yang bersinar saja entah kenapa terasa menakutkan.",
            "kunci": ["わたし", "は", "どうも", "ねこ", "が", "にがてだ", "。", "あの", "ひかる", "め", "からして", "なんとなく", "こわい", "かんじ", "が", "する", "。"],
            "soal": ["こわい", "ねこ", "からして", "にがてだ", "の", "かんじ", "わたし", "が", "どうも", "あかるい", "め", "が", "する"]
        },
        {
            "id": 6,
            "pola": "2. ～からして",
            "kanji": "わたしと夫とは似ているところが少ない。第一、食べ物の好みからして正反対だ。",
            "hiragana": "わたしと おっととは にている ところが すくない。 だいいち、 たべものの このみからして せいはんたいだ。",
            "arti": "Saya dan suami punya sedikit kemiripan. Pertama-tama, dari selera makanan saja sudah bertolak belakang.",
            "kunci": ["わたし", "と", "おっと", "と", "は", "にている", "ところ", "が", "すくない", "。", "だいいち", "、", "たべもの", "の", "このみ", "からして", "せいはんたいだ", "。"],
            "soal": ["と", "にた", "たべもの", "せいはんたいだ", "わたし", "ところ", "の", "おっと", "は", "が", "だ", "の", "すくない", "だいいち", "からして", "このみ", "、"]
        },
        {
            "id": 7,
            "pola": "2. ～からして",
            "kanji": "さすがプロの選手は走り方からしてわたしたちとは違う。",
            "hiragana": "さすが プロの せんしゅは はしりがた からして わたしたちとは ちがう。",
            "arti": "Seperti yang diharapkan dari atlet profesional, dari cara larinya saja sudah berbeda dari kita.",
            "kunci": ["さすが", "プロ", "の", "せんしゅ", "は", "はしりがた", "からして", "わたしたち", "と", "は", "ちがう", "。"],
            "soal": ["はしりがた", "さすが", "と", "ちがう", "プロ", "の", "は", "せんしゅ", "わたし・たち", "からして"]
        },
        {
            "id": 8,
            "pola": "3. ～にわたって",
            "kanji": "連休の最終日、高速道路は20キロにわたって渋滞が続いた。",
            "hiragana": "れんきゅうの さいしゅうび、 こうそくどうろは にじゅっキロに わたって じゅうたいが つづいた。",
            "arti": "Pada hari terakhir libur panjang, kemacetan berlanjut sepanjang 20 km di jalan tol.",
            "kunci": ["れんきゅう", "の", "さいしゅうび", "、", "こうそくどうろ", "は", "２０キロ", "に", "わたって", "じゅうたい", "が", "つづいた", "。"],
            "soal": ["じゅうたい", "に", "さいしゅうび", "こうそくどうろ", "れんきゅう", "２０キロ", "の", "わたって", "づづいた", "が", "は", "、"]
        },
        {
            "id": 9,
            "pola": "3. ～にわたって",
            "kanji": "彼はいろいろなジャンルにわたり、たくさんの本を読んでいる。",
            "hiragana": "かれは いろいろな ジャンルに わたり、 たくさんの ほんを よんでいる。",
            "arti": "Dia membaca banyak buku yang mencakup berbagai macam genre.",
            "kunci": ["かれ", "は", "いろいろな", "ジャンル", "に", "わたり", "、", "たくさん", "の", "ほん", "を", "よんでいる", "。"],
            "soal": ["かれ", "を", "に", "たくさん", "いろいろな", "ほん", "よんでいる", "ジャンル", "わたし", "の", "、"]
        },
        {
            "id": 10,
            "pola": "3. ～にわたって",
            "kanji": "3日間にわたる研究発表大会が、無事終了しました。",
            "hiragana": "みっかかんに わたる けんきゅう はっぴょう たいかいが、 ぶじ しゅうりょう しました。",
            "arti": "Konferensi presentasi penelitian yang berlangsung selama 3 hari telah selesai dengan lancar.",
            "kunci": ["さんにちかん", "に", "わたる", "けんきゅうひょうひょうたいかい", "が", "、", "むじ事", "かんりょうしました", "。"],
            "soal": ["かんりょうしました", "けんきゅうひょうひょうたいかい", "が", "さんにちかん", "むじ事", "に", "わたる", "、"]
        },
        {
            "id": 11,
            "pola": "4. ～を通じて/を通して",
            "kanji": "この町には四季を通じて観光客が訪れる。",
            "hiragana": "この まちには しきを つうじて かんこうきゃくが おとずれる。",
            "arti": "Wisatawan mengunjungi kota ini sepanjang empat musim.",
            "kunci": ["この", "まち", "に", "は", "しき", "を", "つうじて", "かんこうきゃく", "が", "おとずれる", "。"],
            "soal": ["かんこうきゃく", "この", "は", "しき", "に", "まち", "を", "おとずれる", "つうじて", "が", "、"]
        },
        {
            "id": 12,
            "pola": "4. ～を通じて/を通して",
            "kanji": "在職期間を通して皆様には大変お世話になりました。",
            "hiragana": "ざいしょく きかんを とおして みなさまには たいへん おせわに なりました。",
            "arti": "Selama masa jabatan saya, terima kasih banyak atas segala bantuan dari Anda sekalian.",
            "kunci": ["ざいしょくきかん", "を", "とおして", "みなさま", "に", "は", "たいへん", "お世話", "に", "なりました", "。"],
            "soal": ["みなさま", "ざいしょくきかん", "に", "お世話", "たいへん", "を", "に", "とおして", "は", "なりました", "、"]
        },
        {
            "id": 13,
            "pola": "4. ～を通じて/を通して",
            "kanji": "この10年間を通じ、彼はいつも新しいことに挑戦していた。",
            "hiragana": "この じゅうねんかんを つうじ、 かれは いつも あたらしい ことに ちょうせん していた。",
            "arti": "Sepanjang 10 tahun ini, dia selalu menantang hal-hal baru.",
            "kunci": ["この", "１０ねんかん", "を", "つうじ", "、", "かれ", "は", "いつも", "あたらしい", "こと", "に", "ちょうせん", "していた", "。"],
            "soal": ["ちょうせん", "いつも", "に", "は", "あたらしい", "かれ", "この", "１０ねんかん", "を", "つうじ", "していた", "こと", "、"]
        },
        {
            "id": 14,
            "pola": "4. ～を通じて/を通して",
            "kanji": "今日では、インターネットを通じて世界中の情報が手に入る。",
            "hiragana": "こんにちでは、 インターネットを つうじて せかいじゅうの じょうほうが てに はいる。",
            "arti": "Hari ini, informasi dari seluruh dunia dapat diperoleh melalui internet.",
            "kunci": ["にちにち", "で", "は", "、", "インターネット", "を", "つうじて", "せかいじゅう", "の", "じょうほう", "が", "てに", "はじる", "。"],
            "soal": ["てに", "つうじて", "じょうほう", "はじる", "にちにち", "が", "インターネット", "せかいじゅう", "を", "の", "では", "、"]
        },
        {
            "id": 15,
            "pola": "4. ～を通じて/を通して",
            "kanji": "わたしたちは、ボランティア活動を通していろいろな国の人たちと交流を深めている。",
            "hiragana": "わたしたちは、 ボランティア かつどうを とおして いろいろな くにの ひとたちと こうりゅうを ふかめている。",
            "arti": "Kami mempererat pertukaran budaya dengan orang-orang dari berbagai negara melalui kegiatan sukarela.",
            "kunci": ["わたしたち", "は", "、", "ボランティアかつどう", "を", "とおして", "いろいろな", "くに", "の", "ひと・たち", "と", "こうりゅう", "を", "ふかめている", "。"],
            "soal": ["わたしたち", "こうりゅう", "を", "ボランティアかつどう", "くに", "ふかめている", "いろいろな", "と", "の", "とおして", "ひと・たち", "は", "、"]
        },
        {
            "id": 16,
            "pola": "5. ～限り",
            "kanji": "環境を守るためにわたしもできる限りことをしたい。",
            "hiragana": "かんきょうを まもる ために わたしも できる かぎりの ことを したい。",
            "arti": "Saya ingin melakukan hal-hal semampu saya untuk melindungi環境 (lingkungan).",
            "kunci": ["かんきょう", "を", "まもる", "ため", "に", "わたし", "も", "できる", "かぎり", "の", "こと", "を", "したい", "。"],
            "soal": ["まもる", "こと", "かんきょう", "の", "を", "わたし", "できる", "かぎり", "も", "ため", "を", "に", "したい", "、"]
        },
        {
            "id": 17,
            "pola": "5. ～限り",
            "kanji": "君が知っている限りのことを全部わたしに話してほしい。",
            "hiragana": "きみが しっている かぎりの ことを ぜんぶ わたしに はなして ほしい。",
            "arti": "Saya ingin kamu menceritakan semua hal sebatas yang kamu ketahui kepada saya.",
            "kunci": ["きみ", "が", "しって・いる", "かぎり", "の", "こと", "を", "ぜんぶ", "わたし", "に", "はなし", "て", "ほしい", "。"],
            "soal": ["の", "かぎり", "ぜんぶ", "はなし", "きみ", "わたし", "こと", "ほしい", "が", "を", "に", "しって・いる", "て", "、"]
        },
        {
            "id": 18,
            "pola": "5. ～限り",
            "kanji": "あしたはいよいよ試合だ。力の限り頑張ろう。",
            "hiragana": "あしたは いよいよ しあいだ。 ちからの かぎり がんばろう。",
            "arti": "Besok akhirnya pertandingan. Mari berjuang sekuat tenaga.",
            "kunci": ["あした", "は", "いよいよ", "しあわせ", "だ", "。", "ちから", "の", "かぎり", "がんばろう", "。"],
            "soal": ["ちから", "あした", "だ", "しあわせ", "いよいよ", "は", "の", "かぎり", "がんばろう", "、"]
        },
        {
            "id": 19,
            "pola": "6. ～だけ",
            "kanji": "ここにあるダンボールを、車に積めるだけ積んで持って帰ってください。",
            "hiragana": "ここに ある ダンボールを、 くるまに つめるだけ つんで もって かえってください。",
            "arti": "Silakan muat kardus yang ada di sini sebanyak yang muat di mobil lalu bawa pulang.",
            "kunci": ["ここ", "に", "ある", "だんぼーる", "を", "、", "くるま", "に", "つめる", "だけ", "つんで", "もって", "かえってください", "。"],
            "soal": ["くろ", "つめる", "だんぼーる", "ここ", "に", "つんで", "もって", "ある", "かえってください", "だけ", "を", "くるま", "に", "、"]
        },
        {
            "id": 20,
            "pola": "6. ～だけ",
            "kanji": "父は働くだけ働いて、定年前に退職してしまった。",
            "hiragana": "ちちは はたらくだけ はたらいて、 ていねんまえに たいしょく して しまった。",
            "arti": "Ayah bekerja keras sebisanya, lalu pensiun sebelum usianya.",
            "kunci": ["ちち", "は", "はたらくだけ", "はたらいて", "、", "ていねんまえ", "に", "たいしょくして", "しまった", "。"],
            "soal": ["はたらくだけ", "ていねんまえ", "ちち", "はたらいて", "に", "しまった", "たいしょくして", "は", "、"]
        },
        {
            "id": 21,
            "pola": "6. ～だけ",
            "kanji": "今日は部長に言いたいだけの不満を全部言って、すっきりした。",
            "hiragana": "きょうは ぶちょうに いいたいだけ の ふまんを ぜんぶ いって、 すっきりした。",
            "arti": "Hari ini saya merasa lega setelah mengungkapkan semua ketidakpuasan sepuasnya kepada manajer.",
            "kunci": ["きょう", "は", "ぶちょう", "に", "いいたい", "だけ", "の", "ふまん", "を", "ぜんぶ", "いって", "、", "すっきりした", "。"],
            "soal": ["いいたい", "いって", "ぶちょう", "ふまん", "ぜんぶ", "きょう", "だけ", "の", "は", "に", "を", "すっきりした", "、"]
        },
        {
            "id": 22,
            "pola": "6. ～だけ",
            "kanji": "バイキング形式の食事ですから、好きなものを好きなだけ取ってお召し上がりください。",
            "hiragana": "バイキング けいしきの しょくじ ですから、 すきな ものを すきなだけ とって おめしあがり ください。",
            "arti": "Karena ini makanan prasmanan, silakan ambil dan nikmati apa yang Anda sukai sebanyak yang Anda suka.",
            "kunci": ["バイキングけいしき", "の", "しょくじ", "ですから", "、", "すきな", "もの", "を", "すきな", "だけ", "とって", "おめしあがり", "ください", "。"],
            "soal": ["おめしあがり", "バイキングけいしき", "すきな", "を", "すきな", "ですから", "ください", "だけ", "とって", "の", "しょくじ", "、"]
        }
    ]

# --- INISIALISASI INDEX SOAL ---
if "index_soal" not in st.session_state:
    st.session_state.index_soal = 0

# --- FITUR PILIH NOMOR SOAL (SIDEBAR) ---
st.sidebar.title("📌 Navigasi Soal")

# Membuat daftar pilihan: "Soal 1", "Soal 2", dst.
daftar_pilihan = [f"Soal {s['id']} ({s['pola']})" for s in st.session_state.database_soal]

# Selectbox untuk memilih nomor soal
pilihan_terpilih = st.sidebar.selectbox(
    "Pilih nomor soal yang diinginkan:",
    options=daftar_pilihan,
    index=st.session_state.index_soal
)

# Mengubah index_soal saat pengguna memilih dari dropdown
index_terpilih = daftar_pilihan.index(pilihan_terpilih)
if index_terpilih != st.session_state.index_soal:
    st.session_state.index_soal = index_terpilih
    st.rerun()

# --- AMBIL DATA SOAL AKTIF ---
soal_aktif = st.session_state.database_soal[st.session_state.index_soal]

st.title(f"📝 Latihan Soal Grammar N3 - Soal Nomor {soal_aktif['id']}")
st.write(f"**Pola Grammar:** {soal_aktif['pola']}")

# --- TAMPILAN SOAL ---
st.subheader("Kalimat Kanji:")
st.info(soal_aktif["kanji"])

st.subheader("Hiragana / Cara Baca:")
st.caption(soal_aktif["hiragana"])

st.subheader("Arti Bahasa Indonesia:")
st.write(soal_aktif["arti"])

# Tombol Tambahan Navigasi (Sebelum / Sesudah)
col1, col2 = st.columns(2)
with col1:
    if st.button("⬅️ Soal Sebelumnya") and st.session_state.index_soal > 0:
        st.session_state.index_soal -= 1
        st.rerun()

with col2:
    if st.button("Soal Selanjutnya ➡️") and st.session_state.index_soal < len(st.session_state.database_soal) - 1:
        st.session_state.index_soal += 1
        st.rerun()
