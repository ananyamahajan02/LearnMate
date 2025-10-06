import fitz
from pathlib import Path
import json
import logging


#Setting up the folders and logging
logging.basicConfig(level=logging.INFO)
RAW_DIR = Path("data/raw_pdfs")
OUT_DIR = Path("data/extracted_text")
OUT_DIR.mkdir(parents=True, exist_ok=True)

def extract_pdf(pdf_path:Path):
    docs = fitz.open(str(pdf_path))
    pages = []
    for i in range(len(docs)):
        page = docs.load_page(i)
        text = page.get_text("text")
        pages.append(text)
    return pages

#Iterate all PDFs and saved outputs
def main():
    for pdf in RAW_DIR.glob("*pdf"):
        logging.info(f"Extracting:{pdf.name}")
        pages = extract_pdf(pdf)

        #Now saving json page wise
        out_json = OUT_DIR/f"{pdf.stem}_pages.json"
        with open(out_json, "w",encoding="utf-8") as f:
            json.dump({"file": pdf.name, "pages":pages},f,ensure_ascii=False, indent=2)
        logging.info(f"Saved JSON:{out_json}")

if __name__ =="__main__":
    main()     




