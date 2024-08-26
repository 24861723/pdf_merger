import streamlit as st
import PyPDF2
import io
from datetime import datetime
from streamlit_sortables import sort_items

st.set_page_config(page_title="PDF Merger", page_icon="📄", layout="wide")

def merge_pdfs(pdf_files):
    merger = PyPDF2.PdfMerger()
    for pdf_file in pdf_files:
        merger.append(pdf_file)
    output = io.BytesIO()
    merger.write(output)
    merger.close()
    return output.getvalue()

# Custom CSS for dark theme and layout
st.markdown("""
<style>
    body {
        color: #E0E0E0;
        background-color: #1E1E1E;
    }
    .stButton>button {
        color: #E0E0E0;
        background-color: #4CAF50;
        border: none;
        border-radius: 4px;
        padding: 10px 24px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .main .block-container {
        max-width: 40%;
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .draggable-item {
        padding: 10px;
        margin: 5px 0;
        background-color: #2E2E2E;
        border-radius: 5px;
        cursor: move;
    }
    .draggable-item:hover {
        background-color: #3E3E3E;
    }
    .uploadedFile {display: none;}
</style>
""", unsafe_allow_html=True)

st.title("PDF Merger")

uploaded_files = st.file_uploader("Choose PDF files", type="pdf", accept_multiple_files=True, key="pdf_uploader")

if uploaded_files:
    st.write(f"Number of files uploaded: {len(uploaded_files)}")
    
    # Create a list of file names for reordering
    file_names = [file.name for file in uploaded_files]
    
    # Allow user to reorder files using drag and drop
    st.subheader("Reorder files")
    st.write("Drag and drop the files to reorder them:")
    sorted_files = sort_items(file_names)
    
    # Reorder the actual file objects based on the sorted names
    reordered_files = [next(file for file in uploaded_files if file.name == name) for name in sorted_files]
    
    output_filename = st.text_input("Enter output filename", "merged.pdf")
    
    if st.button("Merge PDFs"):
        with st.spinner("Merging PDFs..."):
            merged_pdf = merge_pdfs(reordered_files)
        
        st.success("PDFs merged successfully!")
        
        # Add timestamp to filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"{output_filename.rsplit('.', 1)[0]}_{timestamp}.pdf"
        
        st.download_button(
            label="📥 Download Merged PDF",
            data=merged_pdf,
            file_name=output_filename,
            mime="application/pdf"
        )
else:
    st.info("Please upload PDF files to merge.")