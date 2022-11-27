import fitz
print("Inserting image into PDF File")
doc = fitz.open("new_pdf_image.pdf")
rect = fitz.Rect(0, 0, 100, 100)
for page in doc:
    page.insertImage(rect, filename = "itachi.png")
doc.saveIncr()
print("Done inserting The Image in PDF File")