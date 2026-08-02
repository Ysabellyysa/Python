#Biblioteca utilizadas 
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
from datetime import datetime

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
    schedule='@daily',# roda uma vez por dia
    catchup=False,
    tags=['aula', 'trigger_rule']
) as dag:

    coleta_crm = PythonOperator(
        task_id='coletar_dados_crm',
        python_callable=coletar_dados_crm,
        trigger_rule='all_success'   # roda só se todas upstream tiverem sucesso
    )

    coleta_erp = PythonOperator(
        task_id='coletar_dados_erp',
        python_callable=coletar_dados_erp,
        trigger_rule='all_success'
    )

    alerta_falha = PythonOperator(
        task_id='tratar_falha_coleta',
        python_callable=tratar_falha_coleta,
        trigger_rule='one_failed'# dispara se pelo menos uma upstream falhar
    )

    consolidar = PythonOperator(
        task_id='consolidar_dados',
        python_callable=consolidar_dados,
        trigger_rule='none_failed' # dispara se nenhuma upstream falhou 
    )

    gerar = PythonOperator(
        task_id='gerar_relatorio',
        python_callable=gerar_relatorio,
        trigger_rule='all_done' # dispara independente de sucesso ou falha, só espera terminar
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

    [coleta_crm, coleta_erp] >> [alerta_falha, consolidar]   # as duas coletas alimentam, alerta e consolida
    [alerta_falha, consolidar] >> gerar                      # gerar espera ambos os caminhos
    gerar >> [notif_sucesso, notif_falha]                    # depois dispara as duas notificações 
