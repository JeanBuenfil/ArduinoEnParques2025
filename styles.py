import streamlit as st

def styles():
    st.markdown("""
    <style>
        body {
            background-color: #121212;
            color: white;
        }
        .big-title {
            text-align: center;
            font-size: 48px;
            font-weight: bold;
        }
        .subtitle {
            text-align: center;
            font-size: 20px;
            color: #cccccc;
        }
        .card {
            border: 1px solid #ffffff40;
            border-radius: 15px;
            padding: 20px;
            text-align: center;
            background-color: #1c1c1c;
            box-shadow: 0px 0px 10px rgba(255, 255, 255, 0.1);
        }
        .card-title {
            font-size: 22px;
            font-weight: bold;
            color: #a855f7;
            margin-top: 10px;
        }
        .card-text {
            color: #cccccc;
        }
    </style>
    """, unsafe_allow_html=True)