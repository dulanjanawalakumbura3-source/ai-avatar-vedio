import streamlit as st

st.set_page_config(page_title="AI Face Generator")

st.title("AI Face Generator")
st.write("Upload your image and audio files below.")

uploaded_image = st.file_uploader("Choose an image (JPG/PNG)", type=["jpg", "png"])
uploaded_audio = st.file_uploader("Choose an audio (MP3/WAV)", type=["mp3", "wav"])

if st.button("Generate Video"):
    if uploaded_image is not None and uploaded_audio is not None:
        st.info("Generating video... Please wait.")
    else:
        st.error("Please upload both image and audio files.")