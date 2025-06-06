import streamlit as st
import urllib.parse

# Streamlit 페이지 설정 (화면을 꽉 채우기 위해 넓게 설정)
st.set_page_config(layout="wide")

# 세션 상태 초기화 (점수 관리)
if 'red_score' not in st.session_state:
    st.session_state.red_score = 0
if 'blue_score' not in st.session_state:
    st.session_state.blue_score = 0
if 'red_set_score' not in st.session_state:
    st.session_state.red_set_score = 0
if 'blue_set_score' not in st.session_state:
    st.session_state.blue_set_score = 0

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

# 리셋 함수
def reset_scores():
    st.session_state.red_score = 0
    st.session_state.blue_score = 0
    st.session_state.red_set_score = 0
    st.session_state.blue_set_score = 0
    st.rerun()

# CSS 스타일 정의
st.markdown(f"""
    <style>
    /* Streamlit 기본 여백 제거 */
    .block-container {{
        padding-top: 0rem; padding-bottom: 0rem;
        padding-left: 0rem; padding-right: 0rem;
    }}
    .container {{
        display: flex; height: 80vh; /* 점수 영역 높이 */
        width: 100vw; margin: 0; padding: 0;
        font-family: Arial, sans-serif; position: relative;
        overflow: hidden; /* 스크롤 방지 */
    }}
    .left {{
        flex: 1; background-color: #FF0000; display: flex;
        flex-direction: column; justify-content: flex-start;
        align-items: center; color: white;
        font-size: clamp(20vh, 80vw, 80vh);
        font-weight: bold; position: relative;
        line-height: 1; padding-top: 2vh;
        max-height: 80vh;
    }}
    .right {{
        flex: 1; background-color: #0000FF; display: flex;
        flex-direction: column; justify-content: flex-start;
        align-items: center; color: white;
        font-size: clamp(20vh, 80vw, 80vh);
        font-weight: bold; position: relative;
        line-height: 1; padding-top: 2vh;
        max-height: 80vh;
    }}
    /* 세트 스코어 CSS */
    .set-score-left, .set-score-right {{
        position: absolute; top: clamp(0.5vh, 1vw, 2vh);
        background-color: rgba(255, 255, 255, 0.5);
        padding: clamp(0.2vh, 0.5vw, 1vh) clamp(0.5vw, 1vw, 2vh);
        font-size: clamp(5vh, 30vw, 40vh);
        font-weight: bold; color: black;
        line-height: 1;
    }}
    .set-score-left {{ right: clamp(1vw, 2vw, 3vh); }}
    .set-score-right {{ left: clamp(1vw, 2vw, 3vh); }}
    /* 버튼 스타일링 CSS */
    .fixed-button-container {{
        position: fixed; bottom: 0; left: 0;
        width: 100%; z-index: 100; display: flex;
        justify-content: center; gap: 1vw;
        padding: 0.5vh 5vw;
        background-color: transparent;
        height: 20vh;
    }}
    .stButton > button {{
        border: none; border-radius: 50%;
    width: clamp(4vw, 60px, 6vh);
    height: clamp(4vw, 60px, 6vh);
    box-shadow: 0 4px 12px rgba(0,0,0,0.4);
    background-color: white;
    font-size: clamp(2.5vw, 30px, 4vh); /* 텍스트 크기 증가 */
    font-weight: bold;
    color: black;
    text-align: center;
    overflow: visible;
    transition: transform 0.1s ease-in-out;
    cursor: pointer;
    }}
    .stButton > button:active {{ transform: scale(0.95); }}
    
    .plus-button .stButton > button {
    background-color: #8fdefd;
    font-size: clamp(2.5vw, 30px, 4vh); /* 텍스트 크기 증가 */
}
.plus-button .stButton > button:hover { background-color: #8fdefd; }

.minus-button .stButton > button {
    background-color: #fdb5b4;
    font-size: clamp(2.5vw, 30px, 4vh); /* 텍스트 크기 증가 */
}
.minus-button .stButton > button:hover { background-color: #fdb5b4; }

.reset-button .stButton > button {
    background-color: white;
    font-size: clamp(2.5vw, 30px, 4vh); /* 텍스트 크기 증가 */
}
.reset-button .stButton > button:hover { background-color: #f0f0f0; }
    
    div[data-testid="stHorizontalBlock"] > div:nth-child(1) {{
        display: flex; justify-content: flex-end; padding-right: 5vw;
    }}
    div[data-testid="stHorizontalBlock"] > div:nth-child(2) {{
        display: flex; justify-content: center;
    }}
    div[data-testid="stHorizontalBlock"] > div:nth-child(3) {{
        display: flex; justify-content: flex-start; padding-left: 5vw;
    }}
    /* 버튼 가로 정렬 */
    .button-row {{
        display: flex; justify-content: center; gap: 1vw;
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
with st.container():
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        st.markdown('<div class="button-row">', unsafe_allow_html=True)
        col_plus, col_minus = st.columns(2)
        with col_plus:
            st.button("+1", on_click=increment_red, key="red_plus")
        with col_minus:
            st.button("-1", on_click=decrement_red, key="red_minus")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.button("Reset", on_click=reset_scores, key="reset")

    with col3:
        st.markdown('<div class="button-row">', unsafe_allow_html=True)
        col_plus, col_minus = st.columns(2)
        with col_plus:
            st.button("+1", on_click=increment_blue, key="blue_plus")
        with col_minus:
            st.button("-1", on_click=decrement_blue, key="blue_minus")
        st.markdown('</div>', unsafe_allow_html=True)
