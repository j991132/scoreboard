import streamlit as st

def main():
    st.set_page_config(layout="centered")
    st.title("경기 점수판")

    # 세션 상태 초기화 (점수 및 세트 스코어 유지)
    if 'red_score' not in st.session_state:
        st.session_state.red_score = 25 # 초기값 25로 설정
    if 'blue_score' not in st.session_state:
        st.session_state.blue_score = 25 # 초기값 25로 설정
    if 'red_sets' not in st.session_state:
        st.session_state.red_sets = 0
    if 'blue_sets' not in st.session_state:
        st.session_state.blue_sets = 0

    # CSS를 사용하여 레이아웃 및 스타일링
    st.markdown("""
        <style>
        .score-container {
            display: flex;
            justify-content: space-around;
            align-items: center;
            margin-bottom: 20px;
        }
        .score-box {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            width: 48%; /* Adjust width for better spacing */
            height: 200px;
            font-size: 100px;
            font-weight: bold;
            color: white;
            border-radius: 10px;
            cursor: grab; /* Indicates it's draggable/swipeable */
            user-select: none; /* Prevent text selection */
            -webkit-user-select: none; /* Safari */
            -moz-user-select: none; /* Firefox */
            -ms-user-select: none; /* IE/Edge */
        }
        .red-bg {
            background-color: red;
        }
        .blue-bg {
            background-color: blue;
        }
        .set-score-container {
            display: flex;
            justify-content: center;
            margin-bottom: 20px;
            font-size: 40px;
            font-weight: bold;
        }
        .set-score-box {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 5px 15px;
            background-color: rgba(255, 255, 255, 0.3); /* Semi-transparent background */
            border-radius: 5px;
            margin: 0 10px;
        }
        .set-score-red {
            color: red;
        }
        .set-score-blue {
            color: blue;
        }
        .stButton > button {
            width: 100px;
            height: 50px;
            font-size: 20px;
            font-weight: bold;
            margin: 5px;
            border-radius: 5px;
        }
        .red-btn > button {
            background-color: red !important;
            color: white !important;
        }
        .blue-btn > button {
            background-color: blue !important;
            color: white !important;
        }
        .reset-btn > button {
            background-color: grey !important;
            color: white !important;
            width: 200px;
        }
        </style>
    """, unsafe_allow_html=True)

    # 세트 스코어 부분
    st.markdown(f"""
        <div class="set-score-container">
            <div class="set-score-box set-score-red">
                <span>{st.session_state.red_sets}</span>
                <div style="display:flex;">
                    <div class="red-btn">
                        {st.button('+', key='red_set_plus')}
                    </div>
                    <div class="red-btn">
                        {st.button('-', key='red_set_minus')}
                    </div>
                </div>
            </div>
            <div class="set-score-box set-score-blue">
                <span>{st.session_state.blue_sets}</span>
                <div style="display:flex;">
                    <div class="blue-btn">
                        {st.button('+', key='blue_set_plus')}
                    </div>
                    <div class="blue-btn">
                        {st.button('-', key='blue_set_minus')}
                    </div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 세트 스코어 버튼 로직
    if st.session_state.red_set_plus:
        st.session_state.red_sets += 1
    if st.session_state.red_set_minus:
        st.session_state.red_sets = max(0, st.session_state.red_sets - 1)
    if st.session_state.blue_set_plus:
        st.session_state.blue_sets += 1
    if st.session_state.blue_set_minus:
        st.session_state.blue_sets = max(0, st.session_state.blue_sets - 1)

    # 점수판 표시
    st.markdown(f"""
        <div class="score-container">
            <div class="score-box red-bg" id="red_score_area">
                {st.session_state.red_score}
            </div>
            <div class="score-box blue-bg" id="blue_score_area">
                {st.session_state.blue_score}
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 점수 추가/감소 버튼
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div class='red-btn'>", unsafe_allow_html=True)
        if st.button('+', key='red_plus'):
            st.session_state.red_score += 1
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("<div class='red-btn'>", unsafe_allow_html=True)
        if st.button('-', key='red_minus'):
            st.session_state.red_score = max(0, st.session_state.red_score - 1)
        st.markdown("</div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='blue-btn'>", unsafe_allow_html=True)
        if st.button('+', key='blue_plus'):
            st.session_state.blue_score += 1
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("<div class='blue-btn'>", unsafe_allow_html=True)
        if st.button('-', key='blue_minus'):
            st.session_state.blue_score = max(0, st.session_state.blue_score - 1)
        st.markdown("</div>", unsafe_allow_html=True)

    # 리셋 버튼
    st.markdown("<div style='display:flex; justify-content:center;'>", unsafe_allow_html=True)
    if st.button('리셋', key='reset_all', help="모든 점수를 0으로 초기화합니다."):
        st.session_state.red_score = 0
        st.session_state.blue_score = 0
        st.session_state.red_sets = 0
        st.session_state.blue_sets = 0
    st.markdown("</div>", unsafe_allow_html=True)

    # 자바스크립트를 사용하여 터치 스와이프 기능 구현 (Streamlit의 제한으로 인해 다소 복잡)
    # Streamlit은 직접적인 DOM 접근 및 이벤트 리스너 추가가 어렵습니다.
    # 따라서 st.components.v1.html을 사용하여 자바스크립트 코드를 삽입해야 합니다.
    # 하지만 이 방법은 상태 관리 (session_state)와 직접 연동하기 매우 어렵습니다.
    # 여기서는 스와이프 기능을 시뮬레이션하는 예시만 제공하며, 실제 웹앱에서는
    # 사용자 경험이 매끄럽지 않을 수 있음을 알려드립니다.
    st.markdown("""
    <script>
    function setupSwipe(elementId, incrementCallback, decrementCallback) {
        const element = document.getElementById(elementId);
        let startY;

        if (element) {
            element.addEventListener('touchstart', (e) => {
                startY = e.touches[0].clientY;
            });

            element.addEventListener('touchmove', (e) => {
                // Prevent scrolling while swiping
                e.preventDefault();
            });

            element.addEventListener('touchend', (e) => {
                const endY = e.changedTouches[0].clientY;
                const deltaY = endY - startY;

                if (Math.abs(deltaY) > 20) { // Threshold for swipe
                    if (deltaY < 0) { // Swiped up
                        // Use Streamlit's messaging system (if possible, or a workaround)
                        // This part is the most challenging for direct integration
                        // For a real app, you might need a custom component or a server-side callback.
                        // Here, we'll simulate by re-running the script
                        // In a real scenario, you'd send a message to Streamlit and update session_state.
                        if (incrementCallback) incrementCallback();
                    } else { // Swiped down
                        if (decrementCallback) decrementCallback();
                    }
                    // Trigger a re-run of the Streamlit app to update the score
                    // This is a hacky way and might not be smooth.
                    // Ideally, Streamlit would have a direct JS-to-Python bridge for events.
                    // window.location.reload(); // This will reset the state, not ideal
                }
            });
        }
    }

    // Call the setup function for each score area
    // This will *not* directly update Streamlit state without a complex bridge.
    // The following callbacks are placeholders.
    // To make this work, you'd need a custom component or a more advanced JS/Python interaction.
    // For now, these will only register the events in the browser, not update Streamlit directly.
    setupSwipe('red_score_area', () => { /* Streamlit Callback for Red Score Up */ }, () => { /* Streamlit Callback for Red Score Down */ });
    setupSwipe('blue_score_area', () => { /* Streamlit Callback for Blue Score Up */ }, () => { /* Streamlit Callback for Blue Score Down */ });

    </script>
    """, unsafe_allow_html=True)

    # 세션 상태가 업데이트되면 Streamlit은 자동으로 다시 렌더링합니다.
    # 따라서 버튼 클릭 시 점수 업데이트는 이전에 구현된 st.session_state를 통해 이루어집니다.
    st.experimental_rerun() # Ensure re-render after state changes from initial button presses

if __name__ == '__main__':
    main()
