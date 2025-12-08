import os
from .load_pdf import load_pdf
from .load_mhtml import load_mhtml

def load_document(path: str):
    ext = os.path.splitext(path)[1].lower()

    if ext in [".pdf"]:
        print(load_pdf(path))
        return load_pdf(path)
    
    if ext in [".mhtml", ".mht", ".html", ".htm"]:
        print(load_mhtml(path))
        return load_mhtml(path)
    
    raise ValueError(f"Unsupported file type: {ext}")