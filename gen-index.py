import os
import re
MAX = 88

gallery_item = '<a href="{pdf}" target="_blank"><img src="./img/{i}.png" alt="Title page of edition {i}"></a>'

def generate_stubs():
    editions_html = []
    for i in range(MAX + 1,0,-1):
        pdf_file = f'./pdf/{i}.pdf'
        if os.path.isfile(pdf_file):
            editions_html.append(gallery_item.format(pdf=pdf_file, i=i))
    return '\n'.join(editions_html)

with open("template.html") as template:
    print(re.sub(r"<!--GALLERY-->",generate_stubs(),template.read()))
