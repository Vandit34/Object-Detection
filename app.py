import streamlit as st

st.set_page_config(
    page_title="Object Detection App",
    layout="centered", 
)

def main():
    st.title("VisionScope")

    file = st.file_uploader("Upload an image or video", type=["jpg", "png", "mp4"])

    if file is not None:
        if file.type.startswith('image'):
            st.image(file)
        elif file.type.startswith('video'):
            st.video(file)

if __name__ == "__main__":
    main()