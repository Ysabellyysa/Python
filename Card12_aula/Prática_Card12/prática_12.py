from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime

def _processamento_final():
    print("Processamento concluído")

with DAG('dag_pratica_simples', 
    start_date=datetime(2024, 1, 1), 
    schedule_interval='@once', 
    catchup=False) as dag:

    # Cria uma pasta 
    tarefa_criar_pasta = BashOperator(
        task_id='criar_pasta',
        bash_command='mkdir -p /opt/airflow/dags/saida_pratica'
    )

    #Escreve um log com a data atual dentro de um arquivo
    tarefa_gerar_arquivo = BashOperator(
        task_id='gerar_arquivo',
        bash_command='echo "Executado em: $(date)" > /opt/airflow/dags/saida_pratica/log_sucesso.txt'
    )

    #Executa a função 
    tarefa_python = PythonOperator(
        task_id='aviso_final',
        python_callable=_processamento_final
    )

    # Definindo a ordem das tarefas
    tarefa_criar_pasta >> tarefa_gerar_arquivo >> tarefa_python
