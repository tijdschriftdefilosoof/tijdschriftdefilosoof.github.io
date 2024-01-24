import os
from pdf2image import convert_from_path

imgs = []
for i in range(88 + 1, 0, -1):
    pdf_file = f'./pdf/{i}.pdf'
    if os.path.isfile(pdf_file):
        images = convert_from_path(pdf_file, first_page=1, last_page=1)
        image_path = f'./img/{i}.png'
        for image in images:
            image.save(image_path, "PNG")
