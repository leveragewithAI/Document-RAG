from unstructured.partition.pdf import partition_pdf
import os
from dotenv import load_dotenv
import pytesseract

load_dotenv()

os.environ["PATH"] = os.getenv("POPPLER_PATH") + os.environ["PATH"]
pytesseract.pytesseract.tesseract_cmd = os.getenv("TESSERACT_PATH")

def load_pdf(path: str):
    """
    Load complex PDFs(tables, diagrams, images, OCR) into structured elements.
    """

    elements = partition_pdf(
        filename=path,
        strategy="fast",
    )

    docs= []
    for e in elements:
        docs.append({
            "text": e.text if hasattr(e, "text") else "",
            "type": e.category,
            "metadata": {
                "source": path,
                "page_number": getattr(e.metadata, "page_number", None),
            }
        })
    
    return docs