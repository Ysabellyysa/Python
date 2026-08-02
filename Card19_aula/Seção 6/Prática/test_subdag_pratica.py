#bibliotecas utilizadas 
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from airflow.operators.subdag import SubDagOperator # operator legado para aninhar DAGs 
from datetime import datetime

default_args = {
    'start_date': datetime(2019, 1, 1),
    'owner': 'Marya',
}

DAG_NAME = 'subdag_pratica_dag'   # nome base usado tanto na DAG pai quanto nos subdags

def subdag_validacao(parent_dag_name, child_dag_name, args):
    # função-fábrica que constrói e retorna um DAG filho
    subdag = DAG(
        dag_id=f'{parent_dag_name}.{child_dag_name}',  # convenção obrigatória pai e filho
        default_args=args,
        schedule='@once',
    )

    def checar_nulos():
        print("Verificando campos nulos")

    def checar_duplicatas():
        print("Verificando registros duplicados")

    checar_nulos_task = PythonOperator(
        task_id='checar_nulos',
        python_callable=checar_nulos,
        dag=subdag  # associa a task ao subdag explicitamente 
    )

    checar_duplicatas_task = PythonOperator(
        task_id='checar_duplicatas',
        python_callable=checar_duplicatas,
        dag=subdag
    )

    checar_nulos_task >> checar_duplicatas_task
    return subdag     # devolve o DAG pronto para o SubDagOperator usar

def subdag_relatorio(parent_dag_name, child_dag_name, args):
    subdag = DAG(
        dag_id=f'{parent_dag_name}.{child_dag_name}',
        default_args=args,
        schedule='@once',
    )

    def cria_pdf():
        print("Gerando relatório em PDF")

    def enviar_email():
        print("Enviando relatório por e-mail")

    gerar_pdf_task = PythonOperator(
        task_id='cria_pdf',
        python_callable=criar_pdf,                          
        dag=subdag
    )

    enviar_email_task = PythonOperator(
        task_id='enviar_email',
        python_callable=enviar_email,
        dag=subdag
    )

    gerar_pdf_task >> enviar_email_task                       
    return subdag

with DAG(
    dag_id=DAG_NAME,
    default_args=default_args,
    schedule='@once',
    catchup=False,
    tags=['aula', 'subdag']
) as dag:

    inicio = EmptyOperator(task_id='inicio')

    validacao = SubDagOperator(
        task_id='subdag_validacao',  # o task_id deve bater com o child_dag_name usado acima
        subdag=subdag_validacao(DAG_NAME, 'subdag_validacao', default_args)
    )

    relatorio = SubDagOperator(
        task_id='subdag_relatorio',
        subdag=subdag_relatorio(DAG_NAME, 'subdag_relatorio', default_args)
    )

    fim = EmptyOperator(task_id='fim') #marca o fim 

    inicio >> validacao >> relatorio >> fim # define a ordem de execuçã
