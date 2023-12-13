import PyPDF2
import os

def merge_pdfs(input_files, output_path):
    pdf_writer = PyPDF2.PdfWriter()

    # Iterate over all input PDF files
    for input_file in input_files:
        with open(input_file, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page_num in range(len(pdf_reader.pages)):
                pdf_writer.add_page(pdf_reader.pages[page_num])

    # Write the merged PDF to the output file
    with open(output_path, 'wb') as output_file:
        pdf_writer.write(output_file)

if __name__ == "__main__":
    input_files = ["Page 1.pdf", "Page 2.pdf"]
    output_pdf_path = "merged.pdf"  # You can specify the desired output file name

    merge_pdfs(input_files, output_pdf_path)
