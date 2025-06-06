import streamlit as st

# 1. 페이지 설정 및 세션 상태 초기화
st.set_page_config(layout="wide")

# 점수 변수들
if 'red_score' not in st.session_state:
    st.session_state.red_score = 0
if 'blue_score' not in st.session_state:
    st.session_state.blue_score = 0

# 세트 스코어 변수들 추가
if 'red_set_score' not in st.session_state:
    st.session_state.red_set_score = 0
if 'blue_set_score' not in st.session_state:
    st.session_state.blue_set_score = 0


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
    # 리셋 시 세트 스코어는 유지하거나, 필요시 0으로 초기화할 수 있습니다.
    # st.session_state.red_set_score = 0
    # st.session_state.blue_set_score = 0


# 3. CSS 스타일 정의
st.markdown("""
<style>
    /* Streamlit 기본 UI 숨기기 및 전체화면 설정 */
    #root > div:nth-child(1) > div > div > div > div > section {
        padding: 0;
    }
    header, footer, #MainMenu {
        visibility: hidden;
    }
    /* 점수판 패널 디자인 */
    .container {
        display: flex;
        height: 100vh;
        width: 100vw;
        font-family: Arial, sans-serif;
        position: relative; /* 자식 absolute 요소들의 기준점 */
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

    /* ★★★ 세트 스코어 스타일 추가 ★★★ */
    .set-score {
        position: absolute;
        top: 3vh;
        left: 50%;
        transform: translateX(-50%);
        background-color: rgba(0, 0, 0, 0.2);
        padding: 10px 30px;
        border-radius: 15px;
        font-size: 5vw;
        font-weight: bold;
        color: white;
        display: flex;
        gap: 30px;
        z-index: 10;
    }

    /* 버튼들을 담을 컨테이너들을 화면 위에 띄움 */
    .button-wrapper {
        position: absolute;
        bottom: 5vh;
        display: flex;
        gap: 20px;
        z-index: 10;
    }
    .left-buttons {
        left: 25vw;
        transform: translateX(-50%);
    }
    .right-buttons {
        left: 75vw;
        transform: translateX(-50%);
    }
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

# 4. HTML로 배경 점수판과 세트 스코어 그리기
st.markdown(f"""
    <div class="container">
        <div class="set-score">
            <span>{st.session_state.red_set_score}</span>
            <span>{st.session_state.blue_set_score}</span>
        </div>

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
