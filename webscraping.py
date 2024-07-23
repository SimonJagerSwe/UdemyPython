########## WEB SCRAPING ##########
import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
# print(res)
# print(res.text)

soup = BeautifulSoup(res.text, 'html.parser')
# print(soup)
# print(soup.body)
# print(soup.body.contents)
# print(soup.find_all('div'))
# print(soup.find_all('a'))
# print(soup.title)
# print(soup.find('a'))
# print(soup.find(id='score_20514755'))

# print(soup.select('.score'))
# print(soup.select('#score_20514755'))
# .titleline
# print(soup.select('.titleline')[0])
# print(votes[0])
# print(votes.get('score_20514755'))

links = soup.select('.titleline')
votes = soup.select('.score')

def create_custom_hn(links, votes):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        hn.append(title)
    return hn

print(create_custom_hn(links, votes))