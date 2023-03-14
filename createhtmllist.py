from bs4 import BeautifulSoup
from pathlib import Path
source = Path ("pink.html")
# Define the grid CSS
css = """
    .grid {
        display: grid;
        grid-template-columns: 600px 600px 600px;
        
        grid-gap: 10px;
    }
"""

# Create the BeautifulSoup object and add the grid CSS
with source.open('r') as ss:
    soup = BeautifulSoup(ss, 'lxml')

# Get the list of HTML files and create a block for each one
html_dir = Path('/home/bing/work/compilation/htmls')

for html_file in html_dir.glob('*.html'):
    with html_file.open() as f:
        html_contents = f.read()
        html_soup = BeautifulSoup(html_contents, 'lxml')
        body_contents = html_soup.body.contents
        mybody = body_contents[1]
        #print ("*******************************************************************************************************")
        soup.body.div.append (mybody)
        
# grid_div = soup.find('div', class_='grid')
# for block in blocks:
#     block_div = soup.new_tag('div')
#     for item in block:
#         block_div.append(item)
#     grid_div.append(block_div)

# Write the HTML file
with open('lissterrr.html', 'w') as f:
    f.write(str(soup))
