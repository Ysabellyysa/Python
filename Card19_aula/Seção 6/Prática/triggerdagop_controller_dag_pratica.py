from airflow import DAG
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from datetime import datetime

default_args = {
    'owner': 'Marya',
    'start_date': datetime(2019, 1, 1),
}

def preparar_dados():
    print("Dados do pedido validados!")

with DAG(
    dag_id='triggerdagop_pratica',
    default_args=default_args,
    schedule='@once',
    catchup=False,
    tags=['aula', 'trigger_dagrun']
) as dag:

    preparar = PythonOperator(
        task_id='dados_pedido',
        python_callable=preparar_dados
    )

    disparar = TriggerDagRunOperator(
        task_id='processamento_pedido',
        trigger_dag_id='triggerdagop_pratica',  
        conf={
            'pedido_id': 'PED-2019-001',
            'valor': 150.00,
            'cliente': 'Marya'
        },
        wait_for_completion=False  
    )

    fim = EmptyOperator(task_id='fim')

    preparar >> disparar >> fim
