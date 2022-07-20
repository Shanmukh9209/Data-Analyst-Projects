from bs4 import BeautifulSoup
import requests, openpyxl

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = "Top Rated Movies"
print(excel.sheetnames)
sheet.append(['Rank','Name','Year','Rating'])

source = requests.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")
source.raise_for_status()

soup = BeautifulSoup(source.text,"html.parser")

movies = soup.find("tbody",class_="llister-list").find_all("tr")

for movie in movies:
  name = movie.find("td",class_="titleColumn").a.text
  rank = movie.find("td",class_="titleColumn").get_text(strip=True).split(".")
  year = movie.find("td",class_="titleColumn").span.text.strip('()')
  rating = movie.find("td",class_="ratingColumn imdbRating").strong.text
  
  print(rank,name,year,rating)
  sheet.append([rank,name,year,rating])

  excel.save('IMDB movie ratings.xlsx')
