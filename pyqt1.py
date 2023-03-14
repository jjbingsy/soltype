from bs4 import BeautifulSoup

# Create a new BeautifulSoup object with an empty HTML document



jsoup = BeautifulSoup('<html><body></body></html>', 'html.parser')

# Create a new div tag with the image and description
div_tag = jsoup.new_tag('div', style='display: flex; align-items: center;')
img_tag = jsoup.new_tag('img', src='https://cdn.javsts.com/wp-content/uploads/2023/02/midv252pl.jpg', style='width: 511px; height: 343px; object-fit: cover; margin-right: 10px;')
desc_tag = jsoup.new_tag('p')
desc_tag.string = 'My Image Description'
div_tag.append(img_tag)
div_tag.append(desc_tag)

# Add the div tag to the body tag
jsoup.body.append(div_tag)

# Create a new ul tag with the bullet list items
ul_tag = jsoup.new_tag('ul')
for item in ['Item 1', 'Item 2', 'Item 3']:
    li_tag = jsoup.new_tag('li')
    li_tag.string = item
    ul_tag.append(li_tag)

# Add the ul tag to the body tag
jsoup.body.append(ul_tag)

# Print the modified soup
#print(soup.prettify())
with open('list2.html', 'w') as f:
    f.write(jsoup.prettify())