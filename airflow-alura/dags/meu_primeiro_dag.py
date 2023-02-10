# criando o primeiro dag

from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.empty import EmptyOperator
from airflow.utils.dates import days_ago

with DAG(
    'meu_primeiro_dag', #dag id
    start_date=days_ago(2), #data que o dag começará a ser executado
    schedule_interval='@daily' #intervalo de agendamento do DAG
) as dag:

    # definindo as tasks(tarefas)
    tarefa_1 = EmptyOperator(task_id = 'tarefa_1')
    tarefa_2 = EmptyOperator(task_id = 'tarefa_2')
    tarefa_3 = EmptyOperator(task_id = 'tarefa_3')
    tarefa_4 = BashOperator(
        task_id = 'cria_pasta',
        bash_command = 'mkdir -p  "/Users/francilenesilva/Documents/data-engineer/apache-airflow/orquestrando-pipeline1/data-pipeline/airflow-alura/pasta={{data_interval_end}}" '
    )

    # definindo o fluxo de execução das tarefas
    tarefa_1 >> [tarefa_2, tarefa_3]
    tarefa_3 >> tarefa_4
