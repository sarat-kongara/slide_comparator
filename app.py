import streamlit as st
import textwrap
from slide import Slide
from slide_comparator import SlideComparator

st.subheader('Upload base slide')
base_file = st.file_uploader("Select a pdf file with one page", type=["pdf"])

if base_file is not None:
    base_slide = Slide(base_file)
    base_slide.process()

    content = base_slide.content
    image_buffer = base_slide.image_buffer
    phash = base_slide.phash

    base_col1, base_col2 = st.columns([2, 1])

    with base_col1:
        st.write(textwrap.shorten(content, width=200, placeholder="..."))

    with base_col2:
        st.image(image_buffer, caption=phash, use_container_width=False)

    st.subheader('Upload comparision slides')
    comparision_files = st.file_uploader("Upload pdf files", type=["pdf"], accept_multiple_files=True)

    if comparision_files:
        for comparision_file in comparision_files:
            comparision_slide = Slide(comparision_file)

            comparision_slide.process()
            content = comparision_slide.content
            image_buffer = comparision_slide.image_buffer
            phash = comparision_slide.phash

            slide_comparator = SlideComparator(base_slide, comparision_slide)
            result = slide_comparator.compare_images()
            content_similarity = slide_comparator.compare_content()

            col1, col2, col3 = st.columns([1, 1, 1])

            with col1:
                st.text(textwrap.shorten(content, width=200, placeholder="..."))
    
            with col2:
                caption = str(phash)
                st.image(image_buffer, caption=str(phash), use_container_width=False)
            
            with col3:
                st.info(result)
                st.success(f"Cosine Similarity: {content_similarity}")