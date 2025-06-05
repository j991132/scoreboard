import streamlit as st

# 세션 상태 초기화
if 'team1_score' not in st.session_state:
    st.session_state.team1_score = 25
if 'team2_score' not in st.session_state:
    st.session_state.team2_score = 25
if 'set_score1' not in st.session_state:
    st.session_state.set_score1 = 0
if 'set_score2' not in st.session_state:
    st.session_state.set_score2 = 0

# CSS 스타일링
st.markdown(
    """
    <style>
    .full-screen {
        height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        align-items: center;
        background-color: #f0f0f0;
        margin: 0;
        padding: 0;
    }
    .team-section {
        flex: 1;
        width: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    .red { background-color: #ff0000; color: white; }
    .blue { background-color: #0000ff; color: white; }
    .score { font-size: 150px; padding: 20px; font-weight: bold; }
    .set-score-container {
        position: absolute;
        top: 10px;
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
    }
    .set-score {
        font-size: 40px;
        margin: 0 10px;
        color: black;
    }
    .buttons { margin-top: 10px; display: flex; gap: 10px; }
    .button {
        padding: 10px 20px;
        font-size: 20px;
        border: none;
        cursor: pointer;
        border-radius: 5px;
    }
    .button.red { background-color: #cc0000; color: white; }
    .button.blue { background-color: #0000cc; color: white; }
    .reset-container {
        margin-bottom: 20px;
    }
    .reset-button {
        padding: 10px 40px;
        font-size: 20px;
        background-color: #888;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 전체 레이아웃
st.markdown('<div class="full-screen">', unsafe_allow_html=True)

# 세트 스코어 (중앙 상단)
st.markdown('<div class="set-score-container">', unsafe_allow_html=True)
col_set1, col_set2, col_set3, col_set4, col_set5 = st.columns([2, 1, 1, 1, 2])
with col_set2:
    st.markdown(f'<div class="set-score">{st.session_state.set_score1}</div>', unsafe_allow_html=True)
with col_set3:
    st.markdown(f'<div class="set-score">{st.session_state.set_score2}</div>', unsafe_allow_html=True)
with col_set1:
    if st.button('+', key='set1_inc'):
        st.session_state.set_score1 += 1
    if st.button('-', key='set1_dec'):
        st.session_state.set_score1 = max(0, st.session_state.set_score1 - 1)
with col_set4:
    if st.button('+', key='set2_inc'):
        st.session_state.set_score2 += 1
    if st.button('-', key='set2_dec'):
        st.session_state.set_score2 = max(0, st.session_state.set_score2 - 1)
st.markdown('</div>', unsafe_allow_html=True)

# 팀 1 (빨간색)
st.markdown('<div class="team-section red">', unsafe_allow_html=True)
st.markdown(f'<div class="score">{st.session_state.team1_score}</div>', unsafe_allow_html=True)
st.markdown('<div class="buttons">', unsafe_allow_html=True)
col_t1_inc, col_t1_dec = st.columns(2)
with col_t1_inc:
    if st.button('+', key='team1_inc'):
        st.session_state.team1_score += 1
with col_t1_dec:
    if st.button('-', key='team1_dec'):
        st.session_state.team1_score = max(0, st.session_state.team1_score - 1)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# 팀 2 (파란색)
st.markdown('<div class="team-section blue">', unsafe_allow_html=True)
st.markdown(f'<div class="score">{st.session_state.team2_score}</div>', unsafe_allow_html=True)
st.markdown('<div class="buttons">', unsafe_allow_html=True)
col_t2_inc, col_t2_dec = st.columns(2)
with col_t2_inc:
    if st.button('+', key='team2_inc'):
        st.session_state.team2_score += 1
with col_t2_dec:
    if st.button('-', key='team2_dec'):
        st.session_state.team2_score = max(0, st.session_state.team2_score - 1)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# 리셋 버튼 (중앙 하단)
st.markdown('<div class="reset-container">', unsafe_allow_html=True)
if st.button('리셋', key='reset'):
    st.session_state.team1_score = 0
    st.session_state.team2_score = 0
    st.session_state.set_score1 = 0
    st.session_state.set_score2 = 0
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# 터치 스와이프 기능 (점수 클릭 후 위/아래 드래그)
st.markdown(
    """
    <script>
    document.querySelectorAll('.score').forEach(score => {
        let startY;
        score.addEventListener('touchstart', (e) => {
            startY = e.touches[0].clientY;
        });
        score.addEventListener('touchend', (e) => {
            const endY = e.changedTouches[0].clientY;
            const diffY = startY - endY;
            if (Math.abs(diffY) > 50) {  // 스와이프 민감도 조정
                if (diffY > 0) {  // 위로 스와이프
                    score.innerText = parseInt(score.innerText) + 1;
                } else {  // 아래로 스와이프
                    score.innerText = Math.max(0, parseInt(score.innerText) - 1);
                }
                // Streamlit에 값 업데이트
                Streamlit.setComponentValue({ score: score.innerText });
            }
        });
    });
    </script>
    """,
    unsafe_allow_html=True
)
