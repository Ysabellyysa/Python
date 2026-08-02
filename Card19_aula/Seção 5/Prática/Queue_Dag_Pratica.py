#Bibliotecas utilizadas
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2019, 1, 1),
    'owner': 'Marya',
}

with DAG(
    dag_id='queue_dag_pratica',
    schedule=None,
    default_args=default_args,
    catchup=False,
    tags=['aula', 'infra']
) as dag:

    tarefa_comum = BashOperator(
        task_id='tarefa_geral',
        bash_command='echo "Rodando worker padrão"',
        queue='default'  # fila do Celery que o worker precisa escutar
    )

    tarefa_especifica = BashOperator(
        task_id='tarefa_pesada_especial',
        bash_command='echo "Rodando máquina de alta performance"',
        queue='high_mem_queue'# exige um worker dedicado escutando essa fila
    )

    [tarefa_comum, tarefa_especifica]   # apenas lista as duas não cria dependência real
