########## WEB SCRAPING ##########
import requests
from bs4 import BeautifulSoup
import pprint

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
subtext = soup.select('.subtext')

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key = lambda k : k['votes'])

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title' : title, 'link' : href, 'votes' : points})        
    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(links, subtext))