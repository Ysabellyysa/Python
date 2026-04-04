from airflow import DAG 
from datetime import datetime, timedelta 
from airflow.providers.http.sensors.http import HttpSensor 
from airflow.sensors.filesystem import FileSensor 
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.providers.apache.hive.operators.hive import HiveOperator 
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.operators.email import EmailOperator 
from airflow.operators.slack import SlackWebhookOperator 
import json
import csv
import requests 

# Configurações padrão da DAG
default_args = {
    "owner": "airflow",
    "start_date": datetime(2026, 4, 2), # Ajustado para sua data atual
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}

def download_rates():
    # Caminho absoluto dentro do container Docker do Astro
    base_path = '/usr/local/airflow/dags/files'
    try:
        with open(f'{base_path}/forex_currencies.csv') as f:
            reader = csv.DictReader(f, delimiter=';')
            for row in reader:
                base = row['base']
                res = requests.get(f'https://api.exchangeratesapi.io/latest?base={base}').json()
                outdata = {'base': base, 'rates': res['rates'], 'last_update': res['date']}
                with open(f'{base_path}/forex_rates.json', 'a') as outfile:
                    json.dump(outdata, outfile)
                    outfile.write('\n')
    except Exception as e:
        print(f"Erro no processamento: {e}")

with DAG(
    dag_id="forex_data_pipeline", 
    schedule="@daily",          
    default_args=default_args, 
    catchup=False
) as dag:
    
    # 1. Verifica se a API de moedas está online
    is_forex_rates_available = HttpSensor(
        task_id="is_forex_rates_available",
        method="GET",
        http_conn_id="forex_api",
        endpoint="latest",
        response_check=lambda response: "rates" in response.text,
        poke_interval=5,
        timeout=20
    )

    # 2. Verifica se o arquivo CSV existe na pasta dags/files
    is_forex_currencies_file_available = FileSensor(
        task_id="is_forex_currencies_file_available",
        fs_conn_id="forex_path",
        filepath="forex_currencies.csv",
        poke_interval=5,
        timeout=20 
    )

    # 3. Executa a função Python para baixar os dados
    downloading_rates = PythonOperator(
        task_id="download_forex_rates",
        python_callable=download_rates
    )

    # 4. Salva o JSON no HDFS (Simulado no curso)
    saving_rates = BashOperator(
        task_id="saving_rates",
        bash_command="""
            hdfs dfs -mkdir -p /forex_data && \
            hdfs dfs -put -f /usr/local/airflow/dags/files/forex_rates.json /forex_data
        """
    )

    # 5. Cria a tabela no Hive
    creating_table = HiveOperator(
        task_id="creating_forex_rates_table",
        hive_cli_conn_id="hive_conn",
        hql="""
            CREATE EXTERNAL TABLE IF NOT EXISTS forex_rates(
                base STRING, last_update DATE, eur DOUBLE, usd DOUBLE, 
                nzd DOUBLE, gbp DOUBLE, jpy DOUBLE, cad DOUBLE
            )
            ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' STORED AS TEXTFILE
        """
    )

    # 6. Processamento Spark
    forex_processing = SparkSubmitOperator(
        task_id="forex_processing",
        conn_id="spark_conn",
        application="/usr/local/airflow/dags/scripts/forex_processing.py", 
        verbose=False 
    )

    # 7. Notificação de Sucesso (Usa a Senha de App que você gerou!)
    sending_email_notification = EmailOperator(
        task_id="sending_email",
        to="airflow_course@yopmail.com",
        subject="forex_data_pipeline",
        html_content="<h3>forex_data_pipeline succeeded</h3>"
    )

    sending_slack_notification = SlackWebhookOperator(
        task_id="sending_slack",
        token="xoxb-10859138721057-10844214000806-lmy7akEfu7oX9caQu7SXduWH"
        username="airfloew",
        text="DAG forex_data_pipeline: Done",
        channel="#airflow-exploit"
        

    )

#is_forex_currencies_file_available >> downloading_rates >> saving_rates >> creating_table >> forex_processing >> sending_email_notification

downloading_rates >> sending_email_notification
is_forex_rates_available >> is_forex_currencies_file_available >> downloading_rates >> saving_rates >> creating_table >> forex_processing >> sending_email_notification