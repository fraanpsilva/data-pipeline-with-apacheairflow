from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

with DAG(
    'atividade_aula_4',
    start_date=days_ago(1),
    schedule_interval='@daily'
) as dag:

# função python
 def cumprimentos():
    print("Boas-vindas ao Airflow!")

# definindo as tasks(tarefas)
tarefa = PythonOperator(
    task_id = 'cumprimentos',
    python_callable=cumprimentos
)

