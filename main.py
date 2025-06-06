import streamlit as st

# Streamlit 페이지 설정 (화면을 꽉 채우기 위해 넓게 설정)
st.set_page_config(layout="wide")

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
st.markdown("""
    <style>
    /* Streamlit 기본 여백 제거 */
    .block-container {
        padding-top: 0rem;
        padding-bottom: 0rem;
        padding-left: 0rem;
        padding-right: 0rem;
    }
    .container {
        display: flex;
        height: 100vh;
        width: 100vw;
        margin: 0;
        padding: 0;
        font-family: Arial, sans-serif;
        position: relative;
    }
    .left {
        flex: 1;
        background-color: #FF0000;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        color: white;
        font-size: 80vh;
        font-weight: bold;
        position: relative;
        line-height: 1;
    }
    .right {
        flex: 1;
        background-color: #0000FF;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        color: white;
        font-size: 80vh;
        font-weight: bold;
        position: relative;
        line-height: 1;
    }
    /* --- ✨ 세트 스코어 CSS 수정 --- */
    .set-score-left {
        position: absolute;
        top: 20px;
        right: 20px;
        background-color: rgba(255, 255, 255, 0.5);
        padding: 10px 20px;
        font-size: 240px; /* 원래 크기로 복원 */
        font-weight: bold;
        color: black;
        line-height: 1; /* 텍스트가 잘리지 않도록 line-height 조정 */
    }
    .set-score-right {
        position: absolute;
        top: 20px;
        left: 20px;
        background-color: rgba(255, 255, 255, 0.5);
        padding: 10px 20px;
        font-size: 240px; /* 원래 크기로 복원 */
        font-weight: bold;
        color: black;
        line-height: 1; /* 텍스트가 잘리지 않도록 line-height 조정 */
    }
    
    /* --- ✨ 버튼 스타일링 CSS 추가 --- */
    /* 모든 버튼의 기본 스타일 */
    .stButton > button {
        background-color: white;
        color: transparent; /* 텍스트를 투명하게 처리하여 보이지 않게 함 */
        border: 3px solid black;
        border-radius: 50%; /* 원형 버튼 */
        cursor: pointer;
        width: 100px; /* 버튼 너비 */
        height: 100px; /* 버튼 높이 */
        box-shadow: 0 4px 8px rgba(0,0,0,0.3);
        background-repeat: no-repeat;
        background-position: center;
    }
    
    /* 플러스 버튼 아이콘 (SVG 사용) */
    .plus-button .stButton > button {
        background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" viewBox="0 0 24 24" fill="none" stroke="black" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>');
        background-size: 50% 50%;
    }
    
    /* 마이너스 버튼 아이콘 (SVG 사용) */
    .minus-button .stButton > button {
        background-image: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" viewBox="0 0 24 24" fill="none" stroke="black" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line></svg>');
        background-size: 50% 50%;
    }

    /* 버튼을 담을 컨테이너 스타일 (화면 하단에 고정) */
    .fixed-button-container {
        position: fixed;
        bottom: 40px;
        left: 0;
        width: 100%;
        z-index: 100;
    }
    
    /* 버튼 컬럼 내부 정렬 */
    div[data-testid="stHorizontalBlock"] > div:nth-child(1) {
        display: flex;
        justify-content: flex-end;
        padding-right: 5vw;
    }
    div[data-testid="stHorizontalBlock"] > div:nth-child(2) {
        display: flex;
        justify-content: flex-start;
        padding-left: 5vw;
    }
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

# --- ✨ 버튼 생성 로직 수정 ---

# 버튼을 화면 하단에 고정시키기 위한 컨테이너
st.markdown('<div class="fixed-button-container">', unsafe_allow_html=True)

# 버튼을 좌우로 나누기 위한 컬럼
col1, col2 = st.columns(2)

with col1:
    # 빨강팀 버튼을 한 행에 놓기 위한 내부 컬럼
    b1_col1, b1_col2 = st.columns(2)
    with b1_col1:
        st.markdown('<div class="plus-button">', unsafe_allow_html=True)
        st.button(" ", on_click=increment_red, key="red_plus")
        st.markdown('</div>', unsafe_allow_html=True)
    with b1_col2:
        st.markdown('<div class="minus-button">', unsafe_allow_html=True)
        st.button(" ", on_click=decrement_red, key="red_minus")
        st.markdown('</div>', unsafe_allow_html=True)

with col2:
    # 파랑팀 버튼을 한 행에 놓기 위한 내부 컬럼
    b2_col1, b2_col2 = st.columns(2)
    with b2_col1:
        st.markdown('<div class="plus-button">', unsafe_allow_html=True)
        st.button(" ", on_click=increment_blue, key="blue_plus")
        st.markdown('</div>', unsafe_allow_html=True)
    with b2_col2:
        st.markdown('<div class="minus-button">', unsafe_allow_html=True)
        st.button(" ", on_click=decrement_blue, key="blue_minus")
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
