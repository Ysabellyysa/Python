#Biblioteca utilizadas 
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2019, 1, 1),
    'owner': 'Marya',
}

def tarefa_paralela(id_task):
    print(f"Executando processo paralelo: {id_task}")

def finalizar():
    print("Todas as frentes foram concluidas!")

with DAG(dag_id='parallel_pratica_dag', schedule=None, default_args=default_args, catchup=False) as dag:

    processos = [
        PythonOperator(
            task_id=f'processo_paralelo_{i}', # gera task_ids processo_paralelo_1, _2, _3
            python_callable=tarefa_paralela,
            op_args=[i]  # passa i como argumento posicional pra função
        ) for i in range(1, 4)  # list comprehension cria 3 operators
    ]

    conclusao = PythonOperator(
        task_id='conclusao_geral',
        python_callable=finalizar
    )

    processos >> conclusao  #  todas as 3 devem terminar antes de conclusao
