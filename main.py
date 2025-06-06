import streamlit as st

# --- 페이지 설정 ---
st.set_page_config(layout="wide")

# --- 점수 초기화 (세션 상태 사용) ---
if 'red_score' not in st.session_state:
    st.session_state.red_score = 0
if 'blue_score' not in st.session_state:
    st.session_state.blue_score = 0

# --- 버튼 로직 처리 ---
# URL 쿼리 파라미터를 사용하여 버튼 클릭을 감지하고 처리합니다.
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
    
    # 처리 후 앱을 다시 실행하여 점수를 즉시 업데이트합니다.
    st.rerun()

# --- HTML 및 CSS 스타일 ---
html_code = f"""
<style>
    /* Streamlit 기본 UI 요소 숨기기 */
    #root > div:nth-child(1) > div > div > div > div > section > div {{
        padding-top: 0rem;
        padding-right: 1rem;
        padding-bottom: 0rem;
        padding-left: 1rem;
    }}
    header, footer, #MainMenu {{
        visibility: hidden;
    }}
    /* 전체 화면을 채우도록 설정 */
    html, body, [class*="st-"] {{
        margin: 0;
        padding: 0;
        height: 100%;
        overflow: hidden; /* 스크롤바 숨기기 */
    }}
    .scoreboard-container {{
        display: flex;
        height: 100vh;
        width: 100vw;
        position: relative; /* 리셋 버튼의 기준점 */
    }}
    /* 점수 패널 스타일 */
    .panel {{
        width: 50%;
        height: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
        font-family: 'Arial Black', sans-serif;
        font-weight: 900;
        color: white;
        font-size: 30vw; /* 뷰포트 너비에 비례하는 폰트 크기 */
        line-height: 1;
        position: relative; /* +/- 버튼의 기준점 */
        user-select: none; /* 텍스트 선택 방지 */
    }}
    .red-panel {{ background-color: #E53935; }}
    .blue-panel {{ background-color: #1E88E5; }}

    /* 상단 작은 점수 (원본 이미지 참고) */
    .top-score {{
        position: absolute;
        top: 2vh;
        left: 50%;
        transform: translateX(-50%);
        background-color: rgba(255, 255, 255, 0.2);
        padding: 5px 20px;
        border-radius: 10px;
        font-size: 5vw;
        display: flex;
        gap: 15px;
    }}
    .top-score-red {{ color: #FFCDD2; }}
    .top-score-blue {{ color: #BBDEFB; }}

    /* 버튼 그룹 스타일 */
    .button-group {{
        position: absolute;
        bottom: 5vh;
        left: 50%;
        transform: translateX(-50%);
        display: flex;
        gap: 20px;
        z-index: 10;
    }}
    /* 리셋 버튼 컨테이너 스타일 */
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
        transition: background-color 0.2s, transform 0.1s;
    }}
    .btn:hover {{
        background-color: rgba(0, 0, 0, 0.4);
    }}
    .btn:active {{
        transform: scale(0.95);
    }}
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

# HTML 렌더링 (가장 중요한 부분)
# unsafe_allow_html=True 옵션을 추가해야 HTML이 정상적으로 표시됩니다.
st.markdown(html_code, unsafe_allow_html=True)
