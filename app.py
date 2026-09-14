import json
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Myra & Matthew learning Chinese",
    page_icon="🐰",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# แต่ละคำ: จีน | พินอิน | ไทย | ภาพสัญลักษณ์
CONTENT = [
    ("ทักทาย", "👋", """
你好|nǐ hǎo|สวัสดี|👋;再见|zài jiàn|ลาก่อน|👋;谢谢|xièxie|ขอบคุณ|🙏;不客气|bú kèqi|ไม่ต้องเกรงใจ|😊;对不起|duìbuqǐ|ขอโทษ|🙇;没关系|méi guānxi|ไม่เป็นไร|🤗;请|qǐng|เชิญ|🤲
"""),
    ("ครอบครัว", "🏡", """
爸爸|bàba|พ่อ|👨;妈妈|māma|แม่|👩;哥哥|gēge|พี่ชาย|👦;姐姐|jiějie|พี่สาว|👧;弟弟|dìdi|น้องชาย|👶;妹妹|mèimei|น้องสาว|👶;爷爷|yéye|ปู่|👴;奶奶|nǎinai|ย่า|👵;外公|wàigōng|ตา|👴;外婆|wàipó|ยาย|👵
"""),
    ("ตัวเลข", "🔢", """
一|yī|หนึ่ง|1️⃣;二|èr|สอง|2️⃣;三|sān|สาม|3️⃣;四|sì|สี่|4️⃣;五|wǔ|ห้า|5️⃣;六|liù|หก|6️⃣;七|qī|เจ็ด|7️⃣;八|bā|แปด|8️⃣;九|jiǔ|เก้า|9️⃣;十|shí|สิบ|🔟
"""),
    ("สีสัน", "🎨", """
红色|hóngsè|สีแดง|🔴;黄色|huángsè|สีเหลือง|🟡;蓝色|lánsè|สีน้ำเงิน|🔵;绿色|lǜsè|สีเขียว|🟢;白色|báisè|สีขาว|⚪;黑色|hēisè|สีดำ|⚫;粉色|fěnsè|สีชมพู|🩷;紫色|zǐsè|สีม่วง|🟣;橙色|chéngsè|สีส้ม|🟠
"""),
    ("ร่างกาย", "🖐️", """
头|tóu|ศีรษะ|🧒;头发|tóufa|ผม|👩;眼睛|yǎnjing|ตา|👀;耳朵|ěrduo|หู|👂;鼻子|bízi|จมูก|👃;嘴巴|zuǐba|ปาก|👄;手|shǒu|มือ|🖐️;脚|jiǎo|เท้า|🦶;肚子|dùzi|ท้อง|🧍
"""),
    ("สัตว์", "🐰", """
狗|gǒu|สุนัข|🐶;猫|māo|แมว|🐱;兔子|tùzi|กระต่าย|🐰;鸟|niǎo|นก|🐦;鱼|yú|ปลา|🐟;鸭子|yāzi|เป็ด|🦆;大象|dàxiàng|ช้าง|🐘;老虎|lǎohǔ|เสือ|🐯;狮子|shīzi|สิงโต|🦁;熊猫|xióngmāo|แพนด้า|🐼
"""),
    ("ผลไม้", "🍎", """
苹果|píngguǒ|แอปเปิล|🍎;香蕉|xiāngjiāo|กล้วย|🍌;西瓜|xīguā|แตงโม|🍉;橙子|chéngzi|ส้ม|🍊;葡萄|pútao|องุ่น|🍇;草莓|cǎoméi|สตรอว์เบอร์รี|🍓;芒果|mángguǒ|มะม่วง|🥭;菠萝|bōluó|สับปะรด|🍍
"""),
    ("อาหาร", "🍚", """
饭|fàn|ข้าว|🍚;面条|miàntiáo|บะหมี่|🍜;面包|miànbāo|ขนมปัง|🍞;鸡蛋|jīdàn|ไข่ไก่|🥚;牛奶|niúnǎi|นมวัว|🥛;水|shuǐ|น้ำ|💧;果汁|guǒzhī|น้ำผลไม้|🧃;糖果|tángguǒ|ลูกอม|🍬;蛋糕|dàngāo|เค้ก|🍰
"""),
    ("ของเล่น–ของใช้", "🧸", """
玩具|wánjù|ของเล่น|🧸;球|qiú|ลูกบอล|⚽;娃娃|wáwa|ตุ๊กตา|🪆;积木|jīmù|ตัวต่อ|🧱;书|shū|หนังสือ|📖;笔|bǐ|ปากกาหรือดินสอ|✏️;书包|shūbāo|กระเป๋านักเรียน|🎒;桌子|zhuōzi|โต๊ะ|🪑;椅子|yǐzi|เก้าอี้|🪑
"""),
    ("การกระทำ", "🏃", """
吃|chī|กิน|🍽️;喝|hē|ดื่ม|🥛;看|kàn|ดู|👀;听|tīng|ฟัง|👂;说|shuō|พูด|💬;走|zǒu|เดิน|🚶;跑|pǎo|วิ่ง|🏃;跳|tiào|กระโดด|🦘;坐|zuò|นั่ง|🧘;睡觉|shuìjiào|นอนหลับ|😴;玩|wán|เล่น|🧸
"""),
    ("ความรู้สึก", "😊", """
开心|kāixīn|มีความสุข|😄;难过|nánguò|เศร้า|😢;生气|shēngqì|โกรธ|😠;害怕|hàipà|กลัว|😨;累|lèi|เหนื่อย|😮‍💨;饿|è|หิว|🍽️;渴|kě|กระหายน้ำ|💧
"""),
    ("ธรรมชาติ", "🌷", """
太阳|tàiyáng|ดวงอาทิตย์|☀️;月亮|yuèliang|ดวงจันทร์|🌙;星星|xīngxing|ดาว|⭐;天空|tiānkōng|ท้องฟ้า|🌤️;云|yún|เมฆ|☁️;雨|yǔ|ฝน|🌧️;花|huā|ดอกไม้|🌷;树|shù|ต้นไม้|🌳
"""),
    ("โรงเรียน", "🏫", """
学校|xuéxiào|โรงเรียน|🏫;老师|lǎoshī|คุณครู|👩‍🏫;学生|xuésheng|นักเรียน|🧑‍🎓;朋友|péngyou|เพื่อน|🧒;教室|jiàoshì|ห้องเรียน|🏫;书包|shūbāo|กระเป๋านักเรียน|🎒;铅笔|qiānbǐ|ดินสอ|✏️;橡皮|xiàngpí|ยางลบ|▰;尺子|chǐzi|ไม้บรรทัด|📏;书|shū|หนังสือ|📖;画画|huà huà|วาดรูป|🎨;唱歌|chàng gē|ร้องเพลง|🎵;洗手|xǐ shǒu|ล้างมือ|🧼;上学|shàng xué|ไปโรงเรียน|🏫
"""),
    ("ประโยคสั้น", "💬", """
我爱妈妈。|Wǒ ài māma.|หนูรักแม่|💗;这是小猫。|Zhè shì xiǎo māo.|นี่คือแมวน้อย|🐱;我要喝水。|Wǒ yào hē shuǐ.|หนูอยากดื่มน้ำ|💧;我喜欢苹果。|Wǒ xǐhuan píngguǒ.|หนูชอบแอปเปิล|🍎;我很开心。|Wǒ hěn kāixīn.|หนูมีความสุข|😄;红色的球。|Hóngsè de qiú.|ลูกบอลสีแดง|🔴;谢谢妈妈！|Xièxie māma!|ขอบคุณแม่|🙏
"""),
]

categories = []

for name, icon, text in CONTENT:
    items = []

    for row in text.strip().split(";"):
        zh, pinyin, th, picture = row.strip().split("|")

        items.append({
            "zh": zh,
            "pinyin": pinyin,
            "th": th,
            "icon": picture,
        })

    categories.append({
        "name": name,
        "icon": icon,
        "items": items,
    })


# ตรึงพื้นที่แอปเท่าความสูงหน้าจอ
# ให้เลื่อนเฉพาะรายการคำศัพท์ด้านใน
st.markdown(
    """
    <style>
    [data-testid="stHeader"] {
        display: none;
    }

    [data-testid="stAppViewContainer"],
    [data-testid="stMain"] {
        overflow: hidden !important;
    }

    .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }

    iframe[title="streamlit.components.v1.html"] {
        width: 100% !important;
        height: 100dvh !important;
        border: 0;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


PAGE = r"""
<!doctype html>
<html lang="th">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">

<style>
* {
    box-sizing: border-box;
}

html, body {
    margin: 0;
    height: 100%;
    overflow: hidden;
}

body {
    font-family: Tahoma, Arial, sans-serif;
    color: #48525e;
    background: #fffdf8;
}

.app {
    height: 100vh;
    height: 100dvh;
    display: grid;
    grid-template-rows: auto minmax(0, 1fr);
}

header {
    padding: 12px 16px 8px;
    background: #fffdf8;
    border-bottom: 1px solid #e6e2ec;
}

.top {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 10px;
}

h1 {
    font-size: 18px;
    margin: 0;
    color: #8970a8;
    line-height: 1.4;
}

h1 small {
    display: block;
    font-size: 13px;
    color: #558772;
    font-weight: normal;
}

button, select {
    font: inherit;
    color: inherit;
}

button {
    cursor: pointer;
    touch-action: manipulation;
}

button:focus-visible,
select:focus-visible {
    outline: 3px solid #766198;
    outline-offset: 2px;
}

.stop {
    border: 0;
    border-radius: 12px;
    background: #ffe2d7;
    padding: 10px 14px;
    white-space: nowrap;
}

nav {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    padding-top: 10px;
}

nav button {
    border: 1px solid transparent;
    border-radius: 20px;
    padding: 8px 11px;
    font-size: 13px;
    background: #eee6f8;
    min-height: 36px;
}

nav button:nth-child(3n+2) {
    background: #e0f1e7;
}

nav button:nth-child(3n+3) {
    background: #ffe8db;
}

nav button[aria-pressed="true"] {
    border: 2px solid #796298;
    padding: 7px 10px;
    font-weight: bold;
}

details {
    font-size: 12px;
    margin-top: 8px;
    max-height: 32vh;
    overflow: auto;
}

summary {
    cursor: pointer;
    padding: 5px 0;
}

.settings {
    padding: 8px 0;
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    align-items: center;
}

select {
    max-width: 100%;
    padding: 8px;
    border: 1px solid #c9bbdc;
    border-radius: 10px;
    background: white;
}

#voiceSelect {
    width: min(100%, 420px);
}

#voiceNote {
    line-height: 1.6;
    margin: 4px 0;
}

#status {
    font-size: 12px;
    line-height: 1.5;
    margin: 6px 0 0;
    min-height: 18px;
}

main {
    overflow-y: auto;
    overscroll-behavior: contain;
    padding: 18px;
    min-height: 0;
}

.content {
    max-width: 960px;
    margin: 0 auto;
}

h2 {
    font-size: 21px;
    margin: 0 0 4px;
}

.hint {
    font-size: 13px;
    margin: 0 0 16px;
}

.cards {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 14px;
}

.card {
    border: 2px solid white;
    border-radius: 24px;
    padding: 20px 8px;
    background: #e9e0f7;
    min-width: 0;
    box-shadow: 0 4px 12px #00000007;
}

.card:nth-child(3n+2) {
    background: #ffe2d7;
}

.card:nth-child(3n+3) {
    background: #dff0ff;
}

.card.active {
    outline: 3px solid #65ad91;
    outline-offset: -3px;
}

.card:hover {
    filter: brightness(.98);
}

.card span {
    display: block;
    overflow-wrap: anywhere;
}

.picture {
    font-size: 58px;
    margin-bottom: 12px;
}

.zh {
    font-family: "Microsoft YaHei", "PingFang SC", sans-serif;
    font-size: 32px;
    line-height: 1.5;
}

.pinyin {
    font: 17px Arial, sans-serif;
    margin: 8px 0;
}

.th {
    font-size: 17px;
    line-height: 1.6;
}

.listen {
    font-size: 12px;
    margin-top: 10px;
    color: #586b60;
}

footer {
    text-align: center;
    padding: 24px 0 8px;
    font-size: 13px;
    color: #647969;
}

@media (max-width: 540px) {
    header {
        padding: 10px 10px 6px;
    }

    h1 {
        font-size: 16px;
    }

    nav {
        gap: 5px;
    }

    nav button {
        font-size: 12px;
        padding: 7px 9px;
    }

    nav button[aria-pressed="true"] {
        padding: 6px 8px;
    }

    main {
        padding: 14px 10px;
    }

    .cards {
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 10px;
    }

    .picture {
        font-size: 48px;
    }

    .zh {
        font-size: 27px;
    }

    .pinyin, .th {
        font-size: 15px;
    }
}
</style>
</head>

<body>
<div class="app">

<header>
    <div class="top">
        <h1>
            🐰 Myra &amp; Matthew
            <small>learning Chinese</small>
        </h1>

        <button class="stop" id="stop">
            ⏹ หยุดเสียง
        </button>
    </div>

    <nav id="nav" aria-label="หมวดคำศัพท์"></nav>

    <details id="settings">
        <summary>⚙️ ตั้งค่าเสียง</summary>

        <div class="settings">
            <label for="voiceSelect">เสียงจีน</label>
            <select id="voiceSelect"></select>

            <label for="speed">ความเร็ว</label>
            <select id="speed">
                <option value="0.65">ช้า</option>
                <option value="0.8" selected>ช้าปานกลาง</option>
                <option value="1">ปกติ</option>
            </select>

            <button class="stop" id="testVoice">
                ทดสอบเสียง
            </button>

            <button class="stop" id="refreshVoices">
                โหลดรายชื่อเสียงใหม่
            </button>
        </div>

        <p id="voiceNote"></p>
    </details>

    <p id="status" role="status" aria-live="polite">
        แตะภาพเพื่อฟังภาษาจีน
    </p>
</header>

<main id="scrollArea">
    <div class="content">
        <h2 id="heading"></h2>

        <p class="hint">
            แตะภาพเพื่อฟัง แล้วพูดภาษาจีนตามได้เลย
        </p>

        <div id="cards" class="cards"></div>

        <footer>
            🌷 เรียนวันละนิดกับกระต่ายน้อย 🌷
        </footer>
    </div>
</main>

</div>

<script>
const DATA = __DATA__;
const $ = id => document.getElementById(id);
const synth = window.speechSynthesis;

let voices = [];
let token = 0;
let utterance = null;
let activeCard = null;
let savedVoice = "";

try {
    savedVoice = localStorage.getItem("bunnyChineseVoice") || "";
} catch (e) {}


// เลือกเฉพาะเสียงจีนกลาง ไม่เลือกเสียงไทยหรือกวางตุ้ง
function isMandarin(voice) {
    const lang = voice.lang.replaceAll("_", "-").toLowerCase();

    return /^(zh$|zh-(cn|tw|sg|hans|hant)(-|$)|cmn)/.test(lang)
        && !/(hk|yue)/.test(lang);
}


// เสียงผู้หญิงที่รู้จัก ให้เลือกก่อนเสียงอื่น
function knownFemale(voice) {
    return /xiaoxiao|xiaoyi|huihui|yaoyao|ting[- ]?ting|mei[- ]?jia|li[- ]?li/i
        .test(voice.name);
}


function loadVoices() {
    const select = $("voiceSelect");
    const previous = select.value || savedVoice;

    select.replaceChildren(
        new Option("เลือกเสียงจีน…", "")
    );

    if (!synth) {
        $("voiceNote").textContent =
            "เบราว์เซอร์นี้ไม่รองรับเสียงอ่าน ลองเปิดด้วย Edge หรือ Chrome";
        return;
    }

    voices = synth.getVoices().filter(isMandarin);

    voices.sort(
        (a, b) => Number(knownFemale(b)) - Number(knownFemale(a))
    );

    for (const voice of voices) {
        select.add(
            new Option(
                voice.name + " · " + voice.lang,
                voice.voiceURI
            )
        );
    }

    const chosen =
        voices.find(v => v.voiceURI === previous)
        || voices.find(knownFemale);

    if (chosen) {
        select.value = chosen.voiceURI;
    }

    $("voiceNote").textContent = !voices.length
        ? "ยังไม่พบเสียงจีนกลาง ลองโหลดรายชื่อเสียงใหม่ หากยังไม่มี ให้เพิ่มเสียงจีนกลางในเครื่องแล้วเปิดเบราว์เซอร์ใหม่"
        : "เลือกเสียงผู้หญิง เช่น Xiaoxiao, Huihui หรือ Tingting แล้วกดทดสอบเสียง";
}


function stopSpeech() {
    token += 1;

    if (synth) {
        synth.cancel();
    }

    if (activeCard) {
        activeCard.classList.remove("active");
    }

    activeCard = null;
    utterance = null;
}


function speak(zh, card = null) {
    stopSpeech();

    if (!synth || !window.SpeechSynthesisUtterance) {
        $("status").textContent =
            "เบราว์เซอร์นี้ไม่รองรับเสียงอ่าน";
        $("settings").open = true;
        return;
    }

    loadVoices();

    const voice = voices.find(
        v => v.voiceURI === $("voiceSelect").value
    );

    if (!voice) {
        $("status").textContent =
            "กรุณาเลือกเสียงจีนในตั้งค่าเสียงก่อน แล้วแตะภาพอีกครั้ง";
        $("settings").open = true;
        return;
    }

    const current = token;

    // ส่งเฉพาะคำภาษาจีนไปอ่าน
    utterance = new SpeechSynthesisUtterance(zh);
    utterance.lang = voice.lang;
    utterance.voice = voice;
    utterance.rate = Number($("speed").value);
    utterance.pitch = 1;

    activeCard = card;

    if (card) {
        card.classList.add("active");
    }

    $("status").textContent = "🔊 " + zh;

    const finish = message => {
        if (current !== token) {
            return;
        }

        if (activeCard) {
            activeCard.classList.remove("active");
        }

        activeCard = null;
        utterance = null;
        $("status").textContent = message;
    };

    utterance.onend = () => {
        finish("⭐ เก่งมาก! แตะฟังซ้ำหรือเลือกคำต่อไป");
    };

    utterance.onerror = () => {
        finish(
            "เล่นเสียงไม่ได้ ลองเลือกเสียงจีนอื่นในตั้งค่าเสียงแล้วแตะอีกครั้ง"
        );
    };

    try {
        synth.speak(utterance);
    } catch (e) {
        finish("เปิดเสียงไม่ได้ กรุณาตรวจสอบตั้งค่าเสียง");
    }
}


function addText(parent, text, className, lang) {
    const span = document.createElement("span");

    span.textContent = text;
    span.className = className;

    if (lang) {
        span.lang = lang;
    }

    parent.appendChild(span);
}


function showCategory(index) {
    stopSpeech();

    const category = DATA[index];

    $("heading").textContent =
        category.icon + " " + category.name;

    $("status").textContent = "แตะภาพเพื่อฟังภาษาจีน";

    $("cards").replaceChildren();

    [...$("nav").children].forEach((button, i) => {
        button.setAttribute(
            "aria-pressed",
            String(i === index)
        );
    });

    category.items.forEach(word => {
        const button = document.createElement("button");

        button.className = "card";

        button.setAttribute(
            "aria-label",
            "ฟัง " + word.zh + " " + word.th
        );

        addText(button, word.icon, "picture");
        addText(button, word.zh, "zh", "zh-CN");
        addText(button, word.pinyin, "pinyin");
        addText(button, word.th, "th", "th");
        addText(button, "🔊 แตะเพื่อฟัง", "listen");

        button.onclick = () => {
            speak(word.zh, button);
        };

        $("cards").appendChild(button);
    });

    $("scrollArea").scrollTop = 0;
}


// สร้างปุ่ม navigation ขนาดเล็ก
DATA.forEach((category, index) => {
    const button = document.createElement("button");

    button.textContent =
        category.icon + " " + category.name;

    button.onclick = () => {
        showCategory(index);
    };

    $("nav").appendChild(button);
});


$("stop").onclick = () => {
    stopSpeech();
    $("status").textContent = "หยุดเสียงแล้ว";
};


$("voiceSelect").onchange = () => {
    stopSpeech();

    savedVoice = $("voiceSelect").value;

    try {
        localStorage.setItem(
            "bunnyChineseVoice",
            savedVoice
        );
    } catch (e) {}
};


$("testVoice").onclick = () => {
    speak("你好");
};


$("refreshVoices").onclick = loadVoices;


if (synth) {
    synth.addEventListener("voiceschanged", loadVoices);
}

window.addEventListener("pagehide", stopSpeech);

showCategory(0);
loadVoices();
</script>
</body>
</html>
"""

# ป้องกันข้อมูลถูกตีความเป็นแท็ก HTML ในสคริปต์
payload = json.dumps(
    categories,
    ensure_ascii=False,
).replace("<", "\\u003c")

components.html(
    PAGE.replace("__DATA__", payload),
    height=800,
    scrolling=False,
)
