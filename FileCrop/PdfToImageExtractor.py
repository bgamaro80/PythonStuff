import os
from pdf2image import convert_from_path

inputDir = "./input/Scenarios"
outputDir = "./output"

for fname in os.listdir(inputDir):

    filename_w_ext = os.path.basename(fname)
    name, _ = os.path.splitext(filename_w_ext)

    pdffile = f"{inputDir}/{fname}"

    pages = convert_from_path(pdf_path=pdffile,
                              dpi=300,
                              poppler_path=r'C:\Program Files\poppler-0.68.0\bin')
    
    for i, image in enumerate(pages):
        fname = f"{outputDir}/{name}.jpg"
        image.save(fname, "JPEG")