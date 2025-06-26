import fitz
def extract_text_from_file(uploaded_file):
    if uploaded_file.name.endswith(".pdf"):
        text = ""
        doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        for page in doc:
            text += page.get_text()
        return text
    elif uploaded_file.name.endswith(".txt"):
        return uploaded_file.read().decode("utf-8")
    else:
        return ""
