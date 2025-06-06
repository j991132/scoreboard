import streamlit as st

# --- 1. 페이지 설정 및 상태 초기화 ---
st.set_page_config(layout="wide")

if 'red_score' not in st.session_state:
    st.session_state.red_score = 0
if 'blue_score' not in st.session_state:
    st.session_state.blue_score = 0

# --- 2. CSS 스타일 정의 ---
# 사용자님의 예제 코드 기반 + 버튼 스타일 추가
st.markdown("""
<style>
    /* Streamlit 기본 UI 숨기기 및 전체화면 설정 */
    #root > div:nth-child(1) > div > div > div > div > section {
        padding: 0;
    }
    header, footer, #MainMenu {
        visibility: hidden;
    }
    /* 점수판 패널 컨테이너 (높이를 85%로 설정해 하단에 버튼 공간 확보) */
    .container {
        display: flex;
        height: 85vh; /* 버튼을 위해 높이 조정 */
        width: 100vw;
        margin: 0;
        padding: 0;
        font-family: 'Arial Black', sans-serif;
    }
    /* 왼쪽/오른쪽 패널 (flex: 1 사용) */
    .panel {
        flex: 1;
        display: flex;
        justify-content: center;
        align-items: center;
        color: white;
        font-size: 30vw;
        font-weight: bold;
        user-select: none;
    }
    .left { background-color: #E53935; }
    .right { background-color: #1E88E5; }

    /* Streamlit 버튼 스타일링 */
    .stButton>button {
        width: 80px;
        height: 80px;
        padding: 10px;
        border-radius: 50%;
        border: 3px solid #FFFFFF;
        background-color: rgba(0, 0, 0, 0.2);
        color: white;
        font-size: 30px;
        font-weight: bold;
    }
    .stButton>button:hover {
        border-color: #FFC107;
        color: #FFC107;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. HTML 구조로 점수판 패널 표시 ---
# 버튼 없이, 순수하게 화면 표시만 담당
st.markdown(f"""
    <div class="container">
        <div class="panel left">{st.session_state.red_score}</div>
        <div class="panel right">{st.session_state.blue_score}</div>
    </div>
""", unsafe_allow_html=True)


# --- 4. Streamlit의 컬럼과 버튼으로 컨트롤러 구현 ---
# 화면 하단에 5개의 컬럼을 만들어 버튼을 배치
col1, col2, col3, col4, col5 = st.columns([1.5, 1, 1, 1, 1.5])

with col2:
    if st.button('-', key='red_minus', use_container_width=True):
        st.session_state.red_score = max(0, st.session_state.red_score - 1)
        st.rerun()
    if st.button('+', key='red_plus', use_container_width=True):
        st.session_state.red_score += 1
        st.rerun()

with col3:
    if st.button('🔄', key='reset', use_container_width=True):
        st.session_state.red_score = 0
        st.session_state.blue_score = 0
        st.rerun()

with col4:
    if st.button('-', key='blue_minus', use_container_width=True):
        st.session_state.blue_score = max(0, st.session_state.blue_score - 1)
        st.rerun()
    if st.button('+', key='blue_plus', use_container_width=True):
        st.session_state.blue_score += 1
        st.rerun()
