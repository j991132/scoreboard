import streamlit as st

# Streamlit 페이지 설정 (화면을 꽉 채우기 위해 넓게 설정)
st.set_page_config(layout="wide")

# 세션 상태 초기화 (점수 관리)
if 'red_score' not in st.session_state:
    st.session_state.red_score = 0
if 'blue_score' not in st.session_state:
    st.session_state.blue_score = 0

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
# 기존 CSS는 그대로 유지합니다.
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
        font-size: 80vh; /* 버튼 공간 확보를 위해 폰트 크기 약간 줄임 */
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
        font-size: 80vh; /* 버튼 공간 확보를 위해 폰트 크기 약간 줄임 */
        font-weight: bold;
        position: relative;
        line-height: 1;
    }
    .set-score-left {
        position: absolute;
        top: 20px;
        right: 20px;
        background-color: rgba(255, 255, 255, 0.5);
        padding: 10px 20px;
        font-size: 24px; /* 가독성을 위해 폰트 크기 조정 */
        font-weight: bold;
        color: black;
    }
    .set-score-right {
        position: absolute;
        top: 20px;
        left: 20px;
        background-color: rgba(255, 255, 255, 0.5);
        padding: 10px 20px;
        font-size: 24px; /* 가독성을 위해 폰트 크기 조정 */
        font-weight: bold;
        color: black;
    }
    /* 버튼 스타일 */
    .stButton > button {
        font-size: 40px;
        padding: 15px 30px;
        margin: 0 10px;
        background-color: white;
        color: black;
        border: 2px solid black; /* 테두리 추가 */
        border-radius: 10px;
        cursor: pointer;
        width: 100px; /* 버튼 너비 고정 */
    }
    
    /* 버튼을 담을 컨테이너 스타일 (화면 하단에 고정) */
    .fixed-button-container {
        position: fixed; /* view port 기준으로 위치 고정 */
        bottom: 40px;    /* 하단에서 40px 위 */
        left: 0;
        width: 100%;
        z-index: 100;    /* 다른 요소들 위에 표시 */
    }
    /* 버튼 컬럼 내부 정렬 */
    div[data-testid="stHorizontalBlock"] > div:nth-child(1) {
        display: flex;
        justify-content: flex-end; /* 빨강 버튼을 오른쪽으로 */
        padding-right: 5vw;
    }
    div[data-testid="stHorizontalBlock"] > div:nth-child(2) {
        display: flex;
        justify-content: flex-start; /* 파랑 버튼을 왼쪽으로 */
        padding-left: 5vw;
    }
    </style>
""", unsafe_allow_html=True)

# 배경과 점수를 표시할 HTML 구조
st.markdown(f"""
    <div class="container">
        <div class="left">
            <div class="set-score-left">0</div>
            <div>{st.session_state.red_score}</div>
        </div>
        <div class="right">
            <div class="set-score-right">0</div>
            <div>{st.session_state.blue_score}</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- ✨ 변경된 부분 시작 ---

# 버튼을 화면 하단에 고정시키기 위한 컨테이너
st.markdown('<div class="fixed-button-container">', unsafe_allow_html=True)

# 버튼을 좌우로 나누기 위한 컬럼
col1, col2 = st.columns(2)

with col1:
    # 빨강팀 버튼을 한 행에 놓기 위한 내부 컬럼
    b1, b2 = st.columns(2)
    b1.button("+", on_click=increment_red, key="red_plus")
    b2.button("-", on_click=decrement_red, key="red_minus")

with col2:
    # 파랑팀 버튼을 한 행에 놓기 위한 내부 컬럼
    b3, b4 = st.columns(2)
    b3.button("+", on_click=increment_blue, key="blue_plus")
    b4.button("-", on_click=decrement_blue, key="blue_minus")

st.markdown('</div>', unsafe_allow_html=True)

# --- ✨ 변경된 부분 끝 ---
