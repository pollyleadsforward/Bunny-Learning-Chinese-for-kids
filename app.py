import json

import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    page_title="Myra & Matthew learning Chinese",
    page_icon="🐰",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# Chinese | Pinyin | English | Picture
CONTENT = [
    (
        "Greetings",
        "👋",
        """
你好|nǐ hǎo|Hello|👋
再见|zài jiàn|Goodbye|👋
谢谢|xièxie|Thank you|🙏
不客气|bú kèqi|You're welcome|😊
对不起|duìbuqǐ|Sorry|🙇
没关系|méi guānxi|That's okay|🤗
请|qǐng|Please|🤲
        """,
    ),
    (
        "Family",
        "🏡",
        """
爸爸|bàba|Dad|👨
妈妈|māma|Mom|👩
哥哥|gēge|Big brother|👦
姐姐|jiějie|Big sister|👧
弟弟|dìdi|Little brother|👶
妹妹|mèimei|Little sister|👶
爷爷|yéye|Grandpa (Dad's dad)|👴
奶奶|nǎinai|Grandma (Dad's mom)|👵
外公|wàigōng|Grandpa (Mom's dad)|👴
外婆|wàipó|Grandma (Mom's mom)|👵
        """,
    ),
    (
        "Numbers",
        "🔢",
        """
一|yī|One|1️⃣
二|èr|Two|2️⃣
三|sān|Three|3️⃣
四|sì|Four|4️⃣
五|wǔ|Five|5️⃣
六|liù|Six|6️⃣
七|qī|Seven|7️⃣
八|bā|Eight|8️⃣
九|jiǔ|Nine|9️⃣
十|shí|Ten|🔟
        """,
    ),
    (
        "Colors",
        "🎨",
        """
红色|hóngsè|Red|🔴
黄色|huángsè|Yellow|🟡
蓝色|lánsè|Blue|🔵
绿色|lǜsè|Green|🟢
白色|báisè|White|⚪
黑色|hēisè|Black|⚫
粉色|fěnsè|Pink|🩷
紫色|zǐsè|Purple|🟣
橙色|chéngsè|Orange|🟠
        """,
    ),
    (
        "Body Parts",
        "🖐️",
        """
头|tóu|Head|🧒
头发|tóufa|Hair|👩
眼睛|yǎnjing|Eyes|👀
耳朵|ěrduo|Ears|👂
鼻子|bízi|Nose|👃
嘴巴|zuǐba|Mouth|👄
手|shǒu|Hand|🖐️
脚|jiǎo|Foot|🦶
肚子|dùzi|Tummy|🧍
        """,
    ),
    (
        "Animals",
        "🐰",
        """
狗|gǒu|Dog|🐶
猫|māo|Cat|🐱
兔子|tùzi|Rabbit|🐰
鸟|niǎo|Bird|🐦
鱼|yú|Fish|🐟
鸭子|yāzi|Duck|🦆
大象|dàxiàng|Elephant|🐘
老虎|lǎohǔ|Tiger|🐯
狮子|shīzi|Lion|🦁
熊猫|xióngmāo|Panda|🐼
        """,
    ),
    (
        "Fruits",
        "🍎",
        """
苹果|píngguǒ|Apple|🍎
香蕉|xiāngjiāo|Banana|🍌
西瓜|xīguā|Watermelon|🍉
橙子|chéngzi|Orange|🍊
葡萄|pútao|Grapes|🍇
草莓|cǎoméi|Strawberry|🍓
芒果|mángguǒ|Mango|🥭
菠萝|bōluó|Pineapple|🍍
        """,
    ),
    (
        "Food & Drinks",
        "🍚",
        """
饭|fàn|Rice|🍚
面条|miàntiáo|Noodles|🍜
面包|miànbāo|Bread|🍞
鸡蛋|jīdàn|Egg|🥚
牛奶|niúnǎi|Milk|🥛
水|shuǐ|Water|💧
果汁|guǒzhī|Juice|🧃
糖果|tángguǒ|Candy|🍬
蛋糕|dàngāo|Cake|🍰
        """,
    ),
    (
        "Toys & Things",
        "🧸",
        """
玩具|wánjù|Toys|🧸
球|qiú|Ball|⚽
娃娃|wáwa|Doll|🪆
积木|jīmù|Building blocks|🧱
书|shū|Book|📖
笔|bǐ|Pen or pencil|✏️
书包|shūbāo|School bag|🎒
桌子|zhuōzi|Table|🪑
椅子|yǐzi|Chair|🪑
        """,
    ),
    (
        "Actions",
        "🏃",
        """
吃|chī|Eat|🍽️
喝|hē|Drink|🥛
看|kàn|Look|👀
听|tīng|Listen|👂
说|shuō|Speak|💬
走|zǒu|Walk|🚶
跑|pǎo|Run|🏃
跳|tiào|Jump|🦘
坐|zuò|Sit|🧘
睡觉|shuìjiào|Sleep|😴
玩|wán|Play|🧸
        """,
    ),
    (
        "Feelings",
        "😊",
        """
开心|kāixīn|Happy|😄
难过|nánguò|Sad|😢
生气|shēngqì|Angry|😠
害怕|hàipà|Scared|😨
累|lèi|Tired|😮‍💨
饿|è|Hungry|🍽️
渴|kě|Thirsty|💧
        """,
    ),
    (
        "Nature",
        "🌷",
        """
太阳|tàiyáng|Sun|☀️
月亮|yuèliang|Moon|🌙
星星|xīngxing|Star|⭐
天空|tiānkōng|Sky|🌤️
云|yún|Cloud|☁️
雨|yǔ|Rain|🌧️
花|huā|Flower|🌷
树|shù|Tree|🌳
        """,
    ),
    (
        "School",
        "🏫",
        """
学校|xuéxiào|School|🏫
老师|lǎoshī|Teacher|👩‍🏫
学生|xuésheng|Student|🧑‍🎓
朋友|péngyou|Friend|🧒
教室|jiàoshì|Classroom|🏫
书包|shūbāo|School bag|🎒
铅笔|qiānbǐ|Pencil|✏️
橡皮|xiàngpí|Eraser|▰
尺子|chǐzi|Ruler|📏
书|shū|Book|📖
画画|huà huà|Draw|🎨
唱歌|chàng gē|Sing|🎵
洗手|xǐ shǒu|Wash hands|🧼
上学|shàng xué|Go to school|🏫
        """,
    ),
    (
        "Short Sentences",
        "💬",
        """
我爱妈妈。|Wǒ ài māma.|I love Mom.|💗
这是小猫。|Zhè shì xiǎo māo.|This is a little cat.|🐱
我要喝水。|Wǒ yào hē shuǐ.|I want to drink water.|💧
我喜欢苹果。|Wǒ xǐhuan píngguǒ.|I like apples.|🍎
我很开心。|Wǒ hěn kāixīn.|I am happy.|😄
红色的球。|Hóngsè de qiú.|A red ball.|🔴
谢谢妈妈！|Xièxie māma!|Thank you, Mom!|🙏
        """,
    ),
]


categories = []

for name, icon, text in CONTENT:
    items = []

    for row in text.strip().splitlines():
        if not row.strip():
            continue

        chinese, pinyin, english, picture = row.strip().split("|")

        items.append({
            "zh": chinese,
            "pinyin": pinyin,
            "en": english,
            "icon": picture,
        })

    categories.append({
        "name": name,
        "icon": icon,
        "items": items,
    })


# Make the embedded app fill the screen on phones and tablets.
st.markdown(
    """
    <style>
    [data-testid="stHeader"] {
        display: none;
    }

    [data-testid="stAppViewContainer"],
    [data-testid="stMain"] {
        height: 100dvh !important;
        min-height: 100dvh !important;
        overflow: hidden !important;
        background: #fffdf8 !important;
    }

    .block-container {
        height: 100dvh !important;
        padding: 0 !important;
        max-width: 100% !important;
    }

    .element-container:has(
        iframe[title="streamlit.components.v1.html"]
    ) {
        height: 100dvh !important;
    }

    iframe[title="streamlit.components.v1.html"] {
        display: block;
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
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">

<style>
* {
    box-sizing: border-box;
}

html,
body {
    margin: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
}}

body {
    font-family: Arial, sans-serif;
    color: #48525e;
    background: #fffdf8;
}

/* One scrolling area for navigation, settings, and vocabulary. */
.app {
    width: 100%;
    height: 100vh;
    height: 100dvh;
    overflow-x: hidden;
    overflow-y: auto;
    overscroll-behavior: contain;
    position: relative;
    isolation: isolate;
    scroll-padding-top: 120px;
    -webkit-overflow-scrolling: touch;
}

/* Only this small title bar stays visible. */
.top {
    position: sticky;
    top: 0;
    z-index: 20;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 10px;
    min-height: 56px;
    padding: 8px 12px;
    background: #fffdf8;
    border-bottom: 1px solid #e6e2ec;
    box-shadow: 0 2px 6px #00000005;
}

h1 {
    font-size: 15px;
    margin: 0;
    color: #8970a8;
    line-height: 1.3;
}

h1 small {
    display: block;
    font-size: 11px;
    margin-top: 2px;
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
select:focus-visible,
summary:focus-visible {
    outline: 3px solid #766198;
    outline-offset: 2px;
}

.small-button {
    border: 0;
    border-radius: 12px;
    background: #ffe2d7;
    padding: 8px 10px;
    min-height: 36px;
    font-size: 12px;
    white-space: nowrap;
}

/* Category buttons stay in one horizontally scrollable row. */
nav {
    display: flex;
    flex-wrap: nowrap;
    gap: 6px;
    margin: 0;
    padding: 10px 12px;
    overflow-x: auto;
    overflow-y: hidden;
    -webkit-overflow-scrolling: touch;
    scrollbar-width: thin;
}

nav button {
    flex: 0 0 auto;
    white-space: nowrap;
    border: 1px solid transparent;
    border-radius: 20px;
    padding: 7px 10px;
    min-height: 36px;
    font-size: 12px;
    background: #eee6f8;
}

nav button:nth-child(3n+2) {
    background: #e0f1e7;
}

nav button:nth-child(3n+3) {
    background: #ffe8db;
}

nav button[aria-pressed="true"] {
    border: 2px solid #796298;
    padding: 6px 9px;
    font-weight: bold;
}

.nav-hint {
    margin: 0;
    padding: 0 12px 5px;
    font-size: 11px;
    color: #728078;
}

/* Settings are part of the page, not a fixed panel. */
details {
    margin: 0;
    padding: 0 12px;
    font-size: 12px;
}

summary {
    cursor: pointer;
    padding: 8px 0;
}

.settings {
    padding: 6px 0;
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    align-items: center;
}

select {
    min-width: 0;
    max-width: 100%;
    padding: 8px;
    border: 1px solid #c9bbdc;
    border-radius: 10px;
    background: white;
    font-size: 13px;
}

#voiceSelect {
    width: min(100%, 420px);
}

#voiceNote {
    line-height: 1.6;
    margin: 5px 0;
}

#status {
    margin: 0;
    padding: 6px 12px 10px;
    font-size: 12px;
    line-height: 1.5;
}

/* No separate scroll container inside the vocabulary area. */
main {
    padding: 12px;
}

.content {
    max-width: 960px;
    margin: 0 auto;
}

h2 {
    font-size: 21px;
    margin: 0 0 5px;
}

.hint {
    font-size: 13px;
    margin: 0 0 14px;
    line-height: 1.5;
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
    font-family: "Apple Color Emoji", "Segoe UI Emoji", sans-serif;
    font-size: 58px;
    margin-bottom: 12px;
}

.zh {
    font-family: "Microsoft YaHei", "PingFang SC", sans-serif;
    font-size: 32px;
    line-height: 1.5;
}

.pinyin {
    font-size: 17px;
    margin: 8px 0;
}

.english {
    font-size: 18px;
    line-height: 1.5;
}

.listen {
    font-size: 12px;
    margin-top: 10px;
    color: #586b60;
}

footer {
    text-align: center;
    padding: 24px 0 30px;
    font-size: 13px;
    color: #647969;
}

@media (max-width: 540px) {
    .cards {
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 10px;
    }

    .card {
        padding: 16px 8px;
    }

    .picture {
        font-size: 46px;
    }

    .zh {
        font-size: 28px;
    }

    .pinyin, .english {
        font-size: 15px;
    }
}/* Keep the compact title bar fixed at a predictable height. */
.top {
    position: sticky;
    top: 0;
    z-index: 30;
    height: 56px;
    min-height: 56px;
}

/* Keep the horizontally scrollable navigation below the title. */
#nav {
    position: sticky;
    top: 56px;
    z-index: 29;

    display: flex;
    flex-wrap: nowrap;
    gap: 6px;

    margin: 0;
    padding: 8px 12px;
    background: #fffdf8;
    border-bottom: 1px solid #e6e2ec;
    box-shadow: 0 3px 6px #00000006;

    overflow-x: auto;
    overflow-y: hidden;
    -webkit-overflow-scrolling: touch;
}

#nav button {
    flex: 0 0 auto;
    white-space: nowrap;
}

/* Leave room for both sticky bars when scrolling to content. */
.app {
    scroll-padding-top: 120px;
}.element-container:has(
    iframe[title="streamlit.components.v1.html"]
) {
    height: 100dvh !important;
}

[data-testid="stAppViewContainer"],
[data-testid="stMain"],
.stApp {
    min-height: 100dvh !important;
    background: #fffdf8 !important;
}
</style>
</head>

<body>
<div class="app" id="app">

    <div class="top">
        <h1>
            🐰 Myra &amp; Matthew
            <small>learning Chinese</small>
        </h1>

        <button class="small-button" id="stop">
            ⏹ Stop
        </button>
    </div>

    <nav id="nav" aria-label="Vocabulary categories"></nav>

    <p class="nav-hint">
        Swipe the categories left or right ↔
    </p>

    <details id="settings">
        <summary>⚙️ Voice settings</summary>

        <div class="settings">
            <label for="voiceSelect">Chinese voice</label>
            <select id="voiceSelect"></select>

            <label for="speed">Speed</label>
            <select id="speed">
                <option value="0.65">Slow</option>
                <option value="0.8" selected>Gentle</option>
                <option value="1">Normal</option>
            </select>

            <button class="small-button" id="testVoice">
                Test voice
            </button>

            <button class="small-button" id="refreshVoices">
                Refresh voices
            </button>

            <button class="small-button" id="closeSettings">
                Done
            </button>
        </div>

        <p id="voiceNote"></p>
    </details>

    <p id="status" role="status" aria-live="polite">
        Tap a picture to hear Chinese.
    </p>

    <main>
        <div class="content">
            <h2 id="heading"></h2>

            <p class="hint">
                Tap a picture. Listen. Say it with Bunny!
            </p>

            <div id="cards" class="cards"></div>

            <footer>
                🌷 A little Chinese, a little joy, every day! 🌷
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
} catch (error) {
    // Browser storage is optional.
}


// Include Mandarin voices and exclude Cantonese voices.
function isMandarin(voice) {
    const lang = voice.lang.replaceAll("_", "-").toLowerCase();

    return /^(zh$|zh-(cn|tw|sg|hans|hant)(-|$)|cmn)/.test(lang)
        && !/(hk|yue)/.test(lang);
}


// Prefer recognized female voices.
function knownFemale(voice) {
    return /xiaoxiao|xiaoyi|huihui|yaoyao|ting[- ]?ting|mei[- ]?jia|li[- ]?li/i
        .test(voice.name);
}


function loadVoices() {
    const select = $("voiceSelect");
    const previous = select.value || savedVoice;

    select.replaceChildren(
        new Option("Choose a Chinese voice…", "")
    );

    if (!synth) {
        $("voiceNote").textContent =
            "Speech is not supported in this browser. Try Edge or Chrome.";
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
        voices.find(voice => voice.voiceURI === previous)
        || voices.find(knownFemale);

    if (chosen) {
        select.value = chosen.voiceURI;
    }

    if (!voices.length) {
        $("voiceNote").textContent =
            "No Mandarin voice was found. Try Refresh voices. "
            + "If none appear, add a Mandarin voice to your device "
            + "and restart your browser.";
    } else {
        $("voiceNote").textContent =
            "For a female voice, look for Xiaoxiao, Huihui, or Tingting. "
            + "Available voices depend on your device.";
    }
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


function openVoiceSettings() {
    $("settings").open = true;
    $("app").scrollTop = 0;
}


function speak(chinese, card = null) {
    stopSpeech();

    if (!synth || !window.SpeechSynthesisUtterance) {
        $("status").textContent =
            "This browser does not support speech.";
        openVoiceSettings();
        return;
    }

    loadVoices();

    const voice = voices.find(
        item => item.voiceURI === $("voiceSelect").value
    );

    if (!voice) {
        $("status").textContent =
            "Please choose a Chinese voice, then tap the picture again.";
        openVoiceSettings();
        return;
    }

    const current = token;

    // Speak Chinese only.
    utterance = new SpeechSynthesisUtterance(chinese);
    utterance.lang = voice.lang;
    utterance.voice = voice;
    utterance.rate = Number($("speed").value);
    utterance.pitch = 1;
    utterance.volume = 1;

    activeCard = card;

    if (card) {
        card.classList.add("active");
    }

    $("status").textContent = "🔊 " + chinese;

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
        finish("⭐ Great job! Tap again or choose another word.");
    };

    utterance.onerror = () => {
        if (current !== token) {
            return;
        }

        finish(
            "The voice could not play. Try another voice in Voice settings."
        );

        openVoiceSettings();
    };

    try {
        synth.speak(utterance);
    } catch (error) {
        finish("Could not start speech. Please check Voice settings.");
        openVoiceSettings();
    }
}


function addText(parent, text, className, language) {
    const span = document.createElement("span");

    span.textContent = text;
    span.className = className;

    if (language) {
        span.lang = language;
    }

    parent.appendChild(span);
}


function showCategory(index) {
    stopSpeech();

    const category = DATA[index];

    $("heading").textContent =
        category.icon + " " + category.name;

    $("status").textContent =
        "Tap a picture to hear Chinese.";

    $("cards").replaceChildren();

    [...$("nav").children].forEach((button, buttonIndex) => {
        button.setAttribute(
            "aria-pressed",
            String(buttonIndex === index)
        );
    });

    category.items.forEach(word => {
        const button = document.createElement("button");

        button.className = "card";

        button.setAttribute(
            "aria-label",
            "Hear " + word.en + " in Chinese"
        );

        addText(button, word.icon, "picture");
        addText(button, word.zh, "zh", "zh-CN");
        addText(button, word.pinyin, "pinyin");
        addText(button, word.en, "english", "en");
        addText(button, "🔊 Tap to listen", "listen");

        button.onclick = () => {
            speak(word.zh, button);
        };

        $("cards").appendChild(button);
    });

    // Collapse settings when switching categories.
    $("settings").open = false;
    $("app").scrollTop = 0;
}


// Build compact navigation buttons.
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

    $("status").textContent =
        "Stopped. Tap a picture to listen again.";
};


$("voiceSelect").onchange = () => {
    stopSpeech();

    savedVoice = $("voiceSelect").value;

    try {
        localStorage.setItem(
            "bunnyChineseVoice",
            savedVoice
        );
    } catch (error) {
        // Voice selection still works without browser storage.
    }

    $("status").textContent =
        "Voice changed. Tap Test voice or Done.";
};


$("testVoice").onclick = () => {
    speak("你好");
};


$("refreshVoices").onclick = loadVoices;


$("closeSettings").onclick = () => {
    $("settings").open = false;
};


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


payload = json.dumps(
    categories,
    ensure_ascii=False,
).replace("<", "\\u003c")


components.html(
    PAGE.replace("__DATA__", payload),
    height=800,
    scrolling=False,
)
