
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
# 2. 화면 디자인
# ==========================================
# 페이지 여백과 색상 버튼, 사진 영역을 꾸미는 CSS야.
# CSS는 웹사이트의 크기와 색상, 배치 등을 정하는 코드야.

st.markdown("""
<style>
/* 화면 전체의 여백을 줄여 공간을 확보해 */
.block-container {
    padding-top: 1rem;
    padding-bottom: 0.5rem;
    padding-left: 1.2rem;
    padding-right: 1.2rem;
    max-width: 100%;
}

/* 화면 높이에 맞춰 주요 콘텐츠를 배치해 */
.main-title {
    font-size: clamp(22px, 2.2vw, 34px);
    font-weight: 800;
    margin-bottom: 0.5rem;
}

/* 색상 버튼의 공통 디자인 */
div[data-testid="stButton"] > button {
    width: 100%;
    min-height: 42px;
    padding: 0.25rem;
    border-radius: 9px;
    font-weight: 650;
}

/* 왼쪽 색상 버튼에 표시할 색상 사각형 */
.color-square {
    display: inline-block;
    width: 17px;
    height: 17px;
    border-radius: 3px;
    border: 1px solid #888;
    vertical-align: middle;
    margin-right: 5px;
}

/* 사진 영역은 가운데 정렬 */
.photo-frame {
    display: flex;
    align-items: center;
    justify-content: center;
}

/* 퍼슈트 이름은 크고 굵게 표시 */
.suit-name {
    font-size: clamp(25px, 3vw, 42px);
    font-weight: 850;
    line-height: 1.15;
    overflow-wrap: anywhere;
    margin-bottom: 1rem;
}

/* 정보 글씨 크기 */
.suit-info {
    font-size: clamp(14px, 1.2vw, 18px);
    line-height: 1.6;
    overflow-wrap: anywhere;
}

/* 작은 화면에서 위아래 여백을 더 줄여 */
@media (max-height: 750px) {
    .block-container {
        padding-top: 0.4rem;
    }
    h1 {
        font-size: 1.5rem !important;
    }
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# 3. 색상 목록
# ==========================================
# name: 화면에 표시할 색상 이름
# hex: 색상 사각형에 사용할 색상 코드

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
# 네 퍼슈트의 이름과 사진 경로, 설명 등을 이곳에 입력해.
# 사진은 GitHub의 images 폴더에 넣어 줘.
#
# 사진 경로 예시: images/ruby.jpg
# 사진은 세로 2:3 비율을 권장해.
#
# 한 색상에 여러 퍼슈트가 있다면 목록 안에
# { }로 묶은 정보를 추가하면 돼.

fursuits = {
    "빨강": [
        {
            "name": "여기에 퍼슈트 이름 입력",
            "image": "images/red_example.jpg",
            "description": "여기에 퍼슈트의 특징이나 소개를 적어 줘.",
            "maker": "",
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
# 5. 현재 선택된 색상 기억하기
# ==========================================
# 버튼을 누르면 선택된 색상을 저장하고 해당 퍼슈트를 표시해.
# 처음 사이트를 열었을 때는 빨강이 선택돼.

if "selected_color" not in st.session_state:
    st.session_state.selected_color = "빨강"

# ==========================================
# 6. 페이지 제목
# ==========================================

st.markdown(
    '<div class="main-title">🎨 퍼슈트 컬러 도감</div>',
    unsafe_allow_html=True
)

# ==========================================
# 7. 화면을 왼쪽 / 가운데 / 오른쪽으로 나누기
# ==========================================
# 숫자는 각 영역의 상대적인 너비야.
# 왼쪽 1, 가운데 2, 오른쪽 3 비율로 배치해.

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

    # 두 개의 열을 만들고 각 열에 6개씩 버튼을 배치해.
    button_col1, button_col2 = st.columns(2, gap="small")

    for index, color_name in enumerate(color_names):
        # 앞의 6개는 왼쪽 열, 나머지 6개는 오른쪽 열
        target_col = button_col1 if index < 6 else button_col2

        with target_col:
            # 색상 사각형은 이모지가 아니라 실제 색상 코드로 그려.
            # 버튼을 누르면 선택 색상이 변경돼.
            selected = st.session_state.selected_color == color_name

            if selected:
                label = f"✓ {color_name}"
            else:
                label = color_name

            # 버튼 클릭 시 선택한 색상을 기억해.
            if st.button(
                label,
                key=f"color_{color_name}",
                use_container_width=True,
                type="primary" if selected else "secondary"
            ):
                st.session_state.selected_color = color_name
                st.rerun()

            # 각 버튼의 바로 앞에 실제 색상 사각형을 표시해.
            # 색상은 버튼과 같은 순서로 대응해.
            st.markdown(
                f"""
                <style>
                
/* 색상 버튼 자체를 해당 색상으로 칠하기 */
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

/* 선택된 버튼은 테두리로 구분 */
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
    min-height: 48px;
}

                </style>
                """,
                unsafe_allow_html=True
            )

    # 색상표를 버튼 아래에 표시해 실제 색을 확인할 수 있도록 해.
    # 각 색상의 이름과 색깔을 6행 × 2열로 보여 줘.
    for row in range(6):
        swatch_cols = st.columns(2, gap="small")
        for col_index in range(2):
            color_name = color_names[row + col_index * 6]
            swatch_cols[col_index].markdown(
                f"""
                <div style="
                    display:flex;
                    align-items:center;
                    gap:6px;
                    margin:0 0 5px 2px;
                    font-size:12px;
                    color:#666;
                ">
                    <span style="
                        display:inline-block;
                        width:13px;
                        height:13px;
                        flex-shrink:0;
                        background:{colors[color_name]};
                        border:1px solid #888;
                        border-radius:3px;
                    "></span>
                    {color_name}
                </div>
                """,
                unsafe_allow_html=True
            )

# 선택한 색상과 해당 퍼슈트 정보를 불러와.
selected_color = st.session_state.selected_color
suits = fursuits.get(selected_color, [])

# ==========================================
# 9. 가운데: 퍼슈트 사진
# ==========================================

with center:
    st.markdown("#### 퍼슈트 사진")

    if suits:
        # 한 색상에 퍼슈트가 여러 개라면 선택할 수 있어.
        if len(suits) > 1:
            suit_names = [suit["name"] for suit in suits]
            selected_suit_name = st.selectbox(
                "퍼슈트 선택",
                suit_names,
                label_visibility="collapsed",
                key=f"suit_selector_{selected_color}"
            )
            suit = next(
                suit for suit in suits
                if suit["name"] == selected_suit_name
            )
        else:
            suit = suits[0]

        image_path = BASE_DIR / suit["image"]

        if image_path.is_file():
            # 이미지 원본의 비율을 유지하며 영역에 맞춰 표시해.
            # 세로 2:3 사진을 사용하면 가장 자연스럽게 보여.
            st.image(
                str(image_path),
                use_container_width=True
            )
        else:
            st.warning(
                "사진을 찾을 수 없어요.\n\n"
                f"확인할 경로: {suit['image']}"
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
        # 이름은 크게, 굵게 표시해.
        st.markdown(
            f'<div class="suit-name">{suit["name"]}</div>',
            unsafe_allow_html=True
        )

        # 선택한 색상 표시
        st.markdown(
            f"""
            <div style="
                display:inline-flex;
                align-items:center;
                gap:8px;
                padding:5px 10px;
                border:1px solid #dddddd;
                border-radius:20px;
                margin-bottom:12px;
                font-size:14px;
            ">
                <span style="
                    width:14px;
                    height:14px;
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

        # 퍼슈트 설명
        st.markdown("**소개**")
        st.markdown(
            f'<div class="suit-info">{suit["description"]}</div>',
            unsafe_allow_html=True
        )

        # 제작자 정보가 입력된 경우에만 표시해.
        if suit.get("maker"):
            st.markdown("**제작자**")
            st.write(suit["maker"])

        # 관련 홈페이지나 SNS 주소가 있다면 표시해.
        if suit.get("link"):
            st.markdown(f"[관련 링크 열기]({suit['link']})")

    else:
        st.markdown("### 등록된 정보가 없어요")
        st.write(
            "이 색상의 퍼슈트를 추가하려면 "
            "main.py의 퍼슈트 정보 부분을 수정해 주세요."
        )

# ==========================================
# 11. 페이지 아래쪽
# ==========================================
# 공간을 많이 차지하지 않도록 짧게 표시해.

st.caption("퍼슈트 컬러 도감")
