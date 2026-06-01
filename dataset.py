import argparse
import os 
import sys
from docx import Document
from bs4 import BeautifulSoup

def is_url(path):
    return path.startswith("http://") or path.startswith("https://")

def read_txt(path: str) -> str:
    with open(path, "r", encoding="utf-8",errors="ignore") as textData:
        return textData.read()

def read_pdf(path: str) -> str:
    try:
        from pypdf import PdfReader
    except Exception as e:
        sys.exit("pydf not installed")
    
    pdfData=[]
    with open(path,"rb") as pdfMain:
        pdf=PdfReader(pdfMain)
        for page in pdf.pages:
            pdfData.append(page.extract_text())
    return "\n\n".join(pdfData)

def read_document(path: str) -> str:
    try: 
        from docx import Document
    except Exception as e:
        print("docx not installed properly")
    
    doc = Document(path)
    return "\n\n".join(
        p.text for p in doc.paragraphs if p.text.strip()
    )

def read_website(path:str)->str:
    try:
        import requests
    except:
        print("requests not installed")
    requestText = requests.get(path, timeout=10)
    requestText.raise_for_status()  
    soup=BeautifulSoup(requestText.text,features="html.parser")
    for script in soup(["script","style"]):
        script.extract()
    return soup.get_text()

def load_document(path:str) -> str:
    if is_url(path):
        return read_website(path)
        

    if not os.path.exists(path):
        sys.exit("Path not Found")
    ext=os.path.splitext(path)[1].lower()
    readers={
        ".md":read_txt,
        ".txt":read_txt,
        ".docx":read_document,
        ".pdf":read_pdf,
        
    }
    if ext not in readers:
        print("File Type Not Supported")
    dataSet=readers[ext](path)
    return dataSet


