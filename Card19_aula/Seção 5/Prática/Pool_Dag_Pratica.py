#Bibliotecas utilizadas 
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

#dono da DAG, data a partir da qual a DAG roda
default_args = {
    'start_date': datetime(2019, 1, 1),
    'owner': 'Marya',
}

with DAG(dag_id='pool_pratica_dag', schedule='@daily', default_args=default_args, catchup=False) as dag:

    t1 = BashOperator(task_id='carga_01', bash_command='sleep 5', pool='default_pool')  # limita concorrência via pool
    t2 = BashOperator(task_id='carga_02', bash_command='sleep 5', pool='default_pool')
    t3 = BashOperator(task_id='carga_03', bash_command='sleep 5', pool='default_pool')

    [t1, t2, t3]# apenas lista, sem dependência entre elas
