import requests

from bs4 import BeautifulSoup
response=requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
content=response.text
print(content)
films_list=[]
soup=BeautifulSoup(content,"html.parser")
films=soup.find_all("span",class_="content_content__i0P3p")
for film in films:

    name=film.select_one("h2 strong")
    if name is None:
        pass
    else:
       film=name.get_text()
       films_list.append(film)
for  list1 in (films_list[::-1]):
    print(list1)
    with open("movies.txt", mode="a") as file:
        file.write(list1)
        file.write("\n")