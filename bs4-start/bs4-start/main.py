from bs4 import BeautifulSoup
import requests
response=requests.get("https://news.ycombinator.com/news")
print(response.status_code)
webpage=response.text
soup= BeautifulSoup(webpage,"html.parser")

title=soup.find_all(name="span"
                 ,class_="titleline")
article_text=[]
article_link=[]

for article in title:
    text=article.get_text()
    article_text.append(text)
    link=article.find("a").get("href")
    article_link.append(link)


print(article_text)
print(article_link)
points=soup.find_all(name="span",class_="score")
article_upvote=[int(points.get_text().split()[0] )for points in points]
print(article_upvote)
largest_number=max(article_upvote)
index=article_upvote.index(largest_number)
print(index)
print(article_text[index])
print(article_link[index])