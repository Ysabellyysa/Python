#Bibliotecas utilizadas
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import BranchPythonOperator, PythonOperator  # branch decide qual caminho seguir
from datetime import datetime

default_args = {
    'owner': 'Marya',
    'start_date': datetime(2019, 1, 1),
}

def verificar_tipo_pedido(**context):
    valor = 150  # valor fixo 
    if valor < 100:
        return 'pedido_pequeno' # retorna o task_id que deve rodar em seguida
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

def finalizar_pedido():  # função definida 
    print("Pedido registrado e confirmação enviado ao cliente!")

with DAG(
    dag_id='branch_pratica_dag',
    default_args=default_args,
    schedule=None,
    catchup=False,
    tags=['aula', 'branch']
) as dag:

    inicio = EmptyOperator(task_id='inicio')

    branch = BranchPythonOperator(
        task_id='verificar_tipo_pedido',
        python_callable=verificar_tipo_pedido # o retorno da função decide qual task_id segue
    )

    pequeno = PythonOperator(task_id='pedido_pequeno', python_callable=processar_pequeno)
    medio   = PythonOperator(task_id='pedido_medio',   python_callable=processar_medio)
    grande  = PythonOperator(task_id='pedido_grande',  python_callable=processar_grande)

    fim = EmptyOperator(
        task_id='fim',
        trigger_rule='none_failed_min_one_success'
        # roda mesmo com os outros 2 caminhos skipped, desde que pelo menos 1 tenha sucesso
    )

    inicio >> branch
    branch >> [pequeno, medio, grande] # branch aponta pra todas, mas só uma de fato executa
    [pequeno, medio, grande] >> fim  # todas convergem pro fim
