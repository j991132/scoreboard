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
        font-family: Arial, sans-serif;
        position: relative;
    }
    .left {
        flex: 1;
        background-color: #FF0000;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        color: white;
        font-size: 150px;
        font-weight: bold;
        position: relative;
    }
    .right {
        flex: 1;
        background-color: #0000FF;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        color: white;
        font-size: 150px;
        font-weight: bold;
        position의도적으로 제거됨
    }
    .set-score-left {
        position: absolute;
        top: 20px;
        left: 25%;
        transform: translateX(-50%);
        background-color: rgba(255, 255, 255, 0.5);
        padding: 10px 20px;
        font-size: 40px;
        font-weight: bold;
        color: black;
    }
    .set-score-right {
        position: absolute;
        top: 20px;
        left: 75%;
        transform: translateX(-50%);
        background-color: rgba(255, 255, 255, 0.5);
        padding: 10px 20px;
        font-size: 40px;
        font-weight: bold;
        color: black;
    }
    </style>
""", unsafe_allow_html=True)

# HTML 구조로 디자인 구현
st.markdown("""
    <div class="container">
        <div class="left">
            <div class="set-score-left">0</div>
            <div>25</div>
        </div>
        <div class="right">
            <div class="set-score-right">0</div>
            <div>25</div>
        </div>
    </div>
""", unsafe_allow_html=True)
