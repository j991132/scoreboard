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
        margin: 0 !important; /* 추가: block-container 자체의 마진도 제거 */
    }}
    /* 기본 HTML 및 body 여백/패딩 제거 */
    html, body {{
        margin: 0 !important;
        padding: 0 !important;
        overflow: hidden !important; /* 스크롤바 방지 */
        width: 100vw;
        height: 100vh;
    }}

    /* --- ✨ 새로운 주 레이아웃 CSS --- */
    /* st.columns(2)로 생성된 최상위 가로 블록 */
    div[data-testid="stApp"] > div > div[data-testid="stHorizontalBlock"] {{
        display: flex !important;
        height: 100vh !important;
        width: 100vw !important; 
        padding: 0 !important;
        margin: 0 !important;
        position: absolute; /* 화면 전체를 덮도록 */
        top: 0;
        left: 0;
    }}

    /* 왼쪽 컬럼 (빨강팀) */
    /* st.columns(2)의 첫 번째 자식 div */
    div[data-testid="stApp"] > div > div[data-testid="stHorizontalBlock"] > div:nth-child(1) {{
        background-color: #FF0000;
        flex: 1;
        display: flex;
        flex-direction: column;
        justify-content: center; 
        align-items: center;    
        position: relative;     
        color: white;
        font-size: 75vh; /* 버튼과 세트스코어 공간 확보를 위해 약간 줄임 */
        font-weight: bold;
        line-height: 1;
        overflow: hidden; 
        padding: 0 !important; /* 내부 패딩 제거 */
        height: 100%; /* 부모의 100vh를 따름 */
    }}

    /* 오른쪽 컬럼 (파랑팀) */
    /* st.columns(2)의 두 번째 자식 div */
    div[data-testid="stApp"] > div > div[data-testid="stHorizontalBlock"] > div:nth-child(2) {{
        background-color: #0000FF;
        flex: 1;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        position: relative;
        color: white;
        font-size: 75vh; /* 버튼과 세트스코어 공간 확보를 위해 약간 줄임 */
        font-weight: bold;
        line-height: 1;
        overflow: hidden;
        padding: 0 !important; /* 내부 패딩 제거 */
        height: 100%; /* 부모의 100vh를 따름 */
    }}
    
    /* 세트 스코어 표시 */
    .set-score-display {{
        position: absolute;
        top: 20px; 
        background-color: rgba(255, 255, 255, 0.6); /* 배경 약간 더 불투명하게 */
        padding: 10px 20px; 
        font-size: 180px; /* 크기 재조정 */
        font-weight: bold;
        color: black;
        line-height: 1; 
        z-index: 10; 
        border-radius: 15px; /* 모서리 둥글게 */
    }}
    .set-score-left-team {{ right: 30px; }} /* 빨강팀 영역 내 오른쪽 상단 */
    .set-score-right-team {{ left: 30px; }} /* 파랑팀 영역 내 왼쪽 상단 */

    /* 메인 스코어 (큰 숫자) */
    .main-score-display {{
        /* 폰트 스타일은 부모 컬럼에서 상속, 필요시 추가 스타일링 */
        text-align: center; /* 확실한 중앙 정렬 */
    }}
    
    /* 각 팀의 버튼들을 감싸는 래퍼 */
    .team-buttons-wrapper {{
        position: absolute;
        bottom: 30px; /* 하단 여백 조정 */
        left: 0;      /* 부모 컬럼의 왼쪽 끝에서 시작 */
        width: 100%;  /* 부모 컬럼의 전체 너비 */
        display: flex;
        justify-content: center; /* 내부 버튼 쌍을 수평 중앙 정렬 */
        z-index: 20;
    }}
    
    /* 버튼 쌍(+, -)을 담고 있는 내부 st.columns로 생성된 가로 블록 */
    .team-buttons-wrapper > div[data-testid="stHorizontalBlock"] {{
        display: flex !important;
        justify-content: center !important; 
        align-items: center !important;
        gap: 25px !important; /* 버튼 사이 간격 조정 */
        width: auto !important; 
        height: auto !important; /* 중요: 부모의 100vh 높이 상속 방지 */
        background-color: transparent !important; /* 중요: 부모 배경색 상속 방지 */
        padding: 0 !important;
        margin: 0 !important;
        border: none !important; /* 혹시 모를 테두리 제거 */
    }}

    /* --- 개별 버튼 스타일링 (이전과 동일) --- */
    div[data-testid="stButton"] > button {{ 
        color: transparent !important; 
        border: none !important;
        border-radius: 50% !important; 
        width: 90px !important; /* 버튼 크기 약간 줄임 */
        height: 90px !important; 
        box-shadow: 0 5px 15px rgba(0,0,0,0.35) !important; /* 그림자 강조 */
        background-repeat: no-repeat !important;
        background-position: center !important;
        background-size: 45% 45% !important; /* 아이콘 크기 조정 */
        transition: transform 0.1s ease-in-out, box-shadow 0.1s ease-in-out !important;
        padding: 0 !important; 
        cursor: pointer !important;
    }}
    div[data-testid="stButton"] > button:active {{
        transform: scale(0.93) !important; 
        box-shadow: 0 2px 8px rgba(0,0,0,0.3) !important;
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
    .plus-button, .minus-button {{ 
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
    }}
    
    </style>
""", unsafe_allow_html=True)

# --- ✨ Python 로직 (주 레이아웃 변경) ---
# 화면을 좌우로 나누는 기본 컬럼 생성
# 이 컬럼들이 각각 빨강/파랑 영역이 됨
col_red_area, col_blue_area = st.columns(2)

with col_red_area: # 빨강팀 영역
    # 세트 스코어 (HTML로 생성하여 CSS로 위치 지정)
    st.markdown(f'<div class="set-score-display set-score-left-team">{st.session_state.red_set_score}</div>', unsafe_allow_html=True)
    
    # 메인 스코어 (HTML로 생성, 부모 컬럼의 flex 속성으로 중앙 정렬)
    st.markdown(f'<div class="main-score-display">{st.session_state.red_score}</div>', unsafe_allow_html=True)
    
    # 버튼 래퍼 (HTML로 생성하여 CSS로 위치 지정)
    st.markdown('<div class="team-buttons-wrapper">', unsafe_allow_html=True)
    # 실제 버튼은 Streamlit 위젯으로 생성
    btn_cols_red_plus, btn_cols_red_minus = st.columns([1,1]) 
    with btn_cols_red_plus:
        st.markdown('<div class="plus-button">', unsafe_allow_html=True)
        # 버튼 key 값 변경 (이전 실행과의 충돌 방지)
        st.button(" ", on_click=increment_red, key="red_plus_area_v2") 
        st.markdown('</div>', unsafe_allow_html=True)
    with btn_cols_red_minus:
        st.markdown('<div class="minus-button">', unsafe_allow_html=True)
        st.button(" ", on_click=decrement_red, key="red_minus_area_v2")
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True) # team-buttons-wrapper 닫기

with col_blue_area: # 파랑팀 영역
    st.markdown(f'<div class="set-score-display set-score-right-team">{st.session_state.blue_set_score}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="main-score-display">{st.session_state.blue_score}</div>', unsafe_allow_html=True)

    st.markdown('<div class="team-buttons-wrapper">', unsafe_allow_html=True)
    btn_cols_blue_plus, btn_cols_blue_minus = st.columns([1,1])
    with btn_cols_blue_plus:
        st.markdown('<div class="plus-button">', unsafe_allow_html=True)
        st.button(" ", on_click=increment_blue, key="blue_plus_area_v2")
        st.markdown('</div>', unsafe_allow_html=True)
    with btn_cols_blue_minus:
        st.markdown('<div class="minus-button">', unsafe_allow_html=True)
        st.button(" ", on_click=decrement_blue, key="blue_minus_area_v2")
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True) # team-buttons-wrapper 닫기
