import requests
from bs4 import BeautifulSoup
url = 'https://search-study-uk.britishcouncil.org/course/search-results.html?onlineFlag=Y&OnCampusNowFlag=Y&OnCampusLaterFlag=Y'

r = requests.get(url)
htmlContent = r.content

soup = BeautifulSoup(htmlContent, 'html.parser')
anchors = soup.find_all("a")
all_links =set()

for link in anchors:
    if(link.get('href') !="#"):
        all_links.add(link.get('href'))
        # print(link.get('href'))
        
print(all_links)

# print(soup.find_all('a'))
# print(htmlContent)
