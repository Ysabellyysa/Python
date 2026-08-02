#Bibliotecas adicionadas 
from airflow import DAG
from airflow.operators.trigger_dagrun import TriggerDagRunOperator  # operator que dispara outra DAG
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
    schedule='@once',# roda uma única vez, quando ativada
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
        conf={    # dicionário enviado como 'conf' ao DAG disparado
            'pedido_id': 'PED-2019-001',
            'valor': 150.00,
            'cliente': 'Marya'
        },
        wait_for_completion=False  # não espera a DAG disparada terminar para seguir
    )

    fim = EmptyOperator(task_id='fim') #marca o fim da pipeline

    preparar >> disparar >> fim # define a ordem de execução 
