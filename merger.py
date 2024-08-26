import fitz  # PyMuPDF
import os
from PIL import Image

def convert_image_to_pdf(image_file, output_pdf):
    """
    Converts a single image file to a PDF.
    """
    img = Image.open(image_file)
    width, height = img.size
    
    # Create a new PDF document
    pdf_document = fitz.open()
    
    # Create a new page with the size of the image
    pdf_page = pdf_document.new_page(width=width, height=height)
    
    # Insert image into the page
    pdf_page.insert_image(fitz.Rect(0, 0, width, height), filename=image_file)
    
    # Save the PDF
    pdf_document.save(output_pdf)
    pdf_document.close()

def merge_pdfs(pdf_files, output_filename):
    """
    Merges multiple PDF files into a single PDF.
    """
    pdf_merger = fitz.open()
    
    for pdf_file in pdf_files:
        pdf_document = fitz.open(pdf_file)
        pdf_merger.insert_pdf(pdf_document)
        pdf_document.close()
    
    pdf_merger.save(output_filename)
    pdf_merger.close()

def main():
    # Get the current working directory
    current_dir = os.getcwd()

    # Find all PNG files in the directory
    image_files = sorted([f for f in os.listdir(current_dir) if f.endswith('.png')])

    # Convert each PNG to a PDF and store the PDF filenames
    pdf_files = []
    for image_file in image_files:
        pdf_filename = image_file.replace('.png', '.pdf')
        convert_image_to_pdf(image_file, pdf_filename)
        pdf_files.append(pdf_filename)
        print(f"Converted {image_file} to {pdf_filename}")
    
    # Merge all the PDFs into a single file
    output_pdf = "combined_pages.pdf"
    merge_pdfs(pdf_files, output_pdf)
    print(f"Merged PDFs into {output_pdf}")

if __name__ == "__main__":
    main()
