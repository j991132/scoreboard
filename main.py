import streamlit as st

# --- 페이지 설정 ---
st.set_page_config(layout="wide")

# --- 점수 초기화 (세션 상태 사용) ---
if 'red_score' not in st.session_state:
    st.session_state.red_score = 0
if 'blue_score' not in st.session_state:
    st.session_state.blue_score = 0

# --- 버튼 클릭 로직 처리 ---
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

# --- CSS와 HTML을 결합한 최종 코드 ---
# 보내주신 코드의 안정적인 flex 레이아웃을 기반으로 재구성했습니다.
FULL_HTML_CODE = f"""
<style>
    /* 기본 여백 제거 및 전체화면 설정 */
    body, html {{
        margin: 0;
        padding: 0;
        width: 100vw;
        height: 100vh;
        overflow: hidden;
    }}
    /* Streamlit 기본 UI 요소 숨기기 */
    #root > div:nth-child(1) > div > div > div > div > section > div {{
        padding: 0 !important;
    }}
    header, footer, #MainMenu {{
        visibility: hidden;
    }}
    /* 메인 컨테이너 (Flexbox 레이아웃) */
    .container {{
        display: flex;
        height: 100vh;
        width: 100vw;
        font-family: 'Arial Black', sans-serif;
        position: relative; /* 자식 absolute 요소들의 기준점 */
    }}
    /* 점수 패널 (왼쪽, 오른쪽) */
    .panel {{
        flex: 1; /* ★★★ 보내주신 코드의 핵심! 화면을 1:1로 나눔 ★★★ */
        display: flex;
        justify-content: center;
        align-items: center;
        color: white;
        font-size: 30vw;
        font-weight: 900;
        position: relative; /* 버튼 그룹의 기준점 */
        user-select: none;
    }}
    .red-panel {{ background-color: #E53935; }}
    .blue-panel {{ background-color: #1E88E5; }}

    /* 상단 작은 점수 (absolute 포지셔닝) */
    .top-score {{
        position: absolute;
        top: 2vh;
        left: 50%;
        transform: translateX(-50%);
        background-color: rgba(255, 255, 255, 0.2);
        padding: 5px 20px;
        border-radius: 10px;
        font-size: 5vw;
        color: white;
        display: flex;
        gap: 20px;
        z-index: 10;
    }}
    /* 버튼 그룹 (+, - 버튼) */
    .button-group {{
        position: absolute;
        bottom: 5vh;
        left: 50%;
        transform: translateX(-50%);
        display: flex;
        gap: 20px;
        z-index: 10;
    }}
    /* 리셋 버튼 */
    .reset-container {{
        position: absolute;
        bottom: 5vh;
        left: 50%;
        transform: translateX(-50%);
        z-index: 10;
    }}
    /* 버튼 공통 스타일 */
    .btn {{
        display: flex;
        justify-content: center;
        align-items: center;
        width: 70px;
        height: 70px;
        border: 3px solid white;
        border-radius: 50%;
        background-color: rgba(0, 0, 0, 0.2);
        color: white;
        font-size: 40px;
        text-decoration: none;
        transition: background-color 0.2s;
    }}
    .btn:hover {{ background-color: rgba(0, 0, 0, 0.4); }}
</style>

<div class="container">
    <div class="top-score">
        <span>0</span>
        <span>0</span>
    </div>

    <div class="reset-container">
        <a href="?action=reset" class="btn" target="_self">🔄</a>
    </div>

    <div class="panel red-panel">
        {st.session_state.red_score}
        <div class="button-group">
            <a href="?action=red_plus" class="btn" target="_self">+</a>
            <a href="?action=red_minus" class="btn" target="_self">-</a>
        </div>
    </div>

    <div class="panel blue-panel">
        {st.session_state.blue_score}
        <div class="button-group">
            <a href="?action=blue_plus" class="btn" target="_self">+</a>
            <a href="?action=blue_minus" class="btn" target="_self">-</a>
        </div>
    </div>
</div>
"""

# HTML 렌더링
st.markdown(FULL_HTML_CODE, unsafe_allow_html=True)
