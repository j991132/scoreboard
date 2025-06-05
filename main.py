import streamlit as st

def main():
    # 웹 페이지 설정: 화면을 가득 채우도록 'wide' 레이아웃 사용
    st.set_page_config(layout="wide", page_title="경기 점수판")

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
        html, body, .stApp {
            margin: 0;
            padding: 0;
            height: 100vh; /* Viewport height */
            width: 100vw;  /* Viewport width */
            overflow: hidden; /* Prevent scrolling if not needed */
        }
        .block-container {
            padding-top: 1rem; /* Adjust top padding as needed */
            padding-bottom: 1rem; /* Adjust bottom padding as needed */
            padding-left: 1rem;
            padding-right: 1rem;
            flex-grow: 1; /* Allow container to grow */
            display: flex;
            flex-direction: column;
        }
        .main {
            display: flex;
            flex-direction: column;
            height: 100%;
        }
        .stButton>button {
            width: 100%; /* Make buttons fill their column */
            height: 60px; /* Make buttons larger */
            font-size: 24px; /* Larger font for buttons */
            font-weight: bold;
            margin: 5px 0; /* Add vertical margin */
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .red-btn > button {
            background-color: red !important;
            color: white !important;
            border: 2px solid red !important;
        }
        .blue-btn > button {
            background-color: blue !important;
            color: white !important;
            border: 2px solid blue !important;
        }
        .reset-btn > button {
            background-color: grey !important;
            color: white !important;
            border: 2px solid grey !important;
            width: 200px;
            margin-top: 20px;
        }
        .score-display-area {
            flex-grow: 1; /* Allow score display to take available space */
            display: flex;
            flex-direction: column;
            justify-content: center; /* Center content vertically */
            align-items: center; /* Center content horizontally */
        }
        .score-row {
            display: flex;
            width: 100%;
            justify-content: space-around;
            align-items: center;
            margin-top: 10px;
            margin-bottom: 10px;
            flex-grow: 1; /* Allow score boxes to take available space */
        }
        .score-box {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            width: 48%; /* Adjust width for better spacing */
            min-height: 250px; /* Minimum height for score boxes */
            font-size: 150px; /* Very large font for scores */
            font-weight: bold;
            color: white;
            border-radius: 15px;
            user-select: none; /* Prevent text selection */
            -webkit-user-select: none;
            -moz-user-select: none;
            -ms-user-select: none;
            cursor: grab; /* Indicates it's draggable/swipeable */
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
            align-items: flex-end; /* Align to the bottom of the top section */
            margin-bottom: 10px; /* Space below set scores */
            font-size: 45px; /* Larger font for set scores */
            font-weight: bold;
            width: 100%;
            position: relative; /* For absolute positioning of buttons */
            height: 80px; /* Fixed height for set score area */
        }
        .set-score-wrapper {
            display: flex;
            align-items: flex-end; /* Vertically align numbers and buttons */
            position: absolute;
            top: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 300px; /* Adjust width as needed */
            justify-content: center;
        }
        .set-score-box {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: flex-end; /* Align numbers to the bottom */
            padding: 5px 15px;
            background-color: rgba(255, 255, 255, 0.2); /* Slightly more opaque */
            border-radius: 8px;
            margin: 0 15px; /* Increase margin between set scores */
            min-width: 80px; /* Minimum width for set score boxes */
            height: 100%;
        }
        .set-score-red {
            color: red;
        }
        .set-score-blue {
            color: blue;
        }
        .set-score-buttons {
            display: flex;
            flex-direction: row; /* Buttons side-by-side */
            gap: 5px; /* Space between buttons */
            margin-top: 5px; /* Space above buttons */
        }
        .set-score-buttons .stButton>button {
            width: 50px; /* Smaller buttons for set scores */
            height: 35px;
            font-size: 18px;
            margin: 0;
        }
        .set-score-text {
            font-size: 60px; /* Larger set score number */
            line-height: 1; /* Remove extra line height */
        }

        @media (max-width: 768px) {
            .score-box {
                font-size: 100px; /* Adjust for smaller screens */
                min-height: 200px;
            }
            .set-score-text {
                font-size: 45px;
            }
            .stButton>button {
                height: 50px;
                font-size: 20px;
            }
            .set-score-buttons .stButton>button {
                width: 40px;
                height: 30px;
                font-size: 16px;
            }
        }
        </style>
    """, unsafe_allow_html=True)

    # 세트 스코어 부분
    st.markdown('<div class="set-score-container">', unsafe_allow_html=True)
    st.markdown('<div class="set-score-wrapper">', unsafe_allow_html=True)

    set_col1, set_col2 = st.columns(2) # Two columns for set scores
    with set_col1:
        st.markdown(f"""
            <div class="set-score-box set-score-red">
                <span class="set-score-text">{st.session_state.red_sets}</span>
                <div class="set-score-buttons">
                    <div class="red-btn">{st.button('+', key='red_set_plus_btn')}</div>
                    <div class="red-btn">{st.button('-', key='red_set_minus_btn')}</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with set_col2:
        st.markdown(f"""
            <div class="set-score-box set-score-blue">
                <span class="set-score-text">{st.session_state.blue_sets}</span>
                <div class="set-score-buttons">
                    <div class="blue-btn">{st.button('+', key='blue_set_plus_btn')}</div>
                    <div class="blue-btn">{st.button('-', key='blue_set_minus_btn')}</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown('</div></div>', unsafe_allow_html=True) # Close set-score-wrapper and set-score-container

    # 세트 스코어 버튼 로직
    if st.session_state.red_set_plus_btn:
        st.session_state.red_sets += 1
    if st.session_state.red_set_minus_btn:
        st.session_state.red_sets = max(0, st.session_state.red_sets - 1)
    if st.session_state.blue_set_plus_btn:
        st.session_state.blue_sets += 1
    if st.session_state.blue_set_minus_btn:
        st.session_state.blue_sets = max(0, st.session_state.blue_sets - 1)

    # 점수판 표시
    st.markdown('<div class="score-row">', unsafe_allow_html=True)
    score_col1, score_col2 = st.columns(2) # Two columns for main scores
    with score_col1:
        st.markdown(f"""
            <div class="score-box red-bg" id="red_score_area">
                {st.session_state.red_score}
            </div>
        """, unsafe_allow_html=True)
    with score_col2:
        st.markdown(f"""
            <div class="score-box blue-bg" id="blue_score_area">
                {st.session_state.blue_score}
            </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True) # Close score-row

    # 점수 추가/감소 버튼
    button_col1, button_col2 = st.columns(2) # Two columns for score buttons
    with button_col1:
        st.markdown("<div class='red-btn'>", unsafe_allow_html=True)
        if st.button('+', key='red_plus_btn'):
            st.session_state.red_score += 1
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("<div class='red-btn'>", unsafe_allow_html=True)
        if st.button('-', key='red_minus_btn'):
            st.session_state.red_score = max(0, st.session_state.red_score - 1)
        st.markdown("</div>", unsafe_allow_html=True)
    with button_col2:
        st.markdown("<div class='blue-btn'>", unsafe_allow_html=True)
        if st.button('+', key='blue_plus_btn'):
            st.session_state.blue_score += 1
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("<div class='blue-btn'>", unsafe_allow_html=True)
        if st.button('-', key='blue_minus_btn'):
            st.session_state.blue_score = max(0, st.session_state.blue_score - 1)
        st.markdown("</div>", unsafe_allow_html=True)

    # 리셋 버튼
    st.markdown("<div style='display:flex; justify-content:center; width:100%;'>", unsafe_allow_html=True)
    st.markdown("<div class='reset-btn'>", unsafe_allow_html=True)
    if st.button('리셋', key='reset_all', help="모든 점수를 0으로 초기화합니다."):
        st.session_state.red_score = 0
        st.session_state.blue_score = 0
        st.session_state.red_sets = 0
        st.session_state.blue_sets = 0
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # 자바스크립트를 사용하여 터치 스와이프 기능 구현 (Streamlit의 제한으로 인해 여전히 복잡)
    # Streamlit은 직접적인 DOM 접근 및 이벤트 리스너 추가가 어렵습니다.
    # 이전과 동일하게, 이 부분은 Streamlit의 Python 상태와 직접 연동하기 매우 어렵습니다.
    # 여기서는 스와이프 기능을 시뮬레이션하는 예시만 제공하며, 실제 웹앱에서는
    # 사용자 경험이 매끄럽지 않거나, 심지어 전혀 작동하지 않을 수 있음을 알려드립니다.
    # 이 스크립트 블록은 Streamlit 앱의 Python 상태를 직접 변경하지 않습니다.
    st.markdown("""
    <script>
    function setupSwipe(elementId, type) { // type can be 'red_score' or 'blue_score' etc.
        const element = document.getElementById(elementId);
        if (!element) return;

        let startY;
        const swipeThreshold = 50; // pixels

        element.addEventListener('touchstart', (e) => {
            startY = e.touches[0].clientY;
            e.preventDefault(); // Prevent default touch behavior (e.g., scrolling)
        }, { passive: false }); // Use passive: false to allow preventDefault

        element.addEventListener('touchmove', (e) => {
            e.preventDefault(); // Keep preventing default during move
        }, { passive: false });

        element.addEventListener('touchend', (e) => {
            const endY = e.changedTouches[0].clientY;
            const deltaY = endY - startY;

            if (Math.abs(deltaY) > swipeThreshold) {
                // This is the challenging part: how to communicate back to Streamlit
                // Streamlit doesn't have a built-in way to send JS events to Python.
                // A common hack is to manipulate a hidden input field and read its value,
                // or use st.query_params, but these are cumbersome for real-time updates.
                // For demonstration purposes, we'll just log to console.
                if (deltaY < 0) { // Swiped up
                    // alert(type + ' swiped up'); // For testing in browser
                    // In a real custom component, you'd send an event to Streamlit
                } else { // Swiped down
                    // alert(type + ' swiped down'); // For testing in browser
                    // In a real custom component, you'd send an event to Streamlit
                }
                // To actually update Streamlit state, you would need
                // a custom component that bridges JS and Python.
            }
        });
    }

    // Call the setup function for each score area
    setupSwipe('red_score_area', 'red_score');
    setupSwipe('blue_score_area', 'blue_score');
    </script>
    """, unsafe_allow_html=True)

    # st.experimental_rerun() 제거: 이 함수가 버튼 클릭 버그의 원인일 수 있습니다.
    # st.session_state가 변경되면 Streamlit은 자동으로 재렌더링합니다.

if __name__ == '__main__':
    main()
