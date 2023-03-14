from pathlib import Path
from bs4 import BeautifulSoup

# Specify the directory path
directory = Path('G:/htmls')

# Loop through all the HTML files in the directory and print their titles
for file in directory.glob('*.html'):
    with open(file, 'r') as f:
        jsoup = BeautifulSoup('<html><head><title></title></head><body></body></html>', 'lxml')
        soup = BeautifulSoup(f.read(), 'lxml')
        ss = soup.find ('link', rel='canonical')    
        mainlink = ss['href']
        s = soup.title.string
        #s = 'This is [an example] string with [multiple] sets of [square brackets].'

        # Find the index of the first opening bracket
        start = s.find('[')
        body1 = jsoup.new_tag("div")
        body1["class"] = "item"
        img = soup.find('div', class_="large-screenimg")
        image =img.img['src']
        div_tag = jsoup.new_tag('div')
        a_tag = jsoup.new_tag('a', href=mainlink)
        img_tag = jsoup.new_tag('img', src=image, style='width: 511px; height: 343px; object-fit: cover; margin-right: 10px;')
        desc_tag = jsoup.new_tag('p')
        desc_tag ['style'] = "width: 511px"
        desc_tag.string = s
        a_tag.append(img_tag)
        div_tag.append(a_tag)
        

        # Add the div tag to the body tag
        body1.append(div_tag)
        body1.append(desc_tag)
        # Create a new ul tag with the bullet list items
        ul_tag = jsoup.new_tag('ul')





        # Find the index of the first closing bracket after the opening bracket
        end = s.find(']', start)

        # Extract the substring between the brackets
        substring = s[start+1:end].strip()

        # Print the original string and the extracted substring
        #print(f"Original string: {s}")
        #print(f"Substring inside first set of brackets: {substring}")
        #print(f"{substring}")
        idols = soup.find("div" , class_="infoleft").select('a[href*="jav.guru/actress/"]')
        series = soup.find("div" , class_="infoleft").select('a[href*="jav.guru/series/"]')



        print (len(series))
        if len(series) > 0:
            series_p = jsoup.new_tag('p')
            series_p.string = "Series: "
            series_tag = jsoup.new_tag ('a')
            series_tag.string = str(series[0].string )
            series_tag['href'] = series[0]['href']
            print (substring, "has a series", str(series[0]['href']), str(series[0].string ))
            series_p.append (series_tag)
            body1.append(series_p)

        for idol in idols:
            #print (idol['href'], idol.string.strip())
            li_tag = jsoup.new_tag('li')
            a_tag = jsoup.new_tag('a')
            a_tag['href'] = idol["href"]
            a_tag.string = idol.string.strip()
            li_tag.append(a_tag)
            ul_tag.append(li_tag)

        input_tag = jsoup.new_tag('input')
        input_tag['type'] = 'hidden'
        input_tag['source'] = 2
        input_tag['tilte'] = substring
        jsoup.title.string = substring
        input_tag['idol_count'] = len (series)
        body1.append(ul_tag)
        body1.append(input_tag)
        jsoup.body.append(body1)
        with open(f'g:/modi/{substring}.html', 'w') as f:
            f.write(jsoup.prettify())
            
        

