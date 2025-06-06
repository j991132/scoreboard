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
    }
    .score {
        font-size: 60px;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# HTML 구조로 디자인 구현 (점수를 양쪽에 각각 00으로 나눔)
st.markdown("""
    <div class="container">
        <div class="left">
            <div class="score">00</div>
            <div>25</div>
        </div>
        <div class="right">
            <div class="score">00</div>
            <div>25</div>
        </div>
    </div>
""", unsafe_allow_html=True)
