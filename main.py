
import streamlit as st
from pathlib import Path

# ==========================================
# 1. 웹사이트 기본 설정
# ==========================================

st.set_page_config(
    page_title="퍼슈트 컬러 도감",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

BASE_DIR = Path(__file__).parent

# ==========================================
# 2. 색상 목록
# ==========================================
# 색상 이름과 실제 버튼 배경색을 연결해.
# 색상을 추가하거나 바꾸고 싶으면 이 부분을 수정하면 돼.

colors = {
    "빨강": "#E53935",
    "주황": "#FB8C00",
    "노랑": "#FDD835",
    "초록": "#43A047",
    "파랑": "#1E88E5",
    "하늘색": "#4FC3F7",
    "보라": "#8E24AA",
    "분홍": "#EC407A",
    "검정": "#303030",
    "회색": "#9E9E9E",
    "하양": "#FFFFFF",
    "갈색": "#795548",
}

# ==========================================
# 3. 화면 디자인
# ==========================================
# CSS는 버튼의 색상, 테두리, 크기 등을 꾸미는 코드야.

st.markdown("""
<style>
/* 화면 여백을 줄여 공간을 확보해 */
.block-container {
    padding-top: 0.8rem;
    padding-bottom: 0.3rem;
    padding-left: 1rem;
    padding-right: 1rem;
    max-width: 100%;
}

/* 웹사이트 제목 */
.main-title {
    font-size: clamp(22px, 2.2vw, 34px);
    font-weight: 800;
    margin-bottom: 0.5rem;
}

/* 모든 색상 버튼의 공통 크기와 모양 */
div[data-testid="stButton"] > button {
    width: 100%;
    min-height: 48px;
    padding: 0.2rem;
    border-radius: 9px;
    font-weight: 700;
    border: 2px solid #777777;
    transition: filter 0.15s ease;
}

/* 마우스를 올리면 버튼이 살짝 밝아져 */
div[data-testid="stButton"] > button:hover {
    filter: brightness(1.08);
    border: 2px solid #222222;
}

/* 빨강 */
.st-key-color_빨강 button {
    background-color: #E53935 !important;
    color: white !important;
}

/* 주황 */
.st-key-color_주황 button {
    background-color: #FB8C00 !important;
    color: white !important;
}

/* 노랑 */
.st-key-color_노랑 button {
    background-color: #FDD835 !important;
    color: #222222 !important;
}

/* 초록 */
.st-key-color_초록 button {
    background-color: #43A047 !important;
    color: white !important;
}

/* 파랑 */
.st-key-color_파랑 button {
    background-color: #1E88E5 !important;
    color: white !important;
}

/* 하늘색 */
.st-key-color_하늘색 button {
    background-color: #4FC3F7 !important;
    color: #222222 !important;
}

/* 보라 */
.st-key-color_보라 button {
    background-color: #8E24AA !important;
    color: white !important;
}

/* 분홍 */
.st-key-color_분홍 button {
    background-color: #EC407A !important;
    color: white !important;
}

/* 검정 */
.st-key-color_검정 button {
    background-color: #303030 !important;
    color: white !important;
}

/* 회색 */
.st-key-color_회색 button {
    background-color: #9E9E9E !important;
    color: #222222 !important;
}

/* 하양 */
.st-key-color_하양 button {
    background-color: #FFFFFF !important;
    color: #222222 !important;
}

/* 갈색 */
.st-key-color_갈색 button {
    background-color: #795548 !important;
    color: white !important;
}

/* 선택한 버튼은 더 굵은 검정 테두리로 강조 */
.st-key-color_빨강 button:focus,
.st-key-color_주황 button:focus,
.st-key-color_노랑 button:focus,
.st-key-color_초록 button:focus,
.st-key-color_파랑 button:focus,
.st-key-color_하늘색 button:focus,
.st-key-color_보라 button:focus,
.st-key-color_분홍 button:focus,
.st-key-color_검정 button:focus,
.st-key-color_회색 button:focus,
.st-key-color_하양 button:focus,
.st-key-color_갈색 button:focus {
    outline: 3px solid #222222 !important;
    outline-offset: 2px;
}

/* 퍼슈트 이름은 크고 굵게 표시 */
.suit-name {
    font-size: clamp(25px, 3vw, 42px);
    font-weight: 850;
    line-height: 1.15;
    overflow-wrap: anywhere;
    margin-bottom: 1rem;
}

/* 퍼슈트 설명 글씨 */
.suit-info {
    font-size: clamp(14px, 1.2vw, 18px);
    line-height: 1.6;
    overflow-wrap: anywhere;
}

/* 낮은 화면에서는 여백을 줄여 */
@media (max-height: 750px) {
    .block-container {
        padding-top: 0.3rem;
    }
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# 4. 퍼슈트 정보 입력
# ==========================================
# 사진은 GitHub의 images 폴더에 넣어 줘.
# image에는 사진 파일의 경로를 입력해.
# 예: images/ruby.jpg

fursuits = {
    "빨강": [
        {
            "name": "여기에 퍼슈트 이름 입력",
            "image": "images/red_example.jpg",
            "description": "여기에 퍼슈트의 특징을 적어 줘.",
            "maker": "마라톤",
            "link": ""
        }
    ],
    "주황": [],
    "노랑": [],
    "초록": [],
    "파랑": [],
    "하늘색": [],
    "보라": [],
    "분홍": [],
    "검정": [],
    "회색": [],
    "하양": [],
    "갈색": [],
}

# ==========================================
# 5. 선택한 색상 기억하기
# ==========================================

if "selected_color" not in st.session_state:
    st.session_state.selected_color = "빨강"

# ==========================================
# 6. 페이지 제목
# ==========================================

st.markdown(
    '<div class="main-title">퍼슈트 컬러 도감</div>',
    unsafe_allow_html=True
)

# ==========================================
# 7. 화면을 왼쪽 / 가운데 / 오른쪽으로 나누기
# ==========================================

left, center, right = st.columns(
    [1, 2, 3],
    gap="medium",
    vertical_alignment="top"
)

# ==========================================
# 8. 왼쪽: 색상 선택 버튼 6행 × 2열
# ==========================================

with left:
    st.markdown("#### 색상 선택")

    color_names = list(colors.keys())

    # 두 개의 열에 색상을 6개씩 배치해.
    col1, col2 = st.columns(2, gap="small")

    for index, color_name in enumerate(color_names):
        # 앞의 6개는 왼쪽, 뒤의 6개는 오른쪽 열에 표시해.
        target_col = col1 if index < 6 else col2

        with target_col:
            # 현재 선택한 색상에는 체크 표시를 붙여.
            if st.session_state.selected_color == color_name:
                label = f"✓ {color_name}"
            else:
                label = color_name

            # 버튼 배경색은 위 CSS에서 지정한 실제 색으로 표시돼.
            if st.button(
                label,
                key=f"color_{color_name}",
                use_container_width=True
            ):
                st.session_state.selected_color = color_name
                st.rerun()

# 선택한 색상에 맞는 퍼슈트 목록을 가져와.
selected_color = st.session_state.selected_color
suits = fursuits.get(selected_color, [])

# ==========================================
# 9. 가운데: 퍼슈트 사진
# ==========================================

with center:
    st.markdown("#### 퍼슈트 사진")

    if suits:
        # 같은 색상의 퍼슈트가 여러 개라면 선택 메뉴를 표시해.
        if len(suits) > 1:
            suit_names = [s["name"] for s in suits]

            selected_name = st.selectbox(
                "퍼슈트 선택",
                suit_names,
                label_visibility="collapsed"
            )

            suit = next(
                s for s in suits
                if s["name"] == selected_name
            )
        else:
            suit = suits[0]

        # 사진 파일의 실제 위치를 확인해.
        image_path = BASE_DIR / suit["image"]

        if image_path.is_file():
            st.image(
                str(image_path),
                use_container_width=True
            )
        else:
            st.warning(
                f"사진을 찾을 수 없어요: {suit['image']}"
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
        # 이름을 크고 굵게 표시해.
        st.markdown(
            f'<div class="suit-name">{suit["name"]}</div>',
            unsafe_allow_html=True
        )

        # 선택한 색상도 실제 색상 사각형과 함께 표시해.
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
                    background:{colors[selected_color]};
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
# 11. 페이지 아래쪽 안내
# ==========================================

st.caption("퍼슈트 컬러 도감")
