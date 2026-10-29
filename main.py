
import streamlit as st
from pathlib import Path

# ==========================================
# 1. 기본 설정
# ==========================================

st.set_page_config(
    page_title="퍼슈트 컬러 도감",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

BASE_DIR = Path(__file__).parent

# ==========================================
# 2. 색상 정보
# ==========================================
# key: 내부에서 사용하는 영문 식별자
# name: 화면에 표시할 한글 색상 이름
# hex: 버튼에 적용할 실제 색상

colors = [
    {"key": "red", "name": "빨강", "hex": "#E53935", "text": "#FFFFFF"},
    {"key": "orange", "name": "주황", "hex": "#FB8C00", "text": "#FFFFFF"},
    {"key": "yellow", "name": "노랑", "hex": "#FDD835", "text": "#222222"},
    {"key": "green", "name": "초록", "hex": "#43A047", "text": "#FFFFFF"},
    {"key": "blue", "name": "파랑", "hex": "#1E88E5", "text": "#FFFFFF"},
    {"key": "skyblue", "name": "하늘색", "hex": "#4FC3F7", "text": "#222222"},
    {"key": "purple", "name": "보라", "hex": "#8E24AA", "text": "#FFFFFF"},
    {"key": "pink", "name": "분홍", "hex": "#EC407A", "text": "#FFFFFF"},
    {"key": "black", "name": "검정", "hex": "#303030", "text": "#FFFFFF"},
    {"key": "gray", "name": "회색", "hex": "#9E9E9E", "text": "#222222"},
    {"key": "white", "name": "하양", "hex": "#FFFFFF", "text": "#222222"},
    {"key": "brown", "name": "갈색", "hex": "#795548", "text": "#FFFFFF"},
]

# ==========================================
# 3. 웹사이트 디자인
# ==========================================
# 버튼 식별자는 영문으로 지정했어.
# 그래서 CSS가 각 버튼을 구분하기 쉬워져.

css = """
<style>
.block-container {
    padding-top: 0.8rem;
    padding-bottom: 0.3rem;
    padding-left: 1rem;
    padding-right: 1rem;
    max-width: 100%;
}

.main-title {
    font-size: clamp(22px, 2.2vw, 34px);
    font-weight: 800;
    margin-bottom: 0.5rem;
}

/* 모든 색상 버튼의 기본 크기 */
div[data-testid="stButton"] > button {
    width: 100%;
    min-height: 48px;
    border-radius: 9px;
    font-weight: 700;
    border: 2px solid #777777;
    transition: filter 0.15s ease;
}

/* 각 버튼의 실제 배경색 */
.st-key-color_red button {
    background-color: #E53935 !important;
    color: #FFFFFF !important;
}
.st-key-color_orange button {
    background-color: #FB8C00 !important;
    color: #FFFFFF !important;
}
.st-key-color_yellow button {
    background-color: #FDD835 !important;
    color: #222222 !important;
}
.st-key-color_green button {
    background-color: #43A047 !important;
    color: #FFFFFF !important;
}
.st-key-color_blue button {
    background-color: #1E88E5 !important;
    color: #FFFFFF !important;
}
.st-key-color_skyblue button {
    background-color: #4FC3F7 !important;
    color: #222222 !important;
}
.st-key-color_purple button {
    background-color: #8E24AA !important;
    color: #FFFFFF !important;
}
.st-key-color_pink button {
    background-color: #EC407A !important;
    color: #FFFFFF !important;
}
.st-key-color_black button {
    background-color: #303030 !important;
    color: #FFFFFF !important;
}
.st-key-color_gray button {
    background-color: #9E9E9E !important;
    color: #222222 !important;
}
.st-key-color_white button {
    background-color: #FFFFFF !important;
    color: #222222 !important;
}
.st-key-color_brown button {
    background-color: #795548 !important;
    color: #FFFFFF !important;
}

/* 마우스를 올리면 살짝 밝아져 */
div[data-testid="stButton"] > button:hover {
    filter: brightness(1.08);
    border: 2px solid #222222 !important;
}

/* 퍼슈트 이름 */
.suit-name {
    font-size: clamp(25px, 3vw, 42px);
    font-weight: 850;
    line-height: 1.15;
    overflow-wrap: anywhere;
    margin-bottom: 1rem;
}

.suit-info {
    font-size: clamp(14px, 1.2vw, 18px);
    line-height: 1.6;
    overflow-wrap: anywhere;
}

@media (max-height: 750px) {
    .block-container {
        padding-top: 0.3rem;
    }
}
</style>
"""

st.markdown(css, unsafe_allow_html=True)

# ==========================================
# 4. 퍼슈트 정보
# ==========================================
# 사진은 images 폴더에 넣어 줘.
# 사진 경로와 파일 이름이 정확히 일치해야 해.

fursuits = {
    "빨강": [
        {
            "name": "수라",
            "image": "images/red_example.jpg",
            "description": "수라는 드래곤 퍼슈트를 착용하는 퍼슈터입니다.\n퍼슈트는 @333sango와 @erqingZ가 제작했으며 FurAffinity #dragon_shura로 활동합니다.\n주로 화려한 드래곤 푸르슈트 사진과 재치 있는 캡션을 게시하며 팬들과 소통합니다.",
            "maker": "@333sango & @ErqingZ",
            "link": "https://x.com/shura_fursuit?s=11"
        }
    ],
    "주황": [        {
            "name": "츠나",
            "image": "images/joohaw_example.jpg",
            "description": "@Tsuna_9H는 🦊 츠나 캐릭터로 활동하는 퍼슈터입니다. \n 여우 테마 퍼슈트를 착용한 일상을 #FursuitEveryday 해시태그와 함께 공유하며, @guni1636, @AN_Chobi94, @fluffyjellydog 등 아티스트와 협업한 콘텐츠를 프로필에 활용합니다. \n 5000명 이상 팔로워를 가진 블루 인증 계정으로 커뮤니티 내 활발한 소통을 이어갑니다.",
            "maker": "JellyDog",
            "link": "https://x.com/tsuna_9h?s=11"
        }],
    "노랑": [        {
            "name": "부웅",
            "image": "images/norang_example.jpg",
            "description": "@voooong_은 🐝 부웅(ブーウン)이라는 꿀벌 테마의 퍼리 캐릭터로 fursuit 활동을 하는 사용자입니다. @PRODUCTIONGAL_ 크루 멤버로서 퍼리 이벤트 참여와 디자인 작업을 하고 있으며, 한국어와 일본어를 주로 사용합니다.",
            "maker": "JellyDog",
            "link": "https://x.com/voooong_?s=11"
        }],
    "초록": [        {
            "name": "유우소(悠草)",
            "image": "images/green_example.jpg",
            "description": "@inugami_31은 케모노(인간형 동물)와 춤을 좋아하는 사용자입니다. 버니즈 랄스, 동양용 아를스, 드래곤 유우소우를 두고 있으며 케모노 커뮤니티에서 일상과 관련 콘텐츠를 공유합니다. 2600명 이상의 팔로워를 보유하고 있습니다.",
            "maker": "Furmony",
            "link": "https://x.com/inugami_31?s=11"
        }],
    "파랑": [        {
            "name": "프레일",
            "image": "images/blue_example.jpg",
            "description": "여기에 퍼슈트의 특징을 적어 줘.",
            "maker": "@XiangshanStudio & @Ghosts76532892",
            "link": "https://x.com/_freil?s=11"
        }],
    "하늘색": [        {
            "name": "유진",
            "image": "images/sky_example.jpg",
            "description": "여기에 퍼슈트의 특징을 적어 줘.",
            "maker": "여퍼만(자체 제작)",
            "link": "https://x.com/unknown_1251?s=11"
        }],
    "보라": [        {
            "name": "소게(そが)",
            "image": "images/bola_example.jpg",
            "description": "여기에 퍼슈트의 특징을 적어 줘.",
            "maker": "Doggy Studio(犬工房)",
            "link": "https://x.com/biohazard_29?s=11"
        }],
    "분홍": [        {
            "name": "레이",
            "image": "images/pink_example.jpg",
            "description": "여기에 퍼슈트의 특징을 적어 줘.",
            "maker": "Furmony",
            "link": "https://x.com/ray_fursuit?s=11"
        }],
    "검정": [        {
            "name": "화미",
            "image": "images/black_example.jpg",
            "description": "여기에 퍼슈트의 특징을 적어 줘.",
            "maker": "알수없음",
            "link": "https://x.com/hwami_furry?s=11"
        }],
    "회색": [        {
            "name": "미히라(メキラ)",
            "image": "images/howsec_example.jpg",
            "description": "여기에 퍼슈트의 특징을 적어 줘.",
            "maker": "K-LINE",
            "link": "https://x.com/run_charizard?s=11"
        }],
    "하양": [        {
            "name": "푸르토(果糖含量)",
            "image": "images/white_example.jpg",
            "description": "여기에 퍼슈트의 특징을 적어 줘.",
            "maker": "Furpolis/虛構都市",
            "link": "https://x.com/fructose_c?s=11"
        }],
    "갈색": [        {
            "name": "슈키",
            "image": "images/garsec_example.jpg",
            "description": "여기에 퍼슈트의 특징을 적어 줘.",
            "maker": "BINARI FURSUIT",
            "link": "https://x.com/syuki_fur?s=11"
        }],
}

# ==========================================
# 5. 선택한 색상 기억하기
# ==========================================

if "selected_color" not in st.session_state:
    st.session_state.selected_color = "빨강"

# ==========================================
# 6. 제목
# ==========================================

st.markdown(
    '<div class="main-title">퍼슈트 컬러 도감</div>',
    unsafe_allow_html=True
)

# ==========================================
# 7. 화면 3개 영역
# ==========================================

left, center, right = st.columns(
    [1, 2, 3],
    gap="medium",
    vertical_alignment="top"
)

# ==========================================
# 8. 왼쪽: 색상 버튼 6행 × 2열
# ==========================================

with left:
    st.markdown("#### 색상 선택")

    col1, col2 = st.columns(2, gap="small")

    for index, color in enumerate(colors):
        # 앞의 6개는 왼쪽 열, 뒤의 6개는 오른쪽 열
        target_col = col1 if index < 6 else col2

        with target_col:
            name = color["name"]
            key = color["key"]

            # 선택한 색상에 체크 표시를 붙여.
            label = (
                f"✓ {name}"
                if st.session_state.selected_color == name
                else name
            )

            # 영문 key가 CSS의 버튼 색상 설정과 연결돼.
            if st.button(
                label,
                key=f"color_{key}",
                use_container_width=True
            ):
                st.session_state.selected_color = name
                st.rerun()

# 선택된 색상의 퍼슈트 목록
selected_color = st.session_state.selected_color
suits = fursuits.get(selected_color, [])

# ==========================================
# 9. 가운데: 퍼슈트 사진
# ==========================================

with center:
    st.markdown("#### 퍼슈트 사진")

    if suits:
        if len(suits) > 1:
            names = [s["name"] for s in suits]

            chosen_name = st.selectbox(
                "퍼슈트 선택",
                names,
                label_visibility="collapsed"
            )

            suit = next(
                s for s in suits
                if s["name"] == chosen_name
            )
        else:
            suit = suits[0]

        image_path = BASE_DIR / suit["image"]

        if image_path.is_file():
            st.image(
                str(image_path),
                use_container_width=True
            )
        else:
            st.warning(
                f"사진 파일을 찾을 수 없어요: {suit['image']}"
            )
    else:
        suit = None
        st.info(
            f"아직 {selected_color} 퍼슈트가 등록되지 않았어요."
        )

# ==========================================
# 10. 오른쪽: 퍼슈트 정보
# ==========================================

with right:
    st.markdown("#### 퍼슈트 정보")

    if suit:
        st.markdown(
            f'<div class="suit-name">{suit["name"]}</div>',
            unsafe_allow_html=True
        )

        # 선택한 색상 사각형과 이름
        selected_hex = next(
            c["hex"] for c in colors
            if c["name"] == selected_color
        )

        st.markdown(
            f"""
            <div style="
                display:flex;
                align-items:center;
                gap:8px;
                margin-bottom:12px;
                font-size:14px;
            ">
                <span style="
                    width:16px;
                    height:16px;
                    display:inline-block;
                    background:{selected_hex};
                    border:1px solid #888;
                    border-radius:3px;
                "></span>
                {selected_color}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("**소개**")
        st.markdown(
            f'<div class="suit-info">{suit["description"]}</div>',
            unsafe_allow_html=True
        )

        if suit.get("maker"):
            st.markdown("**제작자**")
            st.write(suit["maker"])

        if suit.get("link"):
            st.markdown(f"[관련 링크 열기]({suit['link']})")

    else:
        st.markdown("### 등록된 정보가 없어요")
        st.write(
            "이 색상의 퍼슈트 정보를 추가하면 여기에 표시돼."
        )

# ==========================================
# 11. 하단 안내
# ==========================================

st.caption("퍼슈트 컬러 도감")
