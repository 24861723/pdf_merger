# PDF Merger

PDF Merger is a web application built with Streamlit that allows users to merge multiple PDF files into a single document. It features a user-friendly interface with drag-and-drop functionality for easy file reordering.

## Features

- Upload multiple PDF files
- Drag-and-drop interface for reordering files
- Customizable output filename
- Dark theme UI
- Timestamp added to output filename for version control
- Download merged PDF directly from the app

## Installation

To run this application, you need Python installed on your system. Follow these steps to set up the project:

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/pdf-merger.git
   cd pdf-merger
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install streamlit PyPDF2 streamlit-sortables
   ```

## Usage

To run the application, use the following command:

```
streamlit run app.py
```

Then, open your web browser and go to `http://localhost:8501`.

1. Click on "Choose PDF files" to upload your PDF files.
2. Reorder the files by dragging and dropping them in the desired sequence.
3. Enter a name for the output file (default is "merged.pdf").
4. Click "Merge PDFs" to combine the files.
5. Once merging is complete, click "Download Merged PDF" to save the result.

## Code Overview

The main components of the application are:

- `streamlit`: Used for creating the web interface.
- `PyPDF2`: Handles PDF merging operations.
- `streamlit_sortables`: Provides drag-and-drop functionality for file reordering.

Key functions:

- `merge_pdfs(pdf_files)`: Merges the uploaded PDF files.
- Custom CSS: Implements a dark theme and improves the layout.

## Customization

You can customize the appearance and behavior of the app by modifying the following:

- Adjust the CSS in the `st.markdown()` section to change colors, layouts, etc.
- Modify the `st.set_page_config()` parameters to change the page title, icon, or layout.

## Contributing

Contributions to improve PDF Merger are welcome. Please feel free to submit a Pull Request.

## License

[Specify your license here, e.g., MIT License]

## Acknowledgments

- Streamlit for the wonderful web app framework
- PyPDF2 for PDF manipulation capabilities
- streamlit-sortables for the drag-and-drop interface
