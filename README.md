# PDF Merger

A simple Python command-line tool to merge multiple PDF files into a single PDF.

## Requirements
- Python 3.7+
- PyPDF2

Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage
Run the script with the number of PDFs, their file paths, and an optional output file name.

```bash
python merge_pdf.py 2 file1.pdf file2.pdf -o merged.pdf
```

### Arguments
- `count` → Number of PDF files to merge.  
- `pdfs` → Paths of the PDF files.  
- `-o, --output` → Output file name (default: `merged.pdf`).  

### Example
```bash
python merge_pdf.py 3 doc1.pdf doc2.pdf doc3.pdf -o final.pdf
```

This will merge **doc1.pdf**, **doc2.pdf**, and **doc3.pdf** into a single file named **final.pdf**.
