import requests
from _settings import ibov
from bs4 import BeautifulSoup


ticker = ibov[0]
url = f'https://www.google.com/search?q={ticker}&sxsrf=AJOqlzWBR3DgjOJZnL0kU_Gzd1XxsDEYuA:1677803825775&source=lnms&tbm=nws&sa=X&ved=2ahUKEwjl3aaowr79AhWEGbkGHQbDC2kQ_AUoAnoECAEQBA&biw=2400&bih=1184&dpr=0.8'


# r = requests.get(url)

# salva os dados da pesquisa em um arquivo html
# with open(f'search_{ticker}.html', 'w', enconding='utf-8') as f:
#    f.write(r.text)

with open(f'search_{ticker}.html', 'r', encoding='latin-1') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
h3 = soup.find_all('h3')
span = soup.find_all('span')
links = soup.find_all('a', href=True)

i = 0
for link in links:
    if ticker in link['href']:
        print(i, link['href'])

        i += 1

# for title in span:
#    print(title.text)



# earch = soup.find(id='search')
# print(search.text)
# for result in search.find_all('div'):
#    print(result.text)
