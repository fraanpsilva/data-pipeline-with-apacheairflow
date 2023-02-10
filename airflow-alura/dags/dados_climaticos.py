# implementando um dag
from os.path import join

import pandas as pd
import pendulum
from airflow import DAG
from airflow.macros import ds_add
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

with DAG(
    "dados_climaticos",
    start_date=pendulum.datetime(2023, 1, 22, tz="UTC"),
    schedule_interval='0 0 * * 1', # executar toda segunda feira
) as dag:

    tarefa_1 = BashOperator(
        task_id = 'cria_pasta',
        bash_command = 'mkdir -p  "/Users/francilenesilva/Documents/data-engineer/apache-airflow/orquestrando-pipeline1/data-pipeline/airflow-alura/semana={{data_interval_end.strftime("%Y-%m-%d")}}"'

    )

    def extrai_dados(data_interval_end):
        city = 'Boston'
        key = 'ANZQ5K8QQP8BXZ85F4ZEQ2FPK'

        URL = join('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}/{data_interval_end}/{ds_add(data_interval_end, 7)}?unitGroup=metric&include=days&key={key}&contentType=csv')    
        dados = pd.read_csv(URL)

        file_path = f'/Users/francilenesilva/Documents/data-engineer/apache-airflow/orquestrando-pipeline1/data-pipeline/airflow-alura/semana={data_interval_end}/'


        dados.to_csv(file_path + 'dados_brutos.csv')
        dados[['datetime','tempmin', 'temp', 'tempmax']].to_csv(file_path + 'temperaturas.csv')
        dados[['datetime', 'description', 'icon']].to_csv(file_path + 'condicoes.csv')

    tarefa_2 = PythonOperator(
        task_id = 'extrai_dados',
        python_callable = extrai_dados,
        op_kwargs = {'data_interval_end': '{{data_interval_end.strftime("%Y-%m-%d")}}'}
    )

    tarefa_1 >> tarefa_2

"""from datetime import datetime, timedelta
from os.path import join

import pandas as pd
import pendulum  # biblioteca para definir uma data específica
from airflow.macros import ds_add
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

# definindo o DAG
with DAG (
    "dados_climaticos",
    start_date=pendulum.datetime(2022, 12, 22, tz="UTC"),
    schedule_interval = '0 0 * * 1' # vai executar toda segunda feira (min hora dia mes dia_semana)
) as dag:

    # definindo as tarefas
    tarefa_1 = BashOperator(
        task_id = 'cria_pasta',
        bash_command = 'mkdir -p  "/Users/francilenesilva/Documents/data-engineer/apache-airflow/orquestrando-pipeline1/data-pipeline/airflow-alura/semana={{data_interval_end}}"'
    )

    # função pyhton
    def extrai_dados(data_interval_end):
        city = 'Boston'
        key = 'JK935MN73WSTV8B5H6KT6QNNW'

        # url da API
        URL = join('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/',
                f'{city}/{data_interval_end}/{ds_add(data_interval_end, 7)}?unitGroup=metric&include=days&key={key}&contentType=csv')

        # lendo os dados
        dados = pd.read_csv(URL)

        # salvando os arquivos
        file_path = f'/Users/francilenesilva/Documents/data-engineer/apache-airflow/orquestrando-pipeline1/data-pipeline/airflow-alura/semana={data_interval_end}/'

        # salvando o arquivo em csv
        dados.to_csv(file_path + 'dados_brutos.csv') # dando nome ao arquivo
        # salvando os arquivos com as informações relevantes
        dados [['datetime', 'tempmin', 'temp', 'tempmax']].to_csv(file_path + 'temperatura.csv')
        dados[['datetime', 'description', 'icon']].to_csv(file_path + 'condicoes.csv')

    tarefa_2 = PythonOperator(
        task_id = 'extrai_dados',
        python_callable = extrai_dados, 
        op_kwargs = {'data_interval_end' : '{{data_interval_end.strftime("%Y-%m-%d)}}'} # aqui onde passamos o jinja templates para usar na função python
    )

    tarefa_1 >> tarefa_2 """

