import streamlit as st

# --- 1. 페이지 설정 및 상태 초기화 ---
st.set_page_config(layout="wide")

if 'red_score' not in st.session_state:
    st.session_state.red_score = 0
if 'blue_score' not in st.session_state:
    st.session_state.blue_score = 0

# --- 2. 버튼 클릭 처리 로직 (이 부분은 변경 없음) ---
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

# --- 3. CSS와 HTML을 결합한 최종 코드 ---
FULL_HTML_CODE = f"""
<style>
    /* 기본 여백 제거 및 전체화면 설정 */
    body, html, #root {{
        margin: 0; padding: 0; width: 100vw; height: 100vh; overflow: hidden;
    }}
    /* Streamlit 기본 UI 숨기기 */
    header, footer, #MainMenu {{ visibility: hidden; }}
    div[data-testid="stAppViewContainer"] {{ background: none; }}
    section[data-testid="stSidebar"] {{ display: none; }}
    div[data-testid="stToolbar"] {{ display: none; }}
    
    /* 메인 컨테이너 (Flexbox 레이아웃, 자식 absolute 요소들의 기준점) */
    .container {{
        display: flex; height: 100vh; width: 100%;
        font-family: 'Arial Black', sans-serif; position: relative;
    }}
    /* 점수 패널 (flex: 1로 화면을 1:1 분할) */
    .panel {{
        flex: 1; display: flex; justify-content: center; align-items: center;
        color: white; font-size: 30vw; font-weight: 900;
        position: relative; /* 버튼 그룹의 기준점 */
        user-select: none;
    }}
    .red-panel {{ background-color: #E53935; }}
    .blue-panel {{ background-color: #1E88E5; }}

    /* 버튼 그룹 (+, - 버튼). 각 패널의 하단 중앙에 배치 */
    .button-group {{
        position: absolute; bottom: 5vh; left: 50%;
        transform: translateX(-50%); display: flex; gap: 20px; z-index: 10;
    }}
    /* 리셋 버튼. 전체 컨테이너의 하단 중앙에 배치 */
    .reset-container {{
        position: absolute; bottom: 5vh; left: 50%;
        transform: translateX(-50%); z-index: 20; /* 버튼 그룹보다 위에 표시 */
    }}
    /* 버튼 공통 스타일 */
    .btn {{
        display: flex; justify-content: center; align-items: center;
        width: 70px; height: 70px; border: 3px solid white; border-radius: 50%;
        background-color: rgba(0, 0, 0, 0.2); color: white;
        font-size: 40px; text-decoration: none; cursor: pointer;
        transition: background-color 0.2s;
    }}
    .btn:hover {{ background-color: rgba(0, 0, 0, 0.4); }}
</style>

<div class="container">
    <div class="reset-container">
        <div class="btn" onclick="window.location.href='?action=reset'">🔄</div>
    </div>

    <div class="panel red-panel">
        {st.session_state.red_score}
        <div class="button-group">
            <div class="btn" onclick="window.location.href='?action=red_plus'">+</div>
            <div class="btn" onclick="window.location.href='?action=red_minus'">-</div>
        </div>
    </div>

    <div class="panel blue-panel">
        {st.session_state.blue_score}
        <div class="button-group">
            <div class="btn" onclick="window.location.href='?action=blue_plus'">+</div>
            <div class="btn" onclick="window.location.href='?action=blue_minus'">-</div>
        </div>
    </div>
</div>
"""

# --- 4. HTML 렌더링 ---
st.markdown(FULL_HTML_CODE, unsafe_allow_html=True)
