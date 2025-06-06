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
    st.rerun()

def decrement_red():
    st.session_state.red_score = max(0, st.session_state.red_score - 1)
    st.rerun()

def increment_blue():
    st.session_state.blue_score += 1
    st.rerun()

def decrement_blue():
    st.session_state.blue_score = max(0, st.session_state.blue_score - 1)
    st.rerun()

# CSS 스타일 정의
st.markdown("""
    <style>
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
        font-size: 90vh;
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
        font-size: 90vh;
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
        font-size: 240px;
        font-weight: bold;
        color: black;
    }
    .set-score-right {
        position: absolute;
        top: 20px;
        left: 20px;
        background-color: rgba(255, 255, 255, 0.5);
        padding: 10px 20px;
        font-size: 240px;
        font-weight: bold;
        color: black;
    }
    .button-container {
        position: absolute;
        bottom: 20px;
        display: flex;
        justify-content: center;
        width: 100%;
    }
    .stButton > button {
        font-size: 40px;
        padding: 15px 30px;
        margin: 0 10px;
        background-color: white;
        color: black;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    </style>
""", unsafe_allow_html=True)

# HTML 구조와 버튼 구현
st.markdown(f"""
    <div class="container">
        <div class="left">
            <div class="set-score-left">0</div>
            <div>{st.session_state.red_score}</div>
            <div class="button-container"></div>
        </div>
        <div class="right">
            <div class="set-score-right">0</div>
            <div>{st.session_state.blue_score}</div>
            <div class="button-container"></div>
        </div>
    </div>
""", unsafe_allow_html=True)

# 버튼 콜백 처리
col1, col2 = st.columns(2)
with col1:
    if st.button("+", key="red_plus"):
        increment_red()
    if st.button("-", key="red_minus"):
        decrement_red()
with col2:
    if st.button("+", key="blue_plus"):
        increment_blue()
    if st.button("-", key="blue_minus"):
        decrement_blue()
