import streamlit as st

# 1. 페이지 설정 및 세션 상태 초기화
st.set_page_config(layout="wide")

if 'red_score' not in st.session_state:
    st.session_state.red_score = 0
if 'blue_score' not in st.session_state:
    st.session_state.blue_score = 0

# 2. 점수 변경 함수 (st.rerun()은 on_click 사용 시 불필요)
def increment_red():
    st.session_state.red_score += 1

def decrement_red():
    st.session_state.red_score = max(0, st.session_state.red_score - 1)

def increment_blue():
    st.session_state.blue_score += 1

def decrement_blue():
    st.session_state.blue_score = max(0, st.session_state.blue_score - 1)

# 3. CSS 스타일 정의
st.markdown("""
<style>
    /* Streamlit 기본 여백과 UI 제거 */
    .stApp {
        margin: 0;
        padding: 0;
    }
    #root > div:nth-child(1) > div > div > div > div > section {
        padding: 0;
    }
    header, footer, #MainMenu {
        visibility: hidden;
    }
    
    /* 컬럼을 감싸는 블록을 전체 화면으로 설정 */
    div[data-testid="stHorizontalBlock"] {
        height: 100vh;
        width: 100vw;
    }

    /* 각 점수판 컬럼(왼쪽, 오른쪽) 스타일 */
    div[data-testid="column"] {
        display: flex;
        flex-direction: column;
        justify-content: space-between; /* 점수는 위로, 버튼은 아래로 */
        height: 100%;
        color: white;
        text-align: center;
        user-select: none;
        padding: 4vh 2vw; /* 내부 여백 */
    }
    /* 첫 번째 컬럼(빨강) */
    div[data-testid="column"]:nth-of-type(1) {
        background-color: #FF0000;
    }
    /* 두 번째 컬럼(파랑) */
    div[data-testid="column"]:nth-of-type(2) {
        background-color: #0000FF;
    }

    /* 점수 텍스트 스타일 */
    .score-text {
        font-family: Arial, sans-serif;
        font-size: 35vw; /* 화면 너비에 비례하는 큰 폰트 */
        font-weight: bold;
        line-height: 1;
        flex-grow: 1; /* 남은 공간을 모두 차지하여 버튼을 아래로 밀어냄 */
        display: flex;
        justify-content: center;
        align-items: center;
    }

    /* 버튼 스타일 */
    .stButton>button {
        font-size: 40px;
        font-weight: bold;
        padding: 15px 30px;
        margin: 0 10px;
        background-color: rgba(255, 255, 255, 0.8);
        color: black;
        border: 2px solid white;
        border-radius: 10px;
        width: 100%; /* 컬럼 너비에 맞춤 */
    }
    .stButton>button:hover {
        background-color: white;
        color: black;
        border: 2px solid black;
    }
</style>
""", unsafe_allow_html=True)

# 4. Streamlit 컬럼으로 레이아웃 구성
col_red, col_blue = st.columns(2, gap="small")

# 왼쪽(빨강) 점수판
with col_red:
    # 점수 표시
    st.markdown(f'<div class="score-text">{st.session_state.red_score}</div>', unsafe_allow_html=True)
    
    # 점수 변경 버튼
    button_plus_red, button_minus_red = st.columns(2)
    with button_plus_red:
        st.button("+", on_click=increment_red, use_container_width=True, key="red_plus")
    with button_minus_red:
        st.button("-", on_click=decrement_red, use_container_width=True, key="red_minus")

# 오른쪽(파랑) 점수판
with col_blue:
    # 점수 표시
    st.markdown(f'<div class="score-text">{st.session_state.blue_score}</div>', unsafe_allow_html=True)

    # 점수 변경 버튼
    button_plus_blue, button_minus_blue = st.columns(2)
    with button_plus_blue:
        st.button("+", on_click=increment_blue, use_container_width=True, key="blue_plus")
    with button_minus_blue:
        st.button("-", on_click=decrement_blue, use_container_width=True, key="blue_minus")
