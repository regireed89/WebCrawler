from pip._vendor import requests
from bs4 import BeautifulSoup



'''def github_repo_spider():
    url='https://github.com/regireed89?tab=repositories'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for link in soup.find_all('a',{'itemprop': 'name codeRepository'}):
        href = "http://github.com" + link.get('href')
        print(href)
        print(link.string)'''
        







def trello_spider():
    url='https://trello.com/b/AirLLYix/student-work-log-2017-2018'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for link in soup.find_all('a',{'class': 'list-card js-member-droppable ui-droppable'}):
        href = "https://trello.com" + link.get('href')
        print(href)
        print(link.string)



'''github_repo_spider()'''
trello_spider()
