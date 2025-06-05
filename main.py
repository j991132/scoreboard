import streamlit as st

# Initialize session state for scores
if 'team1_score' not in st.session_state:
    st.session_state.team1_score = 25
if 'team2_score' not in st.session_state:
    st.session_state.team2_score = 25
if 'set_score' not in st.session_state:
    st.session_state.set_score = 0

# CSS for full-screen layout and colors
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
    }
    .team-section {
        flex: 1;
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .red { background-color: #ff0000; color: white; }
    .blue { background-color: #0000ff; color: white; }
    .score { font-size: 100px; padding: 20px; }
    .buttons { margin-top: 10px; }
    .button { margin: 0 5px; padding: 10px 20px; font-size: 20px; }
    .set-score { font-size: 50px; margin: 10px; }
    </style>
    """,
    unsafe_allow_html=True
)

# Layout
st.markdown('<div class="full-screen">', unsafe_allow_html=True)

# Team 1 (Red)
st.markdown('<div class="team-section red">', unsafe_allow_html=True)
st.markdown(f'<div class="score">{st.session_state.team1_score}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Set Score (Center Top)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown('<div class="set-score">0</div>', unsafe_allow_html=True)
    col_s1, col_s2, col_s3 = st.columns([1, 1, 1])
    with col_s1:
        if st.button('+', key='set_inc'):
            st.session_state.set_score += 1
    with col_s3:
        if st.button('-', key='set_dec'):
            st.session_state.set_score = max(0, st.session_state.set_score - 1)

# Team 2 (Blue)
st.markdown('<div class="team-section blue">', unsafe_allow_html=True)
st.markdown(f'<div class="score">{st.session_state.team2_score}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Buttons Section
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    if st.button('+', key='team1_inc'):
        st.session_state.team1_score += 1
    if st.button('-', key='team1_dec'):
        st.session_state.team1_score = max(0, st.session_state.team1_score - 1)
with col3:
    if st.button('+', key='team2_inc'):
        st.session_state.team2_score += 1
    if st.button('-', key='team2_dec'):
        st.session_state.team2_score = max(0, st.session_state.team2_score - 1)
with col2:
    if st.button('Reset', key='reset'):
        st.session_state.team1_score = 0
        st.session_state.team2_score = 0
        st.session_state.set_score = 0

st.markdown('</div>', unsafe_allow_html=True)

# Simulate touch swipe (increment/decrement on click-hold simulation)
st.markdown(
    """
    <script>
    const scores = document.getElementsByClassName('score');
    for (let score of scores) {
        score.addEventListener('mousedown', () => {
            let count = 0;
            const interval = setInterval(() => {
                count++;
                if (count % 2 === 0) {
                    score.innerText = parseInt(score.innerText) + 1;
                } else {
                    score.innerText = parseInt(score.innerText) - 1;
                }
                Streamlit.setComponentValue({ score: score.innerText });
            }, 500);
            score.addEventListener('mouseup', () => clearInterval(interval));
        });
    }
    </script>
    """,
    unsafe_allow_html=True
)
