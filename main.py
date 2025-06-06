import streamlit as st
import urllib.parse

# Streamlit 페이지 설정 (화면을 꽉 채우기 위해 넓게 설정)
st.set_page_config(layout="wide")

# --- SVG 아이콘 이미지 (URL 인코딩 처리) ---
# 흰색 플러스(+) 아이콘 SVG 코드
svg_plus_white = """
<svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
  <line x1="12" y1="5" x2="12" y2="19"></line>
  <line x1="5" y1="12" x2="19" y2="12"></line>
</svg>
"""
# 흰색 마이너스(-) 아이콘 SVG 코드
svg_minus_white = """
<svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
  <line x1="5" y1="12" x2="19" y2="12"></line>
</svg>
"""

# SVG 코드를 Data URI 형식으로 변환 (URL 인코딩 포함)
encoded_svg_plus = f"data:image/svg+xml,{urllib.parse.quote(svg_plus_white)}"
encoded_svg_minus = f"data:image/svg+xml,{urllib.parse.quote(svg_minus_white)}"


# 세션 상태 초기화 (점수 관리)
if 'red_score' not in st.session_state:
    st.session_state.red_score = 0
if 'blue_score' not in st.session_state:
    st.session_state.blue_score = 0
# 세션 상태 초기화 (세트 스코어)
if 'red_set_score' not in st.session_state:
    st.session_state.red_set_score = 0
if 'blue_set_score' not in st.session_state:
    st.session_state.blue_set_score = 0

# 점수 증가/감소 함수
def increment_red():
    st.session_state.red_score += 1

def decrement_red():
    st.session_state.red_score = max(0, st.session_state.red_score - 1)

def increment_blue():
    st.session_state.blue_score += 1

def decrement_blue():
    st.session_state.blue_score = max(0, st.session_state.blue_score - 1)

# CSS 스타일 정의
st.markdown(f"""
    <style>
    /* Streamlit 기본 여백 제거 */
    .block-container {{
        padding-top: 0rem !important; 
        padding-bottom: 0rem !important;
        padding-left: 0rem !important; 
        padding-right: 0rem !important;
    }}
    /* 기본 HTML 및 body 여백/패딩 제거 */
    html, body {{
        margin: 0 !important;
        padding: 0 !important;
        overflow: hidden; /* 스크롤바 방지 */
    }}
    .container {{
        display: flex; height: 100vh; width: 100vw;
        margin: 0; padding: 0; font-family: Arial, sans-serif; position: relative;
    }}
    .left {{
        flex: 1; background-color: #FF0000; display: flex; flex-direction: column;
        justify-content: center; align-items: center; color: white;
        font-size: 80vh; font-weight: bold; position: relative; line-height: 1;
    }}
    .right {{
        flex: 1; background-color: #0000FF; display: flex; flex-direction: column;
        justify-content: center; align-items: center; color: white;
        font-size: 80vh; font-weight: bold; position: relative; line-height: 1;
    }}
    
    .set-score-left, .set-score-right {{
        position: absolute;
        top: 10px; /* 기존 20px에서 조정하여 잘리지 않도록 */
        background-color: rgba(255, 255, 255, 0.5);
        padding: 5px 10px; /* 패딩 약간 줄임 */
        font-size: 480px; 
        font-weight: bold;
        color: black;
        line-height: 0.9; /* 글자 크기에 맞게 line-height 조정 */
        z-index: 10; /* 다른 요소 위에 표시되도록 z-index 추가 */
    }}
    .set-score-left {{ right: 20px; }}
    .set-score-right {{ left: 20px; }}
    
    /* --- ✨ 버튼 스타일링 CSS 수정 --- */
    /* 모든 버튼의 공통 스타일 */
    div[data-testid="stButton"] > button {{ /* UPDATED SELECTOR */
        color: transparent !important; 
        border: none !important;
        border-radius: 50% !important; 
        width: 100px !important; 
        height: 100px !important; 
        box-shadow: 0 4px 12px rgba(0,0,0,0.4) !important;
        background-repeat: no-repeat !important;
        background-position: center !important;
        background-size: 50% 50% !important;
        transition: transform 0.1s ease-in-out !important;
        padding: 0 !important; /* Streamlit 기본 패딩 제거 */
    }}
    div[data-testid="stButton"] > button:active {{
        transform: scale(0.95) !important; 
    }}

    /* 플러스(+) 버튼: 초록색 배경, 흰색 아이콘 */
    .plus-button div[data-testid="stButton"] > button {{ /* UPDATED SELECTOR */
        background-color: #4CAF50 !important; 
        background-image: url("{encoded_svg_plus}") !important;
    }}
    .plus-button div[data-testid="stButton"] > button:hover {{
        background-color: #45a049 !important;
    }}
    
    /* 마이너스(-) 버튼: 빨간색 배경, 흰색 아이콘 */
    .minus-button div[data-testid="stButton"] > button {{ /* UPDATED SELECTOR */
        background-color: #D32F2F !important; 
        background-image: url("{encoded_svg_minus}") !important;
    }}
    .minus-button div[data-testid="stButton"] > button:hover {{
        background-color: #C62828 !important;
    }}

    .fixed-button-container {{
        position: fixed; bottom: 40px; left: 0;
        width: 100%; z-index: 100;
    }}
    
    /* 버튼 컬럼 내부 정렬 수정 */
    .fixed-button-container > div[data-testid="stHorizontalBlock"] > div {{
        display: flex;
        justify-content: center; /* 각 팀 버튼 그룹을 중앙 정렬 */
    }}
    .fixed-button-container > div[data-testid="stHorizontalBlock"] > div:nth-child(1) .stButton {{
         margin-right: 10px; /* 빨강팀 플러스/마이너스 버튼 사이 간격 */
    }}
     .fixed-button-container > div[data-testid="stHorizontalBlock"] > div:nth-child(2) .stButton {{
         margin-left: 10px; /* 파랑팀 플러스/마이너스 버튼 사이 간격 */
    }}

    /* 내부 컬럼 버튼 정렬 */
    .fixed-button-container .stButton {{ /* 모든 버튼에 적용될 수 있도록 */
        display: flex;
        justify-content: center;
        align-items: center;
    }}

    </style>
""", unsafe_allow_html=True)

# 배경과 점수를 표시할 HTML 구조
st.markdown(f"""
    <div class="container">
        <div class="left">
            <div class="set-score-left">{st.session_state.red_set_score}</div>
            <div>{st.session_state.red_score}</div>
        </div>
        <div class="right">
            <div class="set-score-right">{st.session_state.blue_set_score}</div>
            <div>{st.session_state.blue_score}</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# 버튼을 화면 하단에 고정시키기 위한 컨테이너
st.markdown('<div class="fixed-button-container">', unsafe_allow_html=True)

# 버튼을 좌우로 나누기 위한 컬럼
col1, col2 = st.columns(2)

with col1:
    # 빨강팀 버튼을 한 행에 놓기 위한 내부 컬럼 (Streamlit 컬럼 대신 HTML/CSS로 정렬 고려)
    # 각 버튼을 plus-button 또는 minus-button div로 감싸서 CSS 적용
    r_b1, r_b2 = st.columns([1,1]) # 내부 컬럼 비율 동일하게
    with r_b1:
        st.markdown('<div class="plus-button" style="display: flex; justify-content: flex-end; padding-right: 5px;">', unsafe_allow_html=True)
        st.button(" ", on_click=increment_red, key="red_plus_new") # Key 변경으로 이전 상태와 충돌 방지
        st.markdown('</div>', unsafe_allow_html=True)
    with r_b2:
        st.markdown('<div class="minus-button" style="display: flex; justify-content: flex-start; padding-left: 5px;">', unsafe_allow_html=True)
        st.button(" ", on_click=decrement_red, key="red_minus_new")
        st.markdown('</div>', unsafe_allow_html=True)

with col2:
    # 파랑팀 버튼
    b_b1, b_b2 = st.columns([1,1])
    with b_b1:
        st.markdown('<div class="plus-button" style="display: flex; justify-content: flex-end; padding-right: 5px;">', unsafe_allow_html=True)
        st.button(" ", on_click=increment_blue, key="blue_plus_new")
        st.markdown('</div>', unsafe_allow_html=True)
    with b_b2:
        st.markdown('<div class="minus-button" style="display: flex; justify-content: flex-start; padding-left: 5px;">', unsafe_allow_html=True)
        st.button(" ", on_click=decrement_blue, key="blue_minus_new")
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
