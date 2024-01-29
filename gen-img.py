import os
from pdf2image import convert_from_path
MAX = 88

imgs = []
for i in range(MAX + 1, 0, -1):
    pdf_path = f'./pdf/{i}.pdf'
    img_path = f'./img/{i}.png'
    if not os.path.isfile(img_path):
        if os.path.isfile(pdf_path):
            print("extracting from pdf: " + str(i))
            images = convert_from_path(pdf_path, first_page=1, last_page=1)
            for image in images:
                image.save(img_path, "PNG")
    else:
        print(f"Thumbnail voor {img_path} bestaat al, skipping...")
