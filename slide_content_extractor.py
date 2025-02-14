from pypdf import PdfReader

class SlideContentExtractor:
    def __init__(self, uploaded_file):
        self.uploaded_file = uploaded_file

    def extract(self):
        self.uploaded_file.seek(0)
        
        pdf_reader = PdfReader(self.uploaded_file)
        page = pdf_reader.pages[0]
        text = page.extract_text()
        return text
