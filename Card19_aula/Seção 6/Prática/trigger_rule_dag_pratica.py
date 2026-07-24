from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
from datetime import datetime

# Pipeline de geração de relatório 
default_args = {
    'owner': 'Marya',
    'start_date': datetime(2019, 1, 1),
}

def coletar_dados_crm():
    print("Coletando dados CRM")

def coletar_dados_erp():
    print("Coletando dados ERP")

def tratar_falha_coleta():
    print("ALERTA: Fonte de dados falha!")

def consolidar_dados():
    print("Nenhuma fonte falhou! Dando continuidade ao relatório")

def gerar_relatorio():
    print("Gerando relatório final independente do resultado das fontes")

def notificar_sucesso():
    print("Relatório gerado com sucesso!")

def notificar_falha():
    print("Relatório gerado com pendências!")

with DAG(
    dag_id='trigger_rule_pratica_dag',
    default_args=default_args,
    schedule='@daily',
    catchup=False,
    tags=['aula', 'trigger_rule']
) as dag:

    # Coleta paralela de duas fontes
    coleta_crm = PythonOperator(
        task_id='coletar_dados_crm',
        python_callable=coletar_dados_crm,
        trigger_rule='all_success' 
    )

    coleta_erp = PythonOperator(
        task_id='coletar_dados_erp',
        python_callable=coletar_dados_erp,
        trigger_rule='all_success'
    )

    alerta_falha = PythonOperator(
        task_id='tratar_falha_coleta',
        python_callable=tratar_falha_coleta,
        trigger_rule='one_failed'
    )

    consolidar = PythonOperator(
        task_id='consolidar_dados',
        python_callable=consolidar_dados,
        trigger_rule='none_failed'
    )

    gerar = PythonOperator(
        task_id='gerar_relatorio',
        python_callable=gerar_relatorio,
        trigger_rule='all_done'
    )

    notif_sucesso = PythonOperator(
        task_id='notificar_sucesso',
        python_callable=notificar_sucesso,
        trigger_rule='all_success'
    )

    notif_falha = PythonOperator(
        task_id='notificar_falha',
        python_callable=notificar_falha,
        trigger_rule='all_success'
    )

    [coleta_crm, coleta_erp] >> [alerta_falha, consolidar]
    [alerta_falha, consolidar] >> gerar
    gerar >> [notif_sucesso, notif_falha]
