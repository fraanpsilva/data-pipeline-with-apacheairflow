import os  # biblioteca para manipulação de arquivos e caminhos
from datetime import datetime, timedelta  # manipulação de datas
from os.path import join  # função para juntar caminhos

import pandas as pd  # biblioteca para manipulação de datafram

# definindo as variáveis para a url da api

# intervalo de datas
data_inicio = datetime.today()
data_fim = data_inicio + timedelta(days=7)

# formatando datas
data_inicio = data_inicio.strftime('%Y-%m-%d')
data_fim = data_fim.strftime('%Y-%m-%d')

city = 'Boston'
key = 'JK935MN73WSTV8B5H6KT6QNNW'

# url da API
URL = join('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/',
           f'{city}/{data_inicio}/{data_fim}?unitGroup=metric&include=days&key={key}&contentType=csv')

# parametros adicionados na url
# unitGroup=metric - sistema de unidades que queremos como os dados venham
# include=days - para os dados vir condensados em dias e nã em horas
# contentType=csv - especificar o formato que quero que os dados venham (pode ser em JSON tbm)

# lendo os dados
dados = pd.read_csv(URL)
print(dados.head)

# salvando os arquivos
file_path = f'/Users/francilenesilva/Documents/data-engineer/apache-airflow/orquestrando-pipeline1/data-pipeline/semana={data_inicio}/'
# criando uma pasta
os.mkdir(file_path)

# salvando o arquivo em csv
dados.to_csv(file_path + 'dados_brutos.csv') # dando nome ao arquivo
# salvando os arquivos com as informações relevantes
dados [['datetime', 'tempmin', 'temp', 'tempmax']].to_csv(file_path + 'temperatura.csv')
dados[['datetime', 'description', 'icon']].to_csv(file_path + 'condicoes.csv')




