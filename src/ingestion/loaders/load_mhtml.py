from unstructured.partition.html import partition_html

def load_mhtml(path: str):
    """
    Load MHTML or HTML files into structured elements. Handles tables, images, headers, lists, etc
    """

    elements = partition_html(filename=path)

    docs = []
    for e in elements:
        docs.append({
            "text": e.text if hasattr(e, "text") else "",
            "type": e.category,
            "metadata": {
                "source": path,
            }
        })
    
    return docs