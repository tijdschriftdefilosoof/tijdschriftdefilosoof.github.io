#!/usr/bin/env python3
"""
"""
import os
from pdf2image import convert_from_path

import highest
# Generate the highest numebred pdf and take its number.
MAX : int = highest.find_highest_numbered_pdf()

# Generate and save the images.
imgs = []
for i in range(MAX + 1):
    # Build the paths
    pdf_path = f'./pdf/{i}.pdf'
    img_path = f'./img/{i}.png'
    # Remove an image file if it has no corresponding pdf,
    # Assume it is a leftover artefact.
    # The images should strictly supervene on the pdf's.
    # This uses a technique know as "shortcircuiting".
    os.path.isfile(img_path) and not os.path.isfile(pdf_path) and os.remove(img_path)
    # Generate the images, but look if they already exist, because this proces is costly.
    if not os.path.isfile(img_path):
        # We look if the pdf actually exiss and don't assume this.
        # So we can skip editions.
        if os.path.isfile(pdf_path):
            print("extracting from pdf: " + str(i))
            # Actually extract the image, well get an array back with one image in it.
            images = convert_from_path(pdf_path, first_page=1, last_page=1)
            # Loop through the array.
            for image in images:
                # Save the image.
                image.save(img_path, "PNG")
    else:
        # Report that we skipped the image.
        print(f"Thumbnail voor {img_path} bestaat al, skipping...")
