import streamlit as st

# --- 페이지 설정 ---
st.set_page_config(layout="wide")

# --- CSS 스타일 정의 ---
CSS_CODE = """
<style>
    /* Streamlit 기본 UI 요소 숨기기 */
    #root > div:nth-child(1) > div > div > div > div > section > div {
        padding-top: 0rem;
        padding-right: 1rem;
        padding-bottom: 0rem;
        padding-left: 1rem;
    }
    header, footer, #MainMenu {
        visibility: hidden;
    }
    html, body, [class*="st-"] {
        margin: 0;
        padding: 0;
        height: 100%;
        overflow: hidden;
    }
    .scoreboard-container {
        display: flex;
        height: 100vh;
        width: 100vw;
        position: relative;
    }
    .panel {
        width: 50%;
        height: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
        font-family: 'Arial Black', sans-serif;
        font-weight: 900;
        color: white;
        font-size: 30vw;
        line-height: 1;
        position: relative;
        user-select: none;
    }
    .red-panel { background-color: #E53935; }
    .blue-panel { background-color: #1E88E5; }
    .top-score {
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
    }
    .top-score-red { color: #FFCDD2; }
    .top-score-blue { color: #BBDEFB; }
</style>
"""

# --- HTML 구조 정의 (버튼을 완전히 제거한 최종 테스트 버전) ---
HTML_CODE = """
<div class="scoreboard-container">
    <div class="top-score">
        <span class="top-score-red">0</span>
        <span class="top-score-blue">0</span>
    </div>

    <div class="red-panel">
        0
    </div>

    <div class="blue-panel">
        0
    </div>
</div>
"""

# --- 분리된 코드 렌더링 ---
st.markdown(CSS_CODE, unsafe_allow_html=True)
st.markdown(HTML_CODE, unsafe_allow_html=True)
