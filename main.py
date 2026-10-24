
import streamlit as st
from pathlib import Path

# ==========================================
# 1. 웹사이트 기본 설정
# ==========================================

st.set_page_config(
    page_title="퍼슈트 컬러 도감",
    page_icon="🎨",
    layout="wide"  # 넓은 화면을 사용해 사진을 여러 개 나란히 표시
)

# 사진 폴더의 위치를 찾기 위한 기준 경로
BASE_DIR = Path(__file__).parent

st.title("🎨 퍼슈트 컬러 도감")
st.write("색상을 선택해 원하는 퍼슈트를 찾아보세요!")

# ==========================================
# 2. 색상 이름과 색상 표시 기호
# ==========================================
# 색상 이름 앞에 색깔이 있는 네모 이모지를 표시해.
# 이 기호들은 색상 선택 메뉴에 사용돼.

color_symbols = {
    "빨강": "🟥",
    "주황": "🟧",
    "노랑": "🟨",
    "초록": "🟩",
    "파랑": "🟦",
    "하늘색": "🩵",
    "보라": "🟪",
    "분홍": "🩷",
    "검정": "⬛",
    "회색": "🩶",
    "하양": "⬜",
    "갈색": "🟫",
}

# ==========================================
# 3. 퍼슈트 정보 입력하기
# ==========================================
# 사진은 images 폴더 안에 넣어 줘.
# image에는 폴더 이름과 사진 파일 이름을 입력해.
#
# name: 퍼슈트 이름
# image: 사진 파일 경로
# description: 퍼슈트 설명
# maker: 제작자 정보
# link: 관련 링크
#
# 아래 빨간색 예시를 네 정보로 바꾸면 돼.

fursuits = {
    "빨강": [
        {
            "name": "여기에 퍼슈트 이름 입력",
            "image": "images/red_example.jpg",
            "description": "여기에 퍼슈트의 특징을 입력하세요.",
            "maker": "",
            "link": ""
        }
    ],

    # 퍼슈트가 없는 색상은 빈 목록 []으로 남겨 둬.
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
# 4. 색상 선택 메뉴
# ==========================================
# 기존의 드롭다운 대신 색상 기호와 이름이 함께 보이는
# 선택 메뉴를 사용해.

st.subheader("🌈 색상 선택")

selected_color = st.radio(
    "보고 싶은 색상을 선택하세요.",
    options=list(fursuits.keys()),
    format_func=lambda color: f"{color_symbols[color]} {color}",
    horizontal=True,
    label_visibility="collapsed"
)

st.divider()

# 선택한 색상에 해당하는 퍼슈트 목록을 가져와.
selected_fursuits = fursuits[selected_color]

# ==========================================
# 5. 퍼슈트 사진과 정보 표시하기
# ==========================================
# 사진을 네 개씩 한 줄에 배치해.
# 사진 원본이 2:3 비율이면 그 비율을 유지하며 표시돼.
# 화면 너비에 따라 실제 크기는 달라질 수 있어.

if not selected_fursuits:
    st.info(
        f"아직 {selected_color} 색상의 퍼슈트가 등록되지 않았어요. "
        "main.py의 퍼슈트 정보 부분에 추가해 주세요."
    )

else:
    st.subheader(
        f"{color_symbols[selected_color]} {selected_color} 퍼슈트"
    )

    # 퍼슈트를 네 개씩 묶어 한 줄에 표시해.
    for start in range(0, len(selected_fursuits), 4):

        # 한 줄에 네 칸을 만들어.
        columns = st.columns(4)

        # 이번 줄에 표시할 퍼슈트만 가져와.
        row_fursuits = selected_fursuits[start:start + 4]

        for column, suit in zip(columns, row_fursuits):

            with column:
                # 사진 파일의 실제 경로
                image_path = BASE_DIR / suit["image"]

                # 사진이 존재하는지 확인한 뒤 표시해.
                if image_path.is_file():
                    st.image(
                        str(image_path),
                        use_container_width=True
                    )
                else:
                    st.warning(
                        f"사진을 찾을 수 없어요.\n"
                        f"파일 경로: {suit['image']}"
                    )

                # 사진 바로 아래에 퍼슈트 이름을 표시해.
                st.markdown(f"**{suit['name']}**")

                # 자세한 정보는 눌렀을 때 펼쳐지도록 해.
                # 이렇게 하면 사진과 이름을 한눈에 비교하기 쉬워.
                with st.expander("정보 보기"):
                    st.write("**소개**")
                    st.write(suit["description"])

                    # 입력된 경우에만 제작자 정보를 보여줘.
                    if suit.get("maker"):
                        st.write(f"**제작자:** {suit['maker']}")

                    # 링크가 입력된 경우에만 링크를 보여줘.
                    if suit.get("link"):
                        st.markdown(
                            f"[관련 링크 바로가기]({suit['link']})"
                        )

# ==========================================
# 6. 페이지 아래쪽 안내
# ==========================================

st.divider()
st.caption("퍼슈트 컬러 도감 | 퍼슈트 정보는 직접 등록할 수 있어요.")
