import requests, os, bs4

url = 'http://xkcd.com'
os.makedirs('xkcd',exist_ok=True)
while not url.endswith('#'):
    print('Downloaing comic')
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text)
    
    comicElement = soup.select('#comic img')
    if comicElement == []:
        print('Comic not found')
    else:
        comicURL = 'http:'+comicElement[0].get('src')
        print('downloading img %s...'%(comicURL))
        res = requests.get(comicURL)
        res.raise_for_status()
        
        imageFile = open(os.path.join('xkcd',os.path.basename(comicURL)),'wb')
        for meta in res.iter_content(100000):
            imageFile.write(meta)
        imageFile.close()
        
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com'+prevLink.get('href')
print('good')