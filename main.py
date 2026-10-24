
import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import html

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
st.markdown("""
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
</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. 색상 목록
# ==========================================
# 각 색상의 이름과 실제 색상 코드를 지정해.
# 이 색상 코드로 이모지가 아닌 사각형을 그려.

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
# 4. 퍼슈트 정보
# ==========================================
# 사진은 images 폴더에 넣고 파일 경로를 입력해.
# 이름과 설명 등은 네가 원하는 정보로 수정하면 돼.

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
# 7. 화면을 세 영역으로 나누기
# ==========================================
left, center, right = st.columns(
    [1, 2, 3],
    gap="medium",
    vertical_alignment="top"
)

# ==========================================
# 8. 왼쪽: 색상 선택
# ==========================================
with left:
    st.markdown("#### 색상 선택")

    color_names = list(colors.keys())

    # 색상 버튼을 6행 × 2열로 배치해.
    # HTML로 색상 사각형을 직접 그리므로
    # 브라우저의 이모지 표시 방식에 영향을 받지 않아.

    for row in range(6):
        col_a, col_b = st.columns(2, gap="small")

        # 각 행에 표시할 두 가지 색상
        row_colors = [color_names[row], color_names[row + 6]]

        for col, color_name in zip([col_a, col_b], row_colors):
            with col:
                selected = (
                    st.session_state.selected_color == color_name
                )

                # 선택된 색상은 테두리를 더 진하게 표시해.
                border_color = "#222222" if selected else "#D0D0D0"
                border_width = "3px" if selected else "1px"

                # 버튼 안에 색상 사각형과 이름을 함께 표시해.
                # 색상 사각형은 HTML/CSS로 그린 실제 도형이야.
                button_html = f"""
                <div style="
                    display:flex;
                    align-items:center;
                    justify-content:center;
                    gap:7px;
                    border:{border_width} solid {border_color};
                    border-radius:9px;
                    padding:8px 3px;
                    margin-bottom:5px;
                    min-height:30px;
                    background:#FFFFFF;
                    color:#222222;
                    font-size:13px;
                    font-weight:600;
                    box-sizing:border-box;
                ">
                    <span style="
                        display:inline-block;
                        width:17px;
                        height:17px;
                        min-width:17px;
                        background:{colors[color_name]};
                        border:1px solid #888888;
                        border-radius:3px;
                        box-sizing:border-box;
                    "></span>
                    <span>{html.escape(color_name)}</span>
                </div>
                """

                st.markdown(button_html, unsafe_allow_html=True)

                # 실제 클릭 동작은 Streamlit 버튼이 담당해.
                if st.button(
                    f"{color_name} 선택",
                    key=f"color_{color_name}",
                    use_container_width=True
                ):
                    st.session_state.selected_color = color_name
                    st.rerun()

# ==========================================
# 9. 선택한 퍼슈트 정보 불러오기
# ==========================================
selected_color = st.session_state.selected_color
suits = fursuits.get(selected_color, [])

# ==========================================
# 10. 가운데: 퍼슈트 사진
# ==========================================
with center:
    st.markdown("#### 퍼슈트 사진")

    if suits:
        if len(suits) > 1:
            suit_names = [s["name"] for s in suits]
            selected_name = st.selectbox(
                "퍼슈트 선택",
                suit_names,
                label_visibility="collapsed"
            )
            suit = next(
                s for s in suits if s["name"] == selected_name
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
                f"사진을 찾을 수 없어요: {suit['image']}"
            )
    else:
        suit = None
        st.info(
            f"아직 {selected_color} 퍼슈트가 등록되지 않았어요."
        )

# ==========================================
# 11. 오른쪽: 퍼슈트 정보
# ==========================================
with right:
    st.markdown("#### 퍼슈트 정보")

    if suit:
        st.markdown(
            f'<div class="suit-name">'
            f'{html.escape(suit["name"])}</div>',
            unsafe_allow_html=True
        )

        # 현재 선택한 색상과 사각형을 함께 표시해.
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
                {html.escape(selected_color)}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("**소개**")
        st.markdown(
            f'<div class="suit-info">'
            f'{html.escape(suit["description"])}</div>',
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
# 12. 하단 안내
# ==========================================
st.caption("퍼슈트 컬러 도감")
