from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import BranchPythonOperator, PythonOperator
from datetime import datetime

# Branch DAG
default_args = {
    'owner': 'Marya',
    'start_date': datetime(2019, 1, 1),
}

def verificar_tipo_pedido(**context):
    valor = 150  
    if valor < 100:
        return 'pedido_pequeno'
    elif valor < 500:
        return 'pedido_medio'
    else:
        return 'pedido_grande'

def processar_pequeno():
    print("Pedido pequeno: envio padrão")

def processar_medio():
    print("Pedido médio: envio expresso")

def processar_grande():
    print("Pedido grande: envio prioritário")

def finalizar_pedido():
    print("Pedido registrado e confirmação enviado ao cliente!")

with DAG(
    dag_id='branch_pratica_dag',
    default_args=default_args,
    schedule=None,  
    catchup=False,
    tags=['aula', 'branch']
) as dag:

    inicio = EmptyOperator(task_id='inicio')  # EmptyOperator substitui DummyOperator 

    branch = BranchPythonOperator(
        task_id='verificar_tipo_pedido',
        python_callable=verificar_tipo_pedido
    )

    pequeno = PythonOperator(task_id='pedido_pequeno', python_callable=processar_pequeno)
    medio   = PythonOperator(task_id='pedido_medio',   python_callable=processar_medio)
    grande  = PythonOperator(task_id='pedido_grande',  python_callable=processar_grande)
    
    # garantir q o end roda
    fim = EmptyOperator(
        task_id='fim',
        trigger_rule='none_failed_min_one_success'
    )

    inicio >> branch
    branch >> [pequeno, medio, grande]
    [pequeno, medio, grande] >> fim
