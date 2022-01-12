from bs4 import BeautifulSoup as BS
import requests as R
ry=R.get('https://www.worldometers.info/coronavirus/',auth=('user', 'pass'))
ry.status_code
soup = BS(ry.text, 'html.parser')
total = soup.find("div", class_ = "maincounter-number").text
total = total[1 : len(total) - 2] 
other = soup.find_all("span", class_ = "number-table")
recovered = other[2].text   
deaths = other[3].text   
deaths = deaths[1:]
ans ={'Total Cases' : total, 'recovered cases' : recovered,'Total Deaths' : deaths}
print("Total Cases",ans['Total Cases'])
print("Recovered Cases",ans['recovered cases'])
print("Total deaths",ans['Total Deaths'])





