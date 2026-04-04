from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime

with DAG(
    dag_id='minha_dag_de_estudo',
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False
) as dag:

    tarefa_inicio = EmptyOperator(task_id='comecar_estudo')
    tarefa_fim = EmptyOperator(task_id='terminar_estudo')

    tarefa_inicio >> tarefa_fim