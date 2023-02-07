import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://zenit.games/priston/ranking.php"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Encontrando a lista com os dados do ranking
table = soup.find("div", attrs={"class": "listaRanking"})

# Definindo os atributos do elemento que será filtrado
attributes = ["posicaoRanking", "servidorRanking", "nickRanking", "persRanking", "nivelRanking"]

# Filtrando os dados de acordo com os atributos definidos
rows = table.find_all("span", attrs={"class": attributes})

# Transformando a lista filtrada em uma string
html_string = str(rows)

soups = BeautifulSoup(html_string, 'html.parser')

# Encontrando todos os elementos <span>
spans = soups.find_all('span', attrs={"class": attributes})

# Inicializando as listas para armazenar os dados
posicao = []
servidor = []
nick = []
pers = []
nivel = []

# loop por todos os elementos <span>
for i in range(0, len(spans), 5):
    posicao.append(spans[i].text)
    servidor.append(spans[i+1].text)
    nick.append(spans[i+2].text)
    pers.append(spans[i+3].text)
    nivel.append(spans[i+4].text)

# criando o dataframe com os dados extraídos
df = pd.DataFrame({'RANK': posicao, 'SERVIDOR': servidor, 'PERSONAGEM': nick, 'CLASSE': pers, 'LEVEL': nivel})

# exibe o dataframe
print(df)