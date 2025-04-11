import base64
import streamlit as st

# Background + Custom CSS
def set_bg_from_local(image_path):
    with open(image_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.4)),
                              url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            font-family: 'Segoe UI', sans-serif;
        }}

        h1, h2, h3, h4, h5, h6,
        .stFileUploader label,
        .stFileUploader div div div span,
        label {{
            color: white !important;
        }}

        .stAlert > div {{
            color: white !important;
            font-weight: bold !important;
        }}

        div[data-testid="stCaptionContainer"] p {{
            color: white !important;
            font-weight: bold !important;
            font-size: 1rem !important;
            opacity: 1 !important;
        }}

        .stButton>button {{
            color: white !important;
            background-color: rgba(255, 255, 255, 0.1);
            border: 1px solid white;
            font-weight: bold;
        }}
        .stButton>button:hover {{
            background-color: #29b6f6;
            color: black !important;
        }}

        .stTextInput input,
        .stSelectbox, .stNumberInput input {{
            color: white !important;
        }}

        /* Padding adjustment for better spacing */
        main .block-container {{
            padding-top: 1rem;
            padding-bottom: 1rem;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )