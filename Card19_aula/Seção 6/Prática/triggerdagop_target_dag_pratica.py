from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
from datetime import datetime

default_args = {
    'owner': 'Marya',
    'start_date': datetime(2019, 1, 1),
}

def processar_pedido(**context):
    conf = context['dag_run'].conf
    pedido_id = conf.get('pedido_id', 'desconhecido')
    valor     = conf.get('valor', 0)
    cliente   = conf.get('cliente', 'desconhecido')

    print(f"Processando pedido {pedido_id} do cliente {cliente}")
    print(f"Valor total: R$ {valor:.2f}")

    if valor >= 300:
        print("Pedido aprovado, cupom frete grátis!")
    else:
        print("Frete será calculado!")

def registrar_no_banco(**context):
    conf = context['dag_run'].conf
    pedido_id = conf.get('pedido_id', 'desconhecido')
    print(f"Pedido {pedido_id} registrado no banco de dados com sucesso.")

with DAG(
    dag_id='triggerdagop_pratica',
    default_args=default_args,
    schedule=None, 
    catchup=False,
    tags=['teste', 'trigger_dagrun']
) as dag:

    processar = PythonOperator(
        task_id='processar_pedido',
        python_callable=processar_pedido
    )

    registrar = PythonOperator(
        task_id='registrar_banco',
        python_callable=registrar_banco
    )

    confirmar = BashOperator(
        task_id='confirmar_processamento',
        bash_command='echo "Pedido {{ dag_run.conf[\"pedido_id\"] if dag_run.conf else \"\" }} confirmado!"'
    )

    fim = EmptyOperator(task_id='fim')

    processar >> registrar >> confirmar >> fim
