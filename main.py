
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
# 2. 화면 디자인
# ==========================================
# CSS는 웹사이트의 색상, 크기, 배치 등을 꾸미는 코드야.

st.markdown("""
<style>
/* 페이지 여백을 줄여 스크롤을 최소화해 */
.block-container {
    padding-top: 0.8rem;
    padding-bottom: 0.3rem;
    padding-left: 1rem;
    padding-right: 1rem;
    max-width: 100%;
}

/* 제목 */
.main-title {
    font-size: clamp(22px, 2.2vw, 34px);
    font-weight: 800;
    margin-bottom: 0.5rem;
}

/* 색상 버튼의 기본 모양 */
div[data-testid="stButton"] > button {
    width: 100%;
    min-height: 48px;
    padding: 0.2rem;
    border-radius: 9px;
    font-weight: 700;
}

/* 12가지 색상의 버튼 배경색 */
.st-key-color_빨강 button { background: #E53935; color: white; }
.st-key-color_주황 button { background: #FB8C00; color: white; }
.st-key-color_노랑 button { background: #FDD835; color: #222; }
.st-key-color_초록 button { background: #43A047; color: white; }
.st-key-color_파랑 button { background: #1E88E5; color: white; }
.st-key-color_하늘색 button { background: #4FC3F7; color: #222; }
.st-key-color_보라 button { background: #8E24AA; color: white; }
.st-key-color_분홍 button { background: #EC407A; color: white; }
.st-key-color_검정 button { background: #303030; color: white; }
.st-key-color_회색 button { background: #9E9E9E; color: #222; }
.st-key-color_하양 button { background: #FFFFFF; color: #222; }
.st-key-color_갈색 button { background: #795548; color: white; }

/* 선택 상태를 테두리로 구분해 */
.st-key-color_빨강 button,
.st-key-color_주황 button,
.st-key-color_노랑 button,
.st-key-color_초록 button,
.st-key-color_파랑 button,
.st-key-color_하늘색 button,
.st-key-color_보라 button,
.st-key-color_분홍 button,
.st-key-color_검정 button,
.st-key-color_회색 button,
.st-key-color_하양 button,
.st-key-color_갈색 button {
    border: 2px solid #777;
}

/* 퍼슈트 이름을 크고 굵게 표시해 */
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

/* 낮은 화면에서는 여백과 제목 크기를 줄여 */
@media (max-height: 750px) {
    .block-container {
        padding-top: 0.3rem;
    }
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. 색상 목록
# ==========================================
# 색상 이름과 실제 버튼 색상을 연결해.

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
# 4. 퍼슈트 정보 입력
# ==========================================
# 사진은 GitHub의 images 폴더에 넣어 줘.
# image에는 사진의 경로를 입력하면 돼.
# 예: images/ruby.jpg

fursuits = {
    "빨강": [
        {
            "name": "여기에 퍼슈트 이름 입력",
            "image": "images/il_794xN.7501864133_o83h.webp",
            "description": "여기에 퍼슈트의 특징을 적어 줘.",
            "maker": "마라톤",
            "link": "https://www.etsy.com/listing/1699301493/complete-fursuit-custom-furry-full-suit"
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
# 처음에는 빨강을 선택하고, 버튼을 누르면 선택 색상이 바뀌어.

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
# 7. 화면을 3개 영역으로 나누기
# ==========================================
# 왼쪽은 색상, 가운데는 사진, 오른쪽은 정보 영역이야.
# 숫자가 클수록 영역의 너비가 넓어져.

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

    # 두 개의 열을 만들어 색상을 6개씩 배치해.
    col1, col2 = st.columns(2, gap="small")

    for index, color_name in enumerate(color_names):
        # 앞의 6개는 왼쪽, 뒤의 6개는 오른쪽 열에 표시해.
        target_col = col1 if index < 6 else col2

        with target_col:
            # 현재 선택된 색상에는 체크 표시를 붙여.
            if st.session_state.selected_color == color_name:
                label = f"✓ {color_name}"
            else:
                label = color_name

            # 실제 색상 버튼을 눌렀을 때 선택 색상을 변경해.
            if st.button(
                label,
                key=f"color_{color_name}",
                use_container_width=True
            ):
                st.session_state.selected_color = color_name
                st.rerun()

# 선택된 색상과 퍼슈트 목록을 가져와.
selected_color = st.session_state.selected_color
suits = fursuits.get(selected_color, [])

# ==========================================
# 9. 가운데: 퍼슈트 사진
# ==========================================
with center:
    st.markdown("#### 퍼슈트 사진")

    if suits:
        # 같은 색상에 퍼슈트가 여러 개면 선택 메뉴를 표시해.
        if len(suits) > 1:
            suit_names = [s["name"] for s in suits]
            selected_name = st.selectbox(
                "퍼슈트 선택",
                suit_names,
                label_visibility="collapsed"
            )
            suit = next(s for s in suits if s["name"] == selected_name)
        else:
            suit = suits[0]

        # 사진 파일의 실제 위치를 확인해.
        image_path = BASE_DIR / suit["image"]

        if image_path.is_file():
            # 사진의 원래 비율을 유지하며 화면 너비에 맞춰 표시해.
            # 사진은 2:3 비율로 준비하는 것을 권장해.
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
        st.info(f"아직 {selected_color} 퍼슈트가 등록되지 않았어요.")

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

        # 선택한 색상을 작은 색상 표시와 함께 보여 줘.
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

        # 제작자 정보가 있을 때만 표시해.
        if suit.get("maker"):
            st.markdown("**제작자**")
            st.write(suit["maker"])

        # 링크가 있을 때만 표시해.
        if suit.get("link"):
            st.markdown(f"[관련 링크 열기]({suit['link']})")

    else:
        st.markdown("### 등록된 정보가 없어요")
        st.write("이 색상의 퍼슈트 정보를 추가하면 여기에 표시돼.")

# ==========================================
# 11. 하단 안내
# ==========================================
st.caption("퍼슈트 컬러 도감")
