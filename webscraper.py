import requests
from bs4 import BeautifulSoup
import random
import datetime
random_num=random.randint(1,9999999)

response=requests.get('https://pixelford.com/blog/',headers={'user_agent':f'{random_num}'})
html=response.content
soup=BeautifulSoup(html,'html parser')

blogs=BeautifulSoup.find_all('article',class_='type-post')

#for tag in a_tags:
    #print(tag.get_text())


#titles=list(map(lambda tag:tag.get_text(),a_tags))
#print(titles)

for blog in blogs:
    title=blog.find('a',class_='reference-link').get_text()
    date_tags=blog.find('time',class_='time-post').get('datetime')
    blog_date_format=datetime.datetime.isoformat(date_tags)
    blog_date_time=blog_date_format.strftime("%b %d %Y")

    print(f'{title}-{blog_date_time}')




