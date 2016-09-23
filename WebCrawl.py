from urllib import urlopen
from bs4 import BeautifulSoup

def crawl(url, source):
    soup = BeautifulSoup(urlopen(url))

    if(source == "Mashable"):
        title = str(soup.find('h1', {'class': 'title'}).text)
        paras_raw = soup.find('section', {'class': 'article-content'}).find_all('p')
    
        paras = []
        for para in paras_raw:
            paras.append(str(para.text))

    if(source == "TNW"):
        title = str(soup.find('h1', {'class': 'article-title'}).text)
        paras_raw = soup.find('div', {'class': 'articleBody'}).find_all('p')
    
        paras = []
        for para in paras_raw:
            paras.append(str(para.text))
            
    if(source == "Wired"):
        title = str(soup.find('h1', {'id': 'post-title'}).text)
        paras_raw = soup.find('div', {'class': 'content link-underline relative'}).find_all('p')
    
        paras = []
        for para in paras_raw:
            paras.append(str(para.text))

        
    return [title, paras, len(paras)]
