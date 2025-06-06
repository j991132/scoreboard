import streamlit as st

# --- 1. 페이지 설정 및 상태 초기화 ---
st.set_page_config(layout="wide")

if 'red_score' not in st.session_state:
    st.session_state.red_score = 0
if 'blue_score' not in st.session_state:
    st.session_state.blue_score = 0

# --- 2. CSS 스타일 정의 ---
st.markdown("""
<style>
    /* Streamlit 기본 UI 숨기기 및 여백 제거 */
    #root > div:nth-child(1) > div > div > div > div > section {
        padding: 0;
    }
    iframe[title="st.iframe"] {
        height: 0; /* st.components.v1.html의 높이 제거 */
    }
    header, footer, #MainMenu {
        visibility: hidden;
    }
    
    /* 메인 컬럼들을 감싸는 가로 블록을 전체 화면으로 설정 */
    div[data-testid="stHorizontalBlock"] {
        height: 100vh;
        width: 100vw;
    }

    /* 각 점수판 컬럼(왼쪽, 오른쪽) 스타일 */
    div[data-testid="column"] {
        display: flex;
        flex-direction: column;
        justify-content: space-between; /* 컨텐츠를 위아래로 분산 */
        height: 100%;
        color: white;
        text-align: center;
        user-select: none;
        padding-bottom: 20px; /* 하단 버튼 영역 확보 */
    }
    /* 첫 번째 컬럼(빨강) */
    div[data-testid="column"]:nth-of-type(1) {
        background-color: #E53935;
    }
    /* 두 번째 컬럼(파랑) */
    div[data-testid="column"]:nth-of-type(2) {
        background-color: #1E88E5;
    }

    /* 점수 텍스트 스타일 */
    .score-display {
        font-family: 'Arial Black', sans-serif;
        font-size: 30vw;
        font-weight: 900;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-grow: 1; /* 남은 공간을 모두 차지 */
    }

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
    /* 리셋 버튼을 위한 특수 클래스 */
    .reset-button-container {
        position: fixed; /* 화면에 고정 */
        bottom: 20px; /* 하단에서 20px */
        left: 50%; /* 왼쪽에서 50% */
        transform: translateX(-50%); /* 정확히 중앙으로 이동 */
        z-index: 100; /* 다른 요소들 위에 표시 */
    }

</style>
""", unsafe_allow_html=True)


# --- 3. 화면 레이아웃 구성 ---
# 메인 점수판을 두 개의 컬럼으로 나눕니다.
col_left, col_right = st.columns(2, gap="small")

# 왼쪽(빨강) 점수판
with col_left:
    # 점수 표시
    st.markdown(f'<div class="score-display">{st.session_state.red_score}</div>', unsafe_allow_html=True)
    
    # 점수 변경 버튼 (컬럼 안의 컬럼으로 좌우 배치)
    btn_plus_left, btn_minus_left = st.columns(2)
    with btn_plus_left:
        if st.button('+', key='red_plus', use_container_width=True):
            st.session_state.red_score += 1
            st.rerun()
    with btn_minus_left:
        if st.button('-', key='red_minus', use_container_width=True):
            st.session_state.red_score = max(0, st.session_state.red_score - 1)
            st.rerun()

# 오른쪽(파랑) 점수판
with col_right:
    # 점수 표시
    st.markdown(f'<div class="score-display">{st.session_state.blue_score}</div>', unsafe_allow_html=True)
    
    # 점수 변경 버튼 (컬럼 안의 컬럼으로 좌우 배치)
    btn_plus_right, btn_minus_right = st.columns(2)
    with btn_plus_right:
        if st.button('+', key='blue_plus', use_container_width=True):
            st.session_state.blue_score += 1
            st.rerun()
    with btn_minus_right:
        if st.button('-', key='blue_minus', use_container_width=True):
            st.session_state.blue_score = max(0, st.session_state.blue_score - 1)
            st.rerun()

# --- 4. 리셋 버튼 (별도 처리) ---
# 리셋 버튼을 CSS로 제어하기 위해 div로 감쌉니다.
st.markdown('<div class="reset-button-container">', unsafe_allow_html=True)
if st.button('🔄', key='reset'):
    st.session_state.red_score = 0
    st.session_state.blue_score = 0
    st.rerun()
st.markdown('</div>', unsafe_allow_html=True)
