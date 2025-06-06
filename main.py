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
        overflow: hidden !important; /* 스크롤바 방지 */
    }}
    .container {{
        display: flex; height: 100vh; width: 100vw;
        margin: 0; padding: 0; font-family: Arial, sans-serif; position: relative; /* 부모 컨테이너가 relative여야 자식 absolute가 제대로 동작 */
    }}
    .left {{
        flex: 1; background-color: #FF0000; display: flex; flex-direction: column;
        justify-content: center; align-items: center; color: white;
        font-size: 80vh; font-weight: bold; position: relative; line-height: 1; /* 자식 absolute 요소의 기준점 */
    }}
    .right {{
        flex: 1; background-color: #0000FF; display: flex; flex-direction: column;
        justify-content: center; align-items: center; color: white;
        font-size: 80vh; font-weight: bold; position: relative; line-height: 1; /* 자식 absolute 요소의 기준점 */
    }}
    
    .set-score-left, .set-score-right {{
        position: absolute;
        top: 10px; 
        background-color: rgba(255, 255, 255, 0.5);
        padding: 5px 10px; 
        font-size: 480px; 
        font-weight: bold;
        color: black;
        line-height: 0.9; 
        z-index: 10; 
    }}
    .set-score-left {{ right: 20px; }}
    .set-score-right {{ left: 20px; }}
    
    /* --- 버튼 스타일링 CSS (개별 버튼 모양) --- */
    div[data-testid="stButton"] > button {{ 
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
        padding: 0 !important; 
        cursor: pointer !important;
    }}
    div[data-testid="stButton"] > button:active {{
        transform: scale(0.95) !important; 
    }}
    .plus-button div[data-testid="stButton"] > button {{ 
        background-color: #4CAF50 !important; 
        background-image: url("{encoded_svg_plus}") !important;
    }}
    .plus-button div[data-testid="stButton"] > button:hover {{
        background-color: #45a049 !important;
    }}
    .minus-button div[data-testid="stButton"] > button {{ 
        background-color: #D32F2F !important; 
        background-image: url("{encoded_svg_minus}") !important;
    }}
    .minus-button div[data-testid="stButton"] > button:hover {{
        background-color: #C62828 !important;
    }}
    .plus-button, .minus-button {{ /* 이 div들은 Streamlit 버튼 위젯을 직접 감싸고 있음 */
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
    }}

    /* --- ✨ 새로운 버튼 컨테이너 및 위치 지정 CSS --- */
    .red-team-buttons-css-wrapper {{
        position: absolute; /* .left 또는 .container 기준 (여기서는 .container 기준이 될 가능성이 높음) */
        bottom: 40px;       /* 화면 하단으로부터의 거리 */
        left: 0;            /* 화면 왼쪽 가장자리 */
        width: 50vw;        /* 왼쪽 영역(화면의 절반)을 차지 */
        display: flex;
        justify-content: center; /* 내부 버튼 쌍을 이 영역 내에서 중앙 정렬 */
        z-index: 20; /* 다른 요소들 위에 오도록 */
    }}

    .blue-team-buttons-css-wrapper {{
        position: absolute;
        bottom: 40px;
        right: 0;           /* 화면 오른쪽 가장자리 */
        width: 50vw;        /* 오른쪽 영역(화면의 절반)을 차지 */
        display: flex;
        justify-content: center;
        z-index: 20;
    }}

    /* 각 팀의 버튼 쌍 (+, -)을 담는 내부 컬럼 컨테이너 스타일 */
    /* st.columns([1,1])에 의해 생성된 div[data-testid="stHorizontalBlock"] 대상 */
    .red-team-buttons-css-wrapper > div[data-testid="stHorizontalBlock"],
    .blue-team-buttons-css-wrapper > div[data-testid="stHorizontalBlock"] {{
        display: flex !important;
        justify-content: center !important; /* 버튼 쌍(+,-)을 그들의 컨테이너 내에서 중앙 정렬 */
        align-items: center !important;
        gap: 20px !important; /* 버튼 사이의 간격을 20px로 늘림 */
        width: auto !important; /* 컨텐츠(버튼 두 개 + gap)에 맞게 너비 자동 조정 */
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


# --- ✨ 버튼 생성 로직 변경 ---
# 빨강팀 버튼 영역
# st.container()는 DOM에서 다음 사용 가능한 위치에 렌더링됩니다.
# CSS의 absolute positioning이 이 컨테이너들을 시각적으로 재배치합니다.
red_buttons_container = st.container()
with red_buttons_container:
    # 이 div가 CSS에 의해 절대 위치로 지정됩니다.
    st.markdown('<div class="red-team-buttons-css-wrapper">', unsafe_allow_html=True)
    # 내부 컬럼으로 버튼 쌍 배치
    r_b1, r_b2 = st.columns([1,1]) 
    with r_b1:
        st.markdown('<div class="plus-button">', unsafe_allow_html=True)
        st.button(" ", on_click=increment_red, key="red_plus_abs") 
        st.markdown('</div>', unsafe_allow_html=True)
    with r_b2:
        st.markdown('<div class="minus-button">', unsafe_allow_html=True)
        st.button(" ", on_click=decrement_red, key="red_minus_abs")
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True) # red-team-buttons-css-wrapper 닫기

# 파랑팀 버튼 영역
blue_buttons_container = st.container()
with blue_buttons_container:
    st.markdown('<div class="blue-team-buttons-css-wrapper">', unsafe_allow_html=True)
    b_b1, b_b2 = st.columns([1,1])
    with b_b1:
        st.markdown('<div class="plus-button">', unsafe_allow_html=True)
        st.button(" ", on_click=increment_blue, key="blue_plus_abs")
        st.markdown('</div>', unsafe_allow_html=True)
    with b_b2:
        st.markdown('<div class="minus-button">', unsafe_allow_html=True)
        st.button(" ", on_click=decrement_blue, key="blue_minus_abs")
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True) # blue-team-buttons-css-wrapper 닫기
