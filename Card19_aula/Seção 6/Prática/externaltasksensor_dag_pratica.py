from airflow import DAG
from airflow.sensors.external_task import ExternalTaskSensor 
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from datetime import datetime

#Dag aguardando processamento concluir
default_args = {
    'owner': 'Marya',
    'start_date': datetime(2019, 1, 1),
}

def liberar_envio():
    print("Pagamento confirmado!")

def notificar_cliente():
    print("Notificação enviada ao cliente!")

with DAG(
    dag_id='externalsensor_pratica_dag',
    default_args=default_args,
    schedule='@daily',
    catchup=False,
    tags=['aula', 'sensor']
) as dag:

    aguardar_pagamento = ExternalTaskSensor(
        task_id='aguardar_confirmacao_pagamento',
        external_dag_id='pagamentos_dag',       # DAG precisa finalizar pra continuar
        external_task_id='confirmar_pagamento', 
        mode='poke',      
        timeout=600,    
        poke_interval=30 
    )

    liberar = PythonOperator(
        task_id='liberar_envio',
        python_callable=liberar_envio
    )

    notificar = PythonOperator(
        task_id='notificar_cliente',
        python_callable=notificar_cliente
    )

    fim = EmptyOperator(task_id='fim')

    aguardar_pagamento >> liberar >> notificar >> fim
