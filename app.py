
import streamlit as st
import joblib
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="AI Mobile Guardian",
    page_icon="🛡️",
    layout="wide"
)

MODEL_PATH = "/content/drive/MyDrive/AI_Mobile_Guardian/models/prototype/mobile_guardian_rf.pkl"

model = joblib.load(MODEL_PATH)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #070B1A, #10152E, #17102B);
    color: white;
}
h1 {
    color: #48DFFF;
    text-shadow: 0 0 15px #168BFF;
}
h2, h3 {
    color: #A78BFA;
}
div.stButton > button {
    background: linear-gradient(90deg, #1677FF, #8B5CF6);
    color: white;
    border: none;
    border-radius: 12px;
    height: 50px;
    font-weight: bold;
    width: 100%;
}
div.stButton > button:hover {
    box-shadow: 0 0 20px #48DFFF;
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>🛡️ AI MOBILE GUARDIAN</h1>", unsafe_allow_html=True)
st.caption("INTELLIGENT ANDROID MALWARE CLASSIFICATION SYSTEM")

st.markdown("---")

left, right = st.columns([1, 1])

with left:
    st.subheader("APK ANALYSIS")
    st.write("Upload an Android application package.")

    apk_file = st.file_uploader(
        "Select APK file",
        type=["apk"]
    )

    st.info("APK feature extraction is not connected yet.")

    st.button(
        "SCAN APK",
        disabled=True,
        use_container_width=True
    )

with right:
    st.subheader("SECURITY REPORT")

    st.markdown("""
    <div style="
        background:rgba(30,40,80,0.55);
        border:1px solid #397DFF;
        border-radius:18px;
        padding:25px;
        text-align:center;
    ">
        <h2>🛡️ SYSTEM READY</h2>
        <p style="color:#48DFFF">
        Random Forest Model Connected
        </p>
        <h1 style="font-size:40px">92.36%</h1>
        <p>Test Accuracy</p>
        <p style="color:#A78BFA">
        7 Malware Classification Categories
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.subheader("MODEL INFORMATION")

col1, col2, col3 = st.columns(3)

col1.metric("Algorithm", "Random Forest")
col2.metric("Features", "300 selected")
col3.metric("Classes", "7")

st.markdown("---")
st.caption("AI Mobile Guardian | Master’s Research Prototype")
