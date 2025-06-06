import streamlit as st

# --- 페이지 설정 ---
st.set_page_config(layout="wide")

# --- 점수 초기화 (세션 상태 사용) ---
if 'red_score' not in st.session_state:
    st.session_state.red_score = 0
if 'blue_score' not in st.session_state:
    st.session_state.blue_score = 0

# --- 버튼 로직 처리 ---
query_params = st.query_params
if "action" in query_params:
    action = st.query_params.pop("action")
    if action == "red_plus":
        st.session_state.red_score += 1
    elif action == "red_minus":
        st.session_state.red_score = max(0, st.session_state.red_score - 1)
    elif action == "blue_plus":
        st.session_state.blue_score += 1
    elif action == "blue_minus":
        st.session_state.blue_score = max(0, st.session_state.blue_score - 1)
    elif action == "reset":
        st.session_state.red_score = 0
        st.session_state.blue_score = 0
    
    st.rerun()

# --- HTML 및 CSS 전체 코드 ---
FULL_HTML_CODE = f"""
<style>
    /* Streamlit의 메인 컨테이너에서 여백과 최대 너비를 강제로 제거합니다. */
    #root > div:nth-child(1) > div > div > div > div > section > div {{
        padding: 0rem !important;
        max-width: none !important;
    }}
    header, footer, #MainMenu {{ visibility: hidden; }}
    html, body, [class*="st-"] {{
        margin: 0; padding: 0; height: 100%; overflow: hidden;
    }}
    .scoreboard-container {{
        display: flex; height: 100vh; width: 100vw; position: relative;
    }}
    .panel {{
        width: 50vw !important; /* ★★★ 너비를 강제로 적용합니다 ★★★ */
        height: 100% !important; /* ★★★ 높이를 강제로 적용합니다 ★★★ */
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        font-family: 'Arial Black', sans-serif !important;
        font-weight: 900 !important;
        color: white !important;
        font-size: 30vw !important;
        line-height: 1 !important;
        position: relative !important;
        user-select: none !important;
    }}
    .red-panel {{ background-color: #E53935; }}
    .blue-panel {{ background-color: #1E88E5; }}
    .top-score, .button-group, .reset-container {{
        position: absolute !important;
        z-index: 10 !important;
    }}
    .top-score {{
        top: 2vh !important; left: 50% !important; transform: translateX(-50%) !important;
        background-color: rgba(255, 255, 255, 0.2) !important; padding: 5px 20px !important;
        border-radius: 10px !important; font-size: 5vw !important; display: flex !important; gap: 15px !important;
    }}
    .button-group, .reset-container {{
        bottom: 5vh !important; left: 50% !important; transform: translateX(-50%) !important;
    }}
    .btn {{
        display: flex !important; justify-content: center !important; align-items: center !important;
        width: 70px !important; height: 70px !important; border: 3px solid white !important;
        border-radius: 50% !important; background-color: rgba(0, 0, 0, 0.2) !important;
        color: white !important; font-size: 40px !important; text-decoration: none !important;
        transition: background-color 0.2s, transform 0.1s !important;
    }}
    .btn:hover {{ background-color: rgba(0, 0, 0, 0.4) !important; }}
    .btn:active {{ transform: scale(0.95) !important; }}
</style>

<div class="scoreboard-container">
    <div class="top-score">
        <span class="top-score-red">0</span>
        <span class="top-score-blue">0</span>
    </div>
    <div class="red-panel">
        {st.session_state.red_score}
        <div class="button-group">
            <a href="?action=red_plus" class="btn" target="_self">+</a>
            <a href="?action=red_minus" class="btn" target="_self">-</a>
        </div>
    </div>
    <div class="blue-panel">
        {st.session_state.blue_score}
        <div class="button-group">
            <a href="?action=blue_plus" class="btn" target="_self">+</a>
            <a href="?action=blue_minus" class="btn" target="_self">-</a>
        </div>
    </div>
    <div class="reset-container">
        <a href="?action=reset" class="btn" target="_self">🔄</a>
    </div>
</div>
"""

# --- 코드 렌더링 ---
st.markdown(FULL_HTML_CODE, unsafe_allow_html=True)
