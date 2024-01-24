import os
prefix = """
<!DOCTYPE html>
<html>
<head>
<style>
/* CSS for the overall layout, including the header and the image grid */
body {
  font-family: Arial, sans-serif;
}

.header {
  background-color: #f2f2f2;
  padding: 20px;
  text-align: center;
  font-size: 30px;
  color: #333;
}

.container {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 10px;
  padding: 10px;
}

.container a {
  display: block;
}

.container img {
  width: 100%;
  height: auto;
  aspect-ratio: 1 / 1.41;
  border-radius: 8px;
}

@media screen and (max-width: 600px) {
  .container {
    grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
  }
}
</style>
</head>
<body>
    <header class="header">
    	<h1>De Filosoof</h1>
    </header>
    <div class="container">
      <!-- 88 images wrapped in links -->
"""
#       <a href="https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf" target="_blank"><img src="https://via.placeholder.com/200x282" alt="Placeholder Image"></a>
#       <!-- [Repeat this line for all 88 images] -->
#       <a href="./pdf/88.pdf" target="_blank"><img src="https://via.placeholder.com/200x282" alt="Placeholder Image"></a>
#       <a href="./pdf/87.pdf" target="_blank"><img src="https://via.placeholder.com/200x282" alt="Placeholder Image"></a>

post = """
    </div>
</body>
</html>
"""

template = '<a href="{pdf}" target="_blank"><img src="./img/{i}.png" alt="Title page of edition {i}"></a>'


def generate_stubs():
    editions_html = []
    for i in range(88 + 1,0,-1):
        pdf_file = f'./pdf/{i}.pdf'
        if os.path.isfile(pdf_file):
            editions_html.append(template.format(pdf=pdf_file, i=i))
    return '\n'.join(editions_html)

# with index as open('index.html'):
#    index.write(prefix)
#    index.write(post)
print(prefix + generate_stubs() + post)
