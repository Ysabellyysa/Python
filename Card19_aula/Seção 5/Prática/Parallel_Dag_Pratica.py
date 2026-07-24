from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

#onfigurações básicas da DAG
#
default_args = {
    'start_date': datetime(2019, 1, 1),
    'owner': 'Marya',
}

def tarefa_paralela(id_task):
    print(f"Executando processo paralelo: {id_task}")

def finalizar():
    print("Todas as frentes foram concluidas!")

with DAG(dag_id='parallel_pratica_dag', schedule=None, default_args=default_args, catchup=False) as dag:

    #Cria 3 tarefas 
    processos = [
        PythonOperator(
            task_id=f'processo_paralelo_{i}',
            python_callable=tarefa_paralela,
            op_args=[i]
        ) for i in range(1, 4)
    ]

    #aguarda os processos 
    conclusao = PythonOperator(
        task_id='conclusao_geral',
        python_callable=finalizar
    )

    # o fluxo
    processos >> conclusao
