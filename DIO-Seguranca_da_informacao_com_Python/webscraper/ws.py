from bs4 import BeautifulSoup

import requests

site = requests.get('https://www.climatempo.com.br/').content
#objeto site recebendo o conteudo da requisição http do site ...
soup = BeautifulSoup(site, 'html.parser')
#objeto soup, baixando do site html
#print(soup.prettify())
#transforma o html em string e o print vai exibir o html

temperatura = soup.find('p', class_="-gray _flex _align-center")

print(temperatura.string)

print(soup.p.string)

print(soup.find('admin'))

