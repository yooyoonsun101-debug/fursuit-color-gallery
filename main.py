
import streamlit as st
from pathlib import Path

# ==========================================
# 1. 웹사이트 기본 설정
# ==========================================

# 웹사이트의 브라우저 탭 제목과 아이콘을 설정해.
st.set_page_config(
    page_title="퍼슈트 컬러 도감",
    page_icon="🎨",
    layout="wide"
)

# 웹사이트 제목과 안내 문구
st.title("🎨 퍼슈트 컬러 도감")
st.write("원하는 색상을 선택하고 해당 색상의 퍼슈트를 찾아보세요!")

# 현재 main.py 파일이 있는 폴더를 기준으로
# 사진 폴더의 위치를 찾도록 설정해.
BASE_DIR = Path(__file__).parent
IMAGE_DIR = BASE_DIR / "images"


# ==========================================
# 2. 퍼슈트 정보 입력하기
# ==========================================
# 아래 목록에 퍼슈트의 이름, 사진, 설명을 입력하면 돼.
#
# name: 퍼슈트 이름
# image: images 폴더 안에 있는 사진 파일 경로
# description: 퍼슈트에 대한 설명
# maker: 제작자 또는 제작 팀 (선택 사항)
# link: 관련 홈페이지나 SNS 주소 (선택 사항)
#
# 사진은 GitHub의 images 폴더에 올려야 해.
# 사진 파일 이름과 아래 경로가 정확히 일치해야 해.

fursuits = {
    "빨강": [
        {
            "name": "여기에 퍼슈트 이름 입력",
            "image": "images/il_794xN.7501864133_o83h.webp",
            "description": "여기에 퍼슈트의 특징이나 소개를 입력하세요.",
            "maker": "제작자 정보를 입력하세요.",
            "link": "https://www.etsy.com/listing/1699301493/complete-fursuit-custom-furry-full-suit?utm_source=chatgpt.com"
        }
    ],

    # 아직 등록하지 않은 색상은 빈 목록 []으로 두면 돼.
    # 퍼슈트가 생기면 빨강 부분과 같은 형식으로 입력해.
    "주황": [],
    "노랑": [],
    "초록": [],
    "연두색": [],
    "파랑": [],
    "하늘색": [],
    "보라": [],
    "분홍": [],
    "검정": [],
    "회색": [],
    "하양": [],
}


# ==========================================
# 3. 색상 선택 메뉴
# ==========================================
# 사용자가 고른 색상에 맞는 퍼슈트 목록을 보여줘.

selected_color = st.selectbox(
    "어떤 색상의 퍼슈트를 보고 싶나요?",
    options=list(fursuits.keys())
)

st.divider()

# 선택한 색상의 퍼슈트 목록을 가져와.
selected_fursuits = fursuits[selected_color]

# 해당 색상에 등록된 퍼슈트가 없을 때 보여주는 안내문
if not selected_fursuits:
    st.info(
        f"아직 {selected_color} 색상의 퍼슈트가 등록되지 않았어요. "
        "main.py의 해당 색상 목록에 퍼슈트 정보를 추가해 주세요."
    )

# ==========================================
# 4. 퍼슈트 사진과 정보 표시하기
# ==========================================
# 등록된 퍼슈트가 여러 개라면 각각의 정보를 차례대로 보여줘.

else:
    st.subheader(f"🌈 {selected_color} 퍼슈트")

    # 퍼슈트가 여러 개여도 하나씩 반복해서 표시해.
    for index, suit in enumerate(selected_fursuits):
        # 이름과 사진을 표시해.
        st.markdown(f"### {suit['name']}")

        # 사진 파일의 실제 위치를 확인해.
        image_path = BASE_DIR / suit["image"]

        # 사진 파일이 존재하면 사진을 보여줘.
        if image_path.is_file():
            st.image(
                str(image_path),
                caption=suit["name"],
                use_container_width=True
            )
        else:
            # 사진이 없거나 경로가 틀리면 오류 대신 안내문을 보여줘.
            st.warning(
                f"사진을 찾을 수 없어요: {suit['image']}\n\n"
                "images 폴더와 사진 파일 이름을 확인해 주세요."
            )

        # 퍼슈트 설명
        st.write("**소개**")
        st.write(suit["description"])

        # 제작자 정보
        if suit.get("maker"):
            st.write(f"**제작자:** {suit['maker']}")

        # 링크가 입력되어 있으면 클릭 가능한 링크로 표시해.
        if suit.get("link"):
            st.markdown(f"[관련 링크 바로가기]({suit['link']})")

        # 퍼슈트가 여러 개라면 구분선을 표시해.
        if index < len(selected_fursuits) - 1:
            st.divider()

# ==========================================
# 5. 페이지 아래쪽 안내 문구
# ==========================================

st.divider()
st.caption(
    "퍼슈트 정보는 사이트 관리자가 직접 등록한 자료입니다."
)
