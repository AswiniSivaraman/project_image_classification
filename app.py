import streamlit as st
from PIL import Image
from utils.predict import load_model_and_predict
from utils.style import set_bg_from_local

# Full-width layout
st.set_page_config(page_title="Fish Classifier 🐟", layout="wide")

# Apply background
set_bg_from_local("images/bg_img.jpg") 

# Centered title
st.markdown(
    """
    <h1 style='text-align: center; color: white;'>
        🐟 Multiclass Fish Image Classifier
    </h1>
    """,
    unsafe_allow_html=True
)

# Session state setup
if "uploaded_image" not in st.session_state:
    st.session_state.uploaded_image = None

if "prediction_result" not in st.session_state:
    st.session_state.prediction_result = None

if "uploader_key" not in st.session_state:
    st.session_state.uploader_key = "uploader_1"


# Two-column full-width layout
col1, col2 = st.columns([3, 2], gap="large")

with col1:
    # File uploader with dynamic key
    uploaded = st.file_uploader(
        "Upload a fish image", 
        type=["jpg", "jpeg", "png"],
        key=st.session_state.uploader_key
    )

    if uploaded:
        st.session_state.uploaded_image = uploaded

    if st.session_state.uploaded_image:
        image = Image.open(st.session_state.uploaded_image)
        st.image(image, caption="Uploaded Image", width=600)

        # Buttons
        b1, b2 = st.columns(2)
        with b1:
            if st.button("Predict"):
                with st.spinner("Classifying..."):
                    prediction, confidence, used_model = load_model_and_predict(image)
                    st.session_state.prediction_result = {
                        "prediction": prediction,
                        "confidence": confidence,
                        "model": used_model
                    }
                    st.balloons()

        with b2:
            if st.button("Reset"):
                # Reset both data and uploader key to refresh uploader
                st.session_state.uploaded_image = None
                st.session_state.prediction_result = None
                st.session_state.uploader_key = f"uploader_{st.session_state.uploader_key[-1]}x"
                st.rerun()

with col2:
    if st.session_state.prediction_result:
        result = st.session_state.prediction_result
        st.markdown("<div style='text-align:center'>", unsafe_allow_html=True)
        st.success(f"Predicted Fish Species: **{result['prediction']}**")
        st.info(f"Confidence Score: {result['confidence']:.2f}")
        
        # Confidence Warning
        if result["confidence"] < 0.5:
            st.warning("⚠️ Low confidence — the model may not recognize this fish accurately. Try a clearer image or a known category.")

        st.caption(f"Model used: {result['model']}")
        st.markdown("</div>", unsafe_allow_html=True)

