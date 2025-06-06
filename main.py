import streamlit as st
import urllib.parse

# Streamlit 페이지 설정 (화면을 꽉 채우기 위해 넓게 설정)
st.set_page_config(layout="wide")

# --- SVG 아이콘 이미지 (URL 인코딩 처리) ---
svg_plus_white = """
<svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
  <line x1="12" y1="5" x2="12" y2="19"></line>
  <line x1="5" y1="12" x2="19" y2="12"></line>
</svg>
"""
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
    }}
    .left {{
        flex: 1; background-color: #FF0000; display: flex;
        flex-direction: column; justify-content: center;
        align-items: center; color: white;
        font-size: clamp(20vh, 80vw, 80vh);
        font-weight: bold; position: relative;
        line-height: 1; min-height: 0;
    }}
    .right {{
        flex: 1; background-color: #0000FF; display: flex;
        flex-direction: column; justify-content: center;
        align-items: center; color: white;
        font-size: clamp(20vh, 80vw, 80vh);
        font-weight: bold; position: relative;
        line-height: 1; min-height: 0;
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
    .button-container {{
        display: flex; justify-content: center; gap: 2vw;
        margin-top: 2vh;
    }}
    .stButton > button {{
        color: transparent !important;
        border: none; border-radius: 50%;
        width: clamp(5vw, 100px, 10vh);
        height: clamp(5vw, 100px, 10vh);
        box-shadow: 0 4px 12px rgba(0,0,0,0.4);
        background-repeat: no-repeat; background-position: center;
        background-size: 50% 50%; transition: transform 0.1s ease-in-out;
        cursor: pointer;
    }}
    .stButton > button:active {{ transform: scale(0.95); }}
    .plus-button .stButton > button {{
        background-color: #4CAF50; background-image: url("{encoded_svg_plus}");
    }}
    .plus-button .stButton > button:hover {{ background-color: #45a049; }}
    .minus-button .stButton > button {{
        background-color: #D32F2F; background-image: url("{encoded_svg_minus}");
    }}
    .minus-button .stButton > button:hover {{ background-color: #C62828; }}
    </style>
""", unsafe_allow_html=True)

# 배경과 점수를 표시할 HTML 구조
st.markdown(f"""
    <div class="container">
        <div class="left">
            <div class="set-score-left">{st.session_state.red_set_score}</div>
            <div>{st.session_state.red_score}</div>
            <div class="button-container">
                <div class="plus-button">
                    {st.button(" ", on_click=increment_red, key="red_plus")}
                </div>
                <div class="minus-button">
                    {st.button(" ", on_click=decrement_red, key="red_minus")}
                </div>
            </div>
        </div>
        <div class="right">
            <div class="set-score-right">{st.session_state.blue_set_score}</div>
            <div>{st.session_state.blue_score}</div>
            <div class="button-container">
                <div class="plus-button">
                    {st.button(" ", on_click=increment_blue, key="blue_plus")}
                </div>
                <div class="minus-button">
                    {st.button(" ", on_click=decrement_blue, key="blue_minus")}
                </div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)
