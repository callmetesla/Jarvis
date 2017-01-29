from lxml import html
import requests
def ne():
	response = requests.get('http://news.google.com')

	if (response.status_code == 200):

    		pagehtml = html.fromstring(response.text)

    		news = pagehtml.xpath('//h2[@class="esc-lead-article-title"] \
                          /a/span[@class="titletext"]/text()')
    
	file=open("news.txt",'w')
	file.write("\n".join(news).encode('utf-8'))
