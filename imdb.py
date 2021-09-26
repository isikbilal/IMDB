# Kullanıcının girdiği rating değerinden büyük olan IMDB Top 250 deki filmleri listeleyen program.

import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/"

response = requests.get(url)

print(response)

html_content = response.content

soup = BeautifulSoup(html_content,"html.parser")

a = float(input("Rating'i giriniz: "))

for i in soup.find_all("td",{"class":"titleColumn"}):
    print(i)
    print("**********************************************")
    print(i.text)

filmTitles = soup.find_all("td",{"class":"titleColumn"})
filmRatings = soup.find_all("td",{"class":"ratingColumn imdbRating"})

print(len(filmTitles))
print(type(filmTitles))
#print(dir(filmTitles))

print(len(filmRatings))
print(type(filmRatings))


for title, rating in zip(filmTitles, filmRatings): # zip fonksiyonu iki tane listeyi eşleştirerek liste içerisinde demet (tuple) şeklinde bir yapı oluşturuyor. Bu sayede bizim her bir demetimizin içindeki 1. eleman başlık, 2. eleman da rating değerimiz olacak.
    
    title = title.text # ilk başta text leri almazsak strip ve replace ile diğer tag elementleri de hizalanmaya çalışır ve hata verir.
    title = title.strip() # baştaki ve sonraki boşlukları siler
    title = title.replace("\n","") # \n leri kaldırdık

    rating = rating.text ## ilk başta text leri almazsak strip ve replace ile diğer tag elementleri de hizalanmaya çalışır ve hata verir.
    rating = rating.strip() # baştaki ve sonraki boşlukları siler
    rating = rating.replace("\n","") # \n leri kaldırdık

    if (float(rating) > a):
        print("Film ismi: {} | Filmin Ratingi: {}".format(title,rating))
        print("*************************************")
    

