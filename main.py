import streamlit as st

# Streamlit 페이지 설정 (화면을 꽉 채우기 위해 넓게 설정)
st.set_page_config(layout="wide")

# CSS 스타일 정의
st.markdown("""
    <style>
    .container {
        display: flex;
        height: 100vh;
        width: 100vw;
        margin: 0;
        padding: 0;
        justify-content: center;
        align-items: flex-start;
        background-color: #FF0000;
    }
    .score-box {
        display: flex;
        justify-content: center;
        align-items: center;
        background-color: rgba(255, 255, 255, 0.5);
        padding: 20px;
        margin-top: 20px;
        font-family: Arial, sans-serif;
    }
    .left, .right {
        display: flex;
        flex-direction: column;
        align-items: center;
        color: black;
        font-size: 60px;
        font-weight: bold;
        margin: 0 20px;
    }
    .score {
        font-size: 40px;
        margin-bottom: 10px;
    }
    .main-score {
        font-size: 80px;
    }
    </style>
""", unsafe_allow_html=True)

# HTML 구조로 디자인 구현
st.markdown("""
    <div class="container">
        <div class="score-box">
            <div class="left">
                <div class="score">0</div>
                <div class="main-score">25</div>
            </div>
            <div class="right">
                <div class="score">0</div>
                <div class="main-score">25</div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)
