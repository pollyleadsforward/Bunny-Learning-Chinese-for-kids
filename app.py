import base64
import html
import json
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Bunny Chinese",
    page_icon="🐰",
    layout="centered",
    initial_sidebar_state="collapsed",
)

BASE_DIR = Path(__file__).resolve().parent
ASSET_DIR = BASE_DIR / "assets"


def image_to_data_uri(filename: str) -> str:
    path = ASSET_DIR / filename
    if not path.exists():
        return ""
    mime = "image/png" if path.suffix.lower() == ".png" else "image/jpeg"
    encoded = base64.b64encode(path.read_bytes()).decode("utf-8")
    return f"data:{mime};base64,{encoded}"


SECTIONS = [
    {
        "id": "morning",
        "emoji": "☀️",
        "title": "ตอนเช้า",
        "subtitle": "Morning routine",
        "tone": "cream",
        "items": [
            {"hanzi": "吃饭", "pinyin": "chī fàn", "thai": "กินข้าว", "image": "eat.png"},
            {"hanzi": "洗手", "pinyin": "xǐ shǒu", "thai": "ล้างมือ", "image": "wash.png"},
            {"hanzi": "刷牙", "pinyin": "shuā yá", "thai": "แปรงฟัน", "image": "brush.png"},
            {"hanzi": "洗澡", "pinyin": "xǐ zǎo", "thai": "อาบน้ำ", "image": "bath.png"},
        ],
    },
    {
        "id": "school",
        "emoji": "🏫",
        "title": "ไปโรงเรียน",
        "subtitle": "School time",
        "tone": "blue",
        "items": [
            {"hanzi": "去学校", "pinyin": "qù xuéxiào", "thai": "ไปโรงเรียน", "image": "school.png"},
            {"hanzi": "老师", "pinyin": "lǎoshī", "thai": "คุณครู", "image": "teacher.png"},
            {"hanzi": "见朋友", "pinyin": "jiàn péngyou", "thai": "เจอเพื่อน", "image": "friends.png"},
            {"hanzi": "你", "pinyin": "nǐ", "thai": "หนู / เธอ / คุณ", "image": "you.png"},
        ],
    },
    {
        "id": "travel",
        "emoji": "🚗",
        "title": "เดินทาง",
        "subtitle": "Getting around",
        "tone": "peach",
        "items": [
            {"hanzi": "坐车", "pinyin": "zuò chē", "thai": "นั่งรถ", "image": "ridecar.png"},
            {
                "hanzi": "妈妈送你去学校",
                "pinyin": "māma sòng nǐ qù xuéxiào",
                "thai": "คุณแม่ไปส่งหนูที่โรงเรียน",
                "image": "momcar.png",
                "wide": True,
            },
            {
                "hanzi": "爸爸送你去学校",
                "pinyin": "bàba sòng nǐ qù xuéxiào",
                "thai": "คุณพ่อไปส่งหนูที่โรงเรียน",
                "image": "dadcar.png",
                "wide": True,
            },
            {
                "hanzi": "外公去学校接你",
                "pinyin": "wàigōng qù xuéxiào jiē nǐ",
                "thai": "คุณตาไปรับหนูที่โรงเรียน",
                "image": "grandpa.png",
                "wide": True,
            },
        ],
    },
    {
        "id": "home",
        "emoji": "🌙",
        "title": "กลับบ้านและก่อนนอน",
        "subtitle": "Home & bedtime",
        "tone": "sage",
        "items": [
            {"hanzi": "上楼", "pinyin": "shàng lóu", "thai": "ขึ้นข้างบน / ขึ้นชั้นบน", "image": "upstairs.png"},
            {"hanzi": "睡觉", "pinyin": "shuì jiào", "thai": "เข้านอน / นอน", "image": "sleep.png"},
            {"hanzi": "关窗户", "pinyin": "guān chuānghu", "thai": "ปิดหน้าต่าง", "image": "window.png"},
        ],
    },
]


def make_card(item: dict) -> str:
    hanzi = html.escape(item["hanzi"])
    pinyin = html.escape(item["pinyin"])
    thai = html.escape(item["thai"])
    img_uri = image_to_data_uri(item["image"])
    wide_class = " wide" if item.get("wide") else ""
    js_text = json.dumps(item["hanzi"], ensure_ascii=False)

    if img_uri:
        picture = f'<img class="card-image" src="{img_uri}" alt="{hanzi}">'
    else:
        picture = '<div class="fallback-bunny">🐰</div>'

    return f"""
    <article class="word-card{wide_class}">
        <div class="art-wrap">
            {picture}
        </div>
        <button
            class="hanzi-button"
            onclick='speakChinese({js_text}, this)'
            aria-label="ฟังเสียง {hanzi}"
        >{hanzi}</button>
        <div class="pinyin">{pinyin}</div>
        <div class="thai">{thai}</div>
    </article>
    """


section_html = []
for section in SECTIONS:
    cards = "".join(make_card(item) for item in section["items"])
    section_html.append(
        f"""
        <section class="lesson-section {section["tone"]}" id="{section["id"]}">
            <div class="section-title-row">
                <div class="section-icon">{section["emoji"]}</div>
                <div>
                    <h2>{html.escape(section["title"])}</h2>
                    <p>{html.escape(section["subtitle"])}</p>
                </div>
            </div>
            <div class="card-grid">
                {cards}
            </div>
        </section>
        """
    )

hero_uri = image_to_data_uri("hero.png")

app_html = f"""
<!doctype html>
<html lang="th">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<style>
    :root {{
        color-scheme: light;
        --ink: #5b4542;
        --muted: #8d7d78;
        --pink: #f7cbd7;
        --pink-strong: #e98cab;
        --cream: #fff8ee;
        --peach: #fff0e6;
        --sage: #edf5ee;
        --blue: #eef6fb;
        --lav: #f2eff9;
        --line: rgba(141, 113, 105, 0.15);
        --shadow: 0 10px 28px rgba(113, 86, 78, 0.10);
    }}

    * {{
        box-sizing: border-box;
        -webkit-tap-highlight-color: transparent;
    }}

    html, body {{
        margin: 0;
        padding: 0;
        background: #fffaf6;
        color: var(--ink);
        font-family:
            "Noto Sans Thai", "Noto Sans SC", "PingFang SC",
            "Microsoft YaHei", system-ui, -apple-system, sans-serif;
        overflow-x: hidden;
    }}

    body {{
        width: 100%;
    }}

    button {{
        font: inherit;
    }}

    .phone {{
        width: 100%;
        max-width: 430px;
        margin: 0 auto;
        min-height: 100vh;
        padding: 10px 10px 30px;
        background:
            radial-gradient(circle at 12% 3%, rgba(247,203,215,.38), transparent 23%),
            radial-gradient(circle at 92% 7%, rgba(205,226,210,.42), transparent 22%),
            #fffaf6;
    }}

    .hero {{
        position: relative;
        overflow: hidden;
        border-radius: 28px;
        padding: 16px 16px 14px;
        background: linear-gradient(135deg, #fff7ef 0%, #fffafb 50%, #f1f7f0 100%);
        border: 1px solid rgba(222,190,179,.55);
        box-shadow: var(--shadow);
    }}

    .hero-top {{
        display: flex;
        align-items: center;
        gap: 12px;
    }}

    .hero img {{
        width: 88px;
        height: 82px;
        object-fit: cover;
        border-radius: 22px;
        border: 2px solid rgba(255,255,255,.9);
        box-shadow: 0 7px 20px rgba(112,86,80,.10);
        flex: 0 0 auto;
    }}

    .hero h1 {{
        margin: 0;
        font-family: Georgia, "Times New Roman", serif;
        font-size: 31px;
        line-height: 1.02;
        letter-spacing: -.4px;
        color: #5a3f3d;
    }}

    .hero .sub {{
        margin: 5px 0 0;
        color: #7f706b;
        font-size: 13.5px;
        line-height: 1.45;
    }}

    .tap-note {{
        margin-top: 13px;
        border-radius: 18px;
        padding: 11px 12px;
        text-align: center;
        background: linear-gradient(90deg, #fde4ec, #fff5f7);
        color: #9b5870;
        font-size: 13px;
        font-weight: 700;
        border: 1px solid rgba(233,140,171,.22);
    }}

    .chips {{
        display: flex;
        gap: 8px;
        overflow-x: auto;
        padding: 12px 1px 4px;
        scrollbar-width: none;
    }}

    .chips::-webkit-scrollbar {{
        display: none;
    }}

    .chip {{
        flex: 0 0 auto;
        text-decoration: none;
        color: #6f5c58;
        background: #fff;
        border: 1px solid rgba(180,150,141,.18);
        box-shadow: 0 4px 14px rgba(98,74,67,.07);
        padding: 8px 12px;
        border-radius: 999px;
        font-size: 12px;
        font-weight: 800;
    }}

    .lesson-section {{
        margin-top: 12px;
        border-radius: 27px;
        padding: 13px 11px 14px;
        border: 1px solid var(--line);
        box-shadow: var(--shadow);
    }}

    .lesson-section.cream {{ background: linear-gradient(180deg,#fff9ef,#fffdf9); }}
    .lesson-section.blue  {{ background: linear-gradient(180deg,#eef8fb,#fbfdff); }}
    .lesson-section.peach {{ background: linear-gradient(180deg,#fff1e7,#fffaf7); }}
    .lesson-section.sage  {{ background: linear-gradient(180deg,#eef6ef,#fbfdf9); }}

    .section-title-row {{
        display: flex;
        align-items: center;
        gap: 10px;
        padding: 1px 3px 10px;
    }}

    .section-icon {{
        width: 42px;
        height: 42px;
        display: grid;
        place-items: center;
        border-radius: 15px;
        background: rgba(255,255,255,.74);
        border: 1px solid rgba(255,255,255,.85);
        font-size: 23px;
        box-shadow: 0 5px 16px rgba(104,82,75,.08);
    }}

    .section-title-row h2 {{
        margin: 0;
        font-size: 20px;
        line-height: 1.05;
        color: #604946;
    }}

    .section-title-row p {{
        margin: 3px 0 0;
        font-size: 11.5px;
        color: #95827d;
    }}

    .card-grid {{
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 9px;
    }}

    .word-card {{
        min-width: 0;
        overflow: hidden;
        border-radius: 22px;
        background: rgba(255,255,255,.90);
        border: 1px solid rgba(183,151,143,.16);
        box-shadow: 0 7px 18px rgba(98,77,71,.07);
        padding: 7px 7px 11px;
        text-align: center;
    }}

    .word-card.wide {{
        grid-column: 1 / -1;
        display: grid;
        grid-template-columns: 41% 59%;
        grid-template-areas:
            "art hanzi"
            "art pinyin"
            "art thai";
        align-items: center;
        gap: 0 8px;
        padding: 8px;
        text-align: left;
    }}

    .art-wrap {{
        width: 100%;
        border-radius: 17px;
        overflow: hidden;
        background: #fff6ef;
    }}

    .word-card.wide .art-wrap {{
        grid-area: art;
        height: 130px;
    }}

    .card-image {{
        display: block;
        width: 100%;
        height: 118px;
        object-fit: cover;
    }}

    .wide .card-image {{
        height: 130px;
    }}

    .fallback-bunny {{
        height: 118px;
        display: grid;
        place-items: center;
        font-size: 56px;
        background: linear-gradient(135deg,#fff1e8,#edf6ef);
    }}

    .hanzi-button {{
        appearance: none;
        -webkit-appearance: none;
        width: 100%;
        margin: 7px 0 0;
        padding: 7px 5px 6px;
        border: 1.5px solid rgba(229,134,166,.36);
        border-radius: 15px;
        background: linear-gradient(180deg,#fff9fb,#fdebf1);
        color: #5c403f;
        font-family:
            "Noto Sans SC","PingFang SC","Microsoft YaHei",
            system-ui, sans-serif;
        font-size: 27px;
        font-weight: 800;
        line-height: 1.18;
        cursor: pointer;
        box-shadow:
            0 4px 12px rgba(216,125,155,.09),
            inset 0 0 0 1px rgba(255,255,255,.8);
        transition: transform .08s ease, box-shadow .12s ease, background .12s ease;
        outline: none;
    }}

    .hanzi-button:active,
    .hanzi-button.playing {{
        transform: scale(.97);
        background: linear-gradient(180deg,#fde4ec,#f9d7e3);
        box-shadow: 0 2px 8px rgba(210,120,152,.14);
        color: #6a4149;
    }}

    .hanzi-button:focus-visible {{
        outline: 3px solid rgba(235,145,176,.25);
        outline-offset: 2px;
    }}

    .wide .hanzi-button {{
        grid-area: hanzi;
        margin: 0;
        text-align: center;
        font-size: 23px;
        padding: 10px 8px;
    }}

    .pinyin {{
        margin-top: 4px;
        font-size: 13px;
        color: #7a6e79;
        line-height: 1.25;
    }}

    .thai {{
        margin-top: 3px;
        font-size: 12.5px;
        color: #8a7772;
        line-height: 1.3;
    }}

    .wide .pinyin {{
        grid-area: pinyin;
        text-align: center;
        font-size: 12.5px;
        padding: 3px 4px 0;
        margin-top: 0;
    }}

    .wide .thai {{
        grid-area: thai;
        text-align: center;
        font-size: 12px;
        padding: 3px 4px 0;
        margin-top: 0;
    }}

    .parent-tip {{
        margin-top: 13px;
        border-radius: 24px;
        padding: 15px 15px 14px;
        background: linear-gradient(135deg,#f5eff8,#fff8f2);
        border: 1px solid rgba(170,145,182,.16);
        box-shadow: var(--shadow);
    }}

    .parent-tip h3 {{
        margin: 0 0 8px;
        font-size: 16px;
        color: #67535f;
    }}

    .parent-tip p {{
        margin: 0;
        font-size: 12.5px;
        line-height: 1.55;
        color: #84757b;
    }}

    .footer {{
        padding: 18px 8px 8px;
        text-align: center;
        color: #a07985;
        font-family: Georgia, "Times New Roman", serif;
        font-style: italic;
        font-size: 14px;
    }}

    @media (max-width: 360px) {{
        .phone {{ padding-left: 7px; padding-right: 7px; }}
        .hero h1 {{ font-size: 27px; }}
        .hanzi-button {{ font-size: 24px; }}
        .wide .hanzi-button {{ font-size: 20px; }}
        .card-grid {{ gap: 7px; }}
    }}
</style>
</head>
<body>
<main class="phone">
    <header class="hero">
        <div class="hero-top">
            <img src="{hero_uri}" alt="กระต่ายน้อยอ่านหนังสือ">
            <div>
                <h1>Bunny Chinese</h1>
                <div class="sub">ภาษาจีนในชีวิตประจำวัน<br>สำหรับเด็ก 2–5 ขวบ</div>
            </div>
        </div>
        <div class="tap-note">👆 แตะที่ “ตัวอักษรจีน” เพื่อฟังเสียง — ไม่มีปุ่มลำโพง</div>
    </header>

    <nav class="chips" aria-label="หมวดบทเรียน">
        <a class="chip" href="#morning">☀️ ตอนเช้า</a>
        <a class="chip" href="#school">🏫 โรงเรียน</a>
        <a class="chip" href="#travel">🚗 เดินทาง</a>
        <a class="chip" href="#home">🌙 ก่อนนอน</a>
    </nav>

    {''.join(section_html)}

    <aside class="parent-tip">
        <h3>🌷 วิธีใช้กับเด็กเล็ก</h3>
        <p>
            รอบแรกให้เด็กดูภาพและแตะคำจีนเพื่อฟังเสียง 1–2 ครั้ง
            จากนั้นผู้ปกครองพูดซ้ำในสถานการณ์จริง เช่น ก่อนล้างมือให้แตะ
            “洗手” แล้วพาไปล้างมือทันที เด็กวัยนี้จะจำคำได้ง่ายขึ้นเมื่อ
            “เสียง + ภาพ + เหตุการณ์จริง” เกิดพร้อมกัน
        </p>
    </aside>

    <div class="footer">Little words • happy routines • growing together 🐰</div>
</main>

<script>
    let chineseVoices = [];

    function loadVoices() {{
        chineseVoices = window.speechSynthesis
            .getVoices()
            .filter(v => (v.lang || "").toLowerCase().startsWith("zh"));
    }}

    loadVoices();
    if ("speechSynthesis" in window) {{
        window.speechSynthesis.onvoiceschanged = loadVoices;
    }}

    function speakChinese(text, element) {{
        if (!("speechSynthesis" in window)) {{
            return;
        }}

        window.speechSynthesis.cancel();

        const utterance = new SpeechSynthesisUtterance(text);
        utterance.lang = "zh-CN";
        utterance.rate = 0.72;
        utterance.pitch = 1.05;
        utterance.volume = 1.0;

        const preferred =
            chineseVoices.find(v => (v.lang || "").toLowerCase() === "zh-cn") ||
            chineseVoices.find(v => (v.lang || "").toLowerCase() === "zh-tw") ||
            chineseVoices[0];

        if (preferred) {{
            utterance.voice = preferred;
        }}

        document.querySelectorAll(".hanzi-button.playing")
            .forEach(el => el.classList.remove("playing"));

        element.classList.add("playing");

        utterance.onend = () => element.classList.remove("playing");
        utterance.onerror = () => element.classList.remove("playing");

        window.speechSynthesis.speak(utterance);
    }}

    function reportHeight() {{
        const height = Math.ceil(document.documentElement.scrollHeight);
        window.parent.postMessage({{
            isStreamlitMessage: true,
            type: "streamlit:setFrameHeight",
            height: height
        }}, "*");
    }}

    window.addEventListener("load", () => {{
        setTimeout(reportHeight, 80);
        setTimeout(reportHeight, 400);
        setTimeout(reportHeight, 1000);
    }});

    new ResizeObserver(reportHeight).observe(document.body);
</script>
</body>
</html>
"""

st.markdown(
    """
    <style>
        html, body, [data-testid="stAppViewContainer"], .stApp {
            background: #fffaf6 !important;
        }

        [data-testid="stHeader"],
        [data-testid="stToolbar"],
        #MainMenu,
        footer {
            display: none !important;
        }

        .block-container {
            width: 100% !important;
            max-width: 430px !important;
            padding: 0 !important;
            margin: 0 auto !important;
        }

        iframe {
            border: 0 !important;
            width: 100% !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

components.html(app_html, height=3600, scrolling=False)
