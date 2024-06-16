from collections.abc import Mapping
from nbconvert import HTMLExporter
import nbformat
import sys
import os.path

notebook_filename = sys.argv[1]
html_filename = sys.argv[2]

if not os.path.isfile(notebook_filename):
	exit('Cannot find {}'.format(notebook_filename))

print('Converting {} to {}'.format(notebook_filename, html_filename))

# Load the notebook (.ipynb file)
with open(notebook_filename, 'r', encoding='utf-8') as f:
    notebook_content = nbformat.read(f, as_version=4)

# Configure the HTMLExporter
html_exporter = HTMLExporter()

# Convert notebook to HTML
(body, resources) = html_exporter.from_notebook_node(notebook_content)

# Save the HTML content to a file
with open(html_filename, 'w', encoding='utf-8') as f:
    f.write(body)

print(f'Notebook converted to HTML: {html_filename}')
