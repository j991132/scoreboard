import streamlit as st

# 1. 페이지 설정 및 세션 상태 초기화
st.set_page_config(layout="wide")

if 'red_score' not in st.session_state:
    st.session_state.red_score = 0
if 'blue_score' not in st.session_state:
    st.session_state.blue_score = 0

# 2. 점수 변경 함수
def increment_red():
    st.session_state.red_score += 1

def decrement_red():
    st.session_state.red_score = max(0, st.session_state.red_score - 1)

def increment_blue():
    st.session_state.blue_score += 1

def decrement_blue():
    st.session_state.blue_score = max(0, st.session_state.blue_score - 1)
    
def reset_scores():
    st.session_state.red_score = 0
    st.session_state.blue_score = 0

# 3. CSS 스타일 정의
# 버튼들을 화면 위에 띄워서 배치하기 위한 스타일 추가
st.markdown("""
<style>
    /* Streamlit 기본 UI 숨기기 및 전체화면 설정 */
    #root > div:nth-child(1) > div > div > div > div > section {
        padding: 0;
    }
    header, footer, #MainMenu {
        visibility: hidden;
    }
    /* 점수판 패널 디자인 (보내주신 코드 기반) */
    .container {
        display: flex;
        height: 100vh;
        width: 100vw;
        font-family: Arial, sans-serif;
    }
    .left {
        flex: 1;
        background-color: #FF0000;
        display: flex;
        justify-content: center;
        align-items: center;
        color: white;
        font-size: 35vw;
        font-weight: bold;
        line-height: 1;
    }
    .right {
        flex: 1;
        background-color: #0000FF;
        display: flex;
        justify-content: center;
        align-items: center;
        color: white;
        font-size: 35vw;
        font-weight: bold;
        line-height: 1;
    }

    /* 버튼들을 담을 컨테이너들을 화면 위에 띄움 */
    .button-wrapper {
        position: absolute; /* 가장 가까운 positioned ancestor를 기준으로 위치 */
        bottom: 5vh;      /* 화면 하단에서 5% 위 */
        display: flex;
        gap: 20px;
        z-index: 10;
    }
    /* 왼쪽 버튼 그룹 위치 (화면 너비의 25% 지점 중앙) */
    .left-buttons {
        left: 25vw;
        transform: translateX(-50%);
    }
    /* 오른쪽 버튼 그룹 위치 (화면 너비의 75% 지점 중앙) */
    .right-buttons {
        left: 75vw;
        transform: translateX(-50%);
    }
    /* 리셋 버튼 위치 (화면 너비의 50% 지점 중앙) */
    .reset-button {
        left: 50vw;
        transform: translateX(-50%);
    }
    
    /* 버튼 자체의 스타일 */
    .stButton>button {
        width: 80px;
        height: 80px;
        border-radius: 50%;
        border: 3px solid white;
        background-color: rgba(255, 255, 255, 0.3);
        color: white;
        font-size: 30px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: rgba(255, 255, 255, 0.5);
    }
</style>
""", unsafe_allow_html=True)

# 4. HTML로 배경 점수판 그리기
# 점수만 표시하고, 버튼은 Streamlit으로 따로 그립니다.
st.markdown(f"""
    <div class="container">
        <div class="left">
            {st.session_state.red_score}
        </div>
        <div class="right">
            {st.session_state.blue_score}
        </div>
    </div>
""", unsafe_allow_html=True)

# 5. Streamlit 버튼들을 CSS로 제어하기 위해 div로 감싸서 배치
# 왼쪽 버튼들
st.markdown('<div class="button-wrapper left-buttons">', unsafe_allow_html=True)
cols_left = st.columns(2)
cols_left[0].button("+", on_click=increment_red, key="red_plus", use_container_width=True)
cols_left[1].button("-", on_click=decrement_red, key="red_minus", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# 오른쪽 버튼들
st.markdown('<div class="button-wrapper right-buttons">', unsafe_allow_html=True)
cols_right = st.columns(2)
cols_right[0].button("+", on_click=increment_blue, key="blue_plus", use_container_width=True)
cols_right[1].button("-", on_click=decrement_blue, key="blue_minus", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# 리셋 버튼
st.markdown('<div class="button-wrapper reset-button">', unsafe_allow_html=True)
st.button("🔄", on_click=reset_scores, key="reset")
st.markdown('</div>', unsafe_allow_html=True)
