import argparse
import PyPDF2

def merge_pdfs(pdf_list, output_path):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output_path)
    merger.close()
    print(f"Merged PDF saved as: {output_path}")

def main():
    parser = argparse.ArgumentParser(
        description="Merge multiple PDF files into a single PDF."
    )
    parser.add_argument(
        "count",
        type=int,
        help="Number of PDF files to merge"
    )
    parser.add_argument(
        "pdfs",
        nargs="+",
        help="Paths of the PDF files to merge"
    )
    parser.add_argument(
        "-o", "--output",
        default="merged.pdf",
        help="Output file name (default: merged.pdf)"
    )

    args = parser.parse_args()

    if len(args.pdfs) != args.count:
        parser.error(f"Expected {args.count} PDFs, but got {len(args.pdfs)}")

    merge_pdfs(args.pdfs, args.output)

if __name__ == "__main__":
    main()
