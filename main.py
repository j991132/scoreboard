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
        display: flex; height: 100vh; width: 100vw;
        margin: 0; padding: 0; font-family: Arial, sans-serif;
        position: relative;
        overflow: hidden; /* 스크롤 방지 */
    }}
    .left {{
        flex: 1; background-color: #FF0000; display: flex;
        flex-direction: column; justify-content: center;
        align-items: center; color: white;
        font-size: clamp(5vh, 20vw, 25vh); /* 점수 크기 더 축소 */
        font-weight: bold; position: relative;
        line-height: 1; max-height: 70vh; /* 높이 제한 */
    }}
    .right {{
        flex: 1; background-color: #0000FF; display: flex;
        flex-direction: column; justify-content: center;
        align-items: center; color: white;
        font-size: clamp(5vh, 20vw, 25vh); /* 점수 크기 더 축소 */
        font-weight: bold; position: relative;
        line-height: 1; max-height: 70vh; /* 높이 제한 */
    }}
    /* 세트 스코어 CSS */
    .set-score-left, .set-score-right {{
        position: absolute; top: clamp(0.5vh, 1vw, 1.5vh); /* 상단 위치 조정 */
        background-color: rgba(255, 255, 255, 0.5);
        padding: clamp(0.1vh, 0.3vw, 0.5vh) clamp(0.3vw, 0.5vw, 1vh); /* 패딩 축소 */
        font-size: clamp(2vh, 10vw, 12vh); /* 세트 스코어 크기 더 축소 */
        font-weight: bold; color: black;
        line-height: 1;
    }}
    .set-score-left {{ right: clamp(1vw, 1.5vw, 2vh); }}
    .set-score-right {{ left: clamp(1vw, 1.5vw, 2vh); }}
    /* 버튼 스타일링 CSS */
    .fixed-button-container {{
        position: fixed; bottom: 1vh; left: 0;
        width: 100%; z-index: 100; display: flex;
        justify-content: center; gap: 1vw; /* 간격 축소 */
        padding: 0 5vw; /* 양쪽 여백 추가 */
    }}
    .stButton > button {{
        border: none; border-radius: 50%;
        width: clamp(4vw, 60px, 6vh); /* 버튼 크기 더 축소 */
        height: clamp(4vw, 60px, 6vh); /* 버튼 크기 더 축소 */
        box-shadow: 0 4px 12px rgba(0,0,0,0.4);
        background-color: white;
        font-size: clamp(1.5vw, 18px, 2.5vh); /* 텍스트 크기 조정 */
        font-weight: bold;
        color: black;
        text-align: center; /* 텍스트 중앙 정렬 */
        overflow: visible; /* 텍스트가 잘리지 않도록 */
        transition: transform 0.1s ease-in-out;
        cursor: pointer;
    }}
    .stButton > button:active {{ transform: scale(0.95); }}
    .plus-button .stButton > button {{
        background-color: white;
    }}
    .plus-button .stButton > button:hover {{ background-color: #f0f0f0; }}
    .minus-button .stButton > button {{
        background-color: white;
    }}
    .minus-button .stButton > button:hover {{ background-color: #f0f0f0; }}
    .reset-button .stButton > button {{
        background-color: white;
        font-size: clamp(1.2vw, 14px, 2vh); /* 리셋 버튼 텍스트 크기 조정 */
    }}
    .reset-button .stButton > button:hover {{ background-color: #f0f0f0; }}
    div[data-testid="stHorizontalBlock"] > div:nth-child(1) {{
        display: flex; justify-content: flex-end; padding-right: 2vw;
    }}
    div[data-testid="stHorizontalBlock"] > div:nth-child(2) {{
        display: flex; justify-content: center;
    }}
    div[data-testid="stHorizontalBlock"] > div:nth-child(3) {{
        display: flex; justify-content: flex-start; padding-left: 2vw;
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

# 버튼을 좌우 및 중앙으로 나누기 위한 컬럼
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    b1_col1, b1_col2 = st.columns(2)
    with b1_col1:
        st.markdown('<div class="plus-button">', unsafe_allow_html=True)
        st.button("+", on_click=increment_red, key="red_plus")
        st.markdown('</div>', unsafe_allow_html=True)
    with b1_col2:
        st.markdown('<div class="minus-button">', unsafe_allow_html=True)
        st.button("-", on_click=decrement_red, key="red_minus")
        st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="reset-button">', unsafe_allow_html=True)
    st.button("Reset", on_click=reset_scores, key="reset")
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    b2_col1, b2_col2 = st.columns(2)
    with b2_col1:
        st.markdown('<div class="plus-button">', unsafe_allow_html=True)
        st.button("+", on_click=increment_blue, key="blue_plus")
        st.markdown('</div>', unsafe_allow_html=True)
    with b2_col2:
        st.markdown('<div class="minus-button">', unsafe_allow_html=True)
        st.button("-", on_click=decrement_blue, key="blue_minus")
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
