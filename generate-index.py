#!/usr/bin/env python3
"""

"""
import os
import re
import highest
# Calculate the highest numbered pdf and take its humber.
MAX :int = highest.find_highest_numbered_pdf()

# The string for a gallery item.
gallery_item = '<a href="{pdf}" target="_blank"><img src="./img/{i}.png" alt="Title page of edition {i}"></a>'

def generate_gallery():
    """
    """
    editions_html = []
    for i in range(MAX + 1,-1, -1):
        pdf_file = f'./pdf/{i}.pdf'
        if os.path.isfile(pdf_file):
            editions_html.append(gallery_item.format(pdf=pdf_file, i=i))
    return '\n'.join(editions_html)

with open("index.template.html") as template, open("index.html", "w") as index:
    replacement_string = r"""
    <p>YOU HAVE LANDED ON THE TEMPLATE PAGE OF <a href="./index.html">INDEX.HTML</a> THIS PARAGRAPH WILL BE REPLACED WITH THE GENERATED GALLERY!</p>
    """.strip()
    index.write(re.sub(replacement_string, generate_gallery(), template.read()))
