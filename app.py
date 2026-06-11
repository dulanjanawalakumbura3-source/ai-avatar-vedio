import streamlit as st
from moviepy.editor import ImageClip, AudioFileClip
import os

# Page Configuration
st.set_page_config(page_title="AI Face Generator")
st.title("AI Face Generator")

# File Uploaders
uploaded_image = st.file_uploader("Choose an image (JPG/PNG)", type=['jpg', 'jpeg', 'png'])
uploaded_audio = st.file_uploader("Choose an audio (MP3/WAV)", type=['mp3', 'wav'])

# Generation Logic
if st.button("Generate Video"):
    if uploaded_image is not None and uploaded_audio is not None:
        st.info("Generating video... Please wait.")
        
        # Save uploaded files temporarily
        with open("temp_img.jpg", "wb") as f:
            f.write(uploaded_image.getbuffer())
        with open("temp_audio.mp3", "wb") as f:
            f.write(uploaded_audio.getbuffer())
        
        try:
            # Processing the video
            audio_clip = AudioFileClip("temp_audio.mp3")
            image_clip = ImageClip("temp_img.jpg").set_duration(audio_clip.duration)
            video = image_clip.set_audio(audio_clip)
            
            # Export the video
            output_filename = "output.mp4"
            video.write_videofile(output_filename, fps=24, codec="libx264")
            
            st.success("Video generated successfully!")
            st.video(output_filename)
            
        except Exception as e:
            st.error(f"An error occurred: {e}")
            
    else:
        st.error("Please upload both image and audio files.")
