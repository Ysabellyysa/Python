from airflow import DAG
from datetime import datetime, timedelta
from airflow.providers.http.sensors.http import HttpSensor
from airflow.sensors.filesystem import FileSensor
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.operators.email import EmailOperator
# from airflow.providers.apache.hive.operators.hive import HiveOperator  # Commented out - provider not installed
from airflow.providers.slack.operators.slack_webhook import SlackWebhookOperator
import json
import csv
import requests
import logging

# Configurações padrão da DAG
default_args = {
    "owner": "airflow",
    "email_on_failure": True,
    "start_date": datetime(2021, 1, 1),
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
}


def download_rates() -> None:
    """Download forex rates from API and save to JSON file."""
    base_path = "/opt/airflow/dags/files"

    # Create empty file
    with open(f"{base_path}/forex_rates.json", "w", encoding="utf-8") as f:
        pass

    try:
        with open(f"{base_path}/forex_currencies.csv", encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=";")
            for row in reader:
                base = row["base"]
                try:
                    response = requests.get(
                        f"https://api.exchangeratesapi.io/latest?base={base}",
                        timeout=10,
                    )
                    response.raise_for_status()
                    res = response.json()

                    # Validate response contains rates
                    if "rates" in res and "date" in res:
                        outdata = {
                            "base": base,
                            "rates": res["rates"],
                            "last_update": res["date"],
                        }
                        with open(
                            f"{base_path}/forex_rates.json",
                            "a",
                            encoding="utf-8",
                        ) as outfile:
                            json.dump(outdata, outfile)
                            outfile.write("\n")
                    else:
                        logging.warning(f"Invalid API response for {base}: {res}")
                except requests.RequestException as api_error:
                    logging.error(f"API request error for {base}: {api_error}")
                    raise
    except FileNotFoundError as file_error:
        logging.error(f"CSV file not found: {file_error}")
        raise
    except Exception as e:
        logging.error(f"Unexpected error during processing: {e}")
        raise


with DAG(
    dag_id="forex_data_pipeline",
    start_date=datetime(2026, 4, 2),
    schedule="@daily",
    default_args=default_args,
    catchup=True,
) as dag:
    # Verifica se a API de moedas está online
    is_forex_rates_available = HttpSensor(
        task_id="is_forex_rates_available",
        method="GET",
        http_conn_id="forex_api",
        endpoint="latest",
        response_check=lambda response: "rates" in response.text,
        poke_interval=5,
        timeout=20,
    )

    # Verifica se o arquivo CSV existe na pasta dags/files
    is_forex_currencies_file_available = FileSensor(
        task_id="is_forex_currencies_file_available",
        fs_conn_id="forex_path",
        filepath="forex_currencies.csv",
        poke_interval=5,
        timeout=20,
    )

    # Executa a função Python para baixar os dados
    downloading_rates = PythonOperator(
        task_id="download_forex_rates",
        python_callable=download_rates,
    )

    # Salva o JSON no HDFS
    saving_rates = BashOperator(
        task_id="saving_rates",
        bash_command="""
            hdfs dfs -mkdir -p /forex_data && \
            hdfs dfs -put -f /opt/airflow/dags/files/forex_rates.json /forex_data
        """,
    )

    # Cria a tabela no Hive
    creating_table = BashOperator(
        task_id="creating_forex_rates_table",
        bash_command="""
            hive -e "
                CREATE EXTERNAL TABLE IF NOT EXISTS forex_rates(
                    base STRING, last_update DATE, eur DOUBLE, usd DOUBLE,
                    nzd DOUBLE, gbp DOUBLE, jpy DOUBLE, cad DOUBLE
                )
                ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' STORED AS TEXTFILE
            "
        """,
    )

    # Carrega dados na tabela Hive
    # load_forex_rates_table = HiveOperator(  # Commented out - provider not installed
    #     task_id="load_forex_rates_table",
    #     hive_cli_conn_id="hive_conn",
    #     hql="""
    #         LOAD DATA LOCAL INPATH '/opt/airflow/dags/files/forex_rates.csv'
    #         OVERWRITE INTO TABLE forex_rates;
    #     """,
    # )

    load_forex_rates_table = BashOperator(
        task_id="load_forex_rates_table",
        bash_command="""
            echo "Loading data into Hive table (simulated)"
        """,
    )

    # Processamento Spark (descomente quando necessário)
    # forex_processing = SparkSubmitOperator(
    #     task_id="forex_processing",
    #     conn_id="spark_conn",
    #     application="/opt/airflow/dags/scripts/forex_processing.py",
    #     verbose=False,
    # )

    # Notificação de Sucesso por Email
    sending_email_notification = EmailOperator(
        task_id="sending_email",
        to="airflow_course@yopmail.com",
        subject="forex_data_pipeline",
        html_content="<h3>forex_data_pipeline succeeded</h3>",
    )

    # Notificação de Sucesso por Slack
    sending_slack_notification = SlackWebhookOperator(
        task_id="sending_slack",
        slack_webhook_conn_id="slack_conn",
        message="DAG forex_data_pipeline: Done",
        channel="#airflow-exploit",
        username="airflow",
    )

    # Define a ordem de execução das tasks
    (
        is_forex_rates_available
        >> is_forex_currencies_file_available
        >> downloading_rates
        >> saving_rates
        >> creating_table
        >> load_forex_rates_table
        >> [sending_email_notification, sending_slack_notification]
    )
# Duplicate imports removed - already imported at top
# from airflow import DAG
# from datetime import datetime, timedelta
# from airflow.providers.http.sensors.http import HttpSensor
# from airflow.sensors.filesystem import FileSensor
# from airflow.operators.python import PythonOperator
# from airflow.operators.bash import BashOperator
# from airflow.operators.email import EmailOperator
# from airflow.providers.apache.hive.operators.hive import HiveOperator  # Commented out - provider not installed
# from airflow.providers.slack.operators.slack_webhook import SlackWebhookOperator
# # from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
# import json
# import csv
# import requests
# import logging

# Configurações padrão da DAG
default_args = {
    "owner": "airflow",
    "email_on_failure": True, #ativa alertas por email se algo quebrar
    "start_date": datetime(2021, 1, 1), # Ajustado para sua data atual
    "retries": 2, #se falahr, o Airflow tentarárodar de novo 2 vezes 
    "retry_delay": timedelta(minutes=5) #expera 5 minutos entre as tentativas
}

def download_rates():
    base_path = '/usr/local/airflow/dags/files' # Verifique se esta pasta existe no container
    open(f'{base_path}/forex_rates.json', 'w').close()
    try:
        with open(f'{base_path}/forex_currencies.csv') as f:
            reader = csv.DictReader(f, delimiter=';')
            for row in reader:
                base = row['base']
                # Nota: Esta API pode falhar sem Access Key
                res = requests.get(f'https://api.exchangeratesapi.io/latest?base={base}').json()
                
                # Verifique se a resposta contém 'rates' antes de acessar
                if 'rates' in res:
                    outdata = {'base': base, 'rates': res['rates'], 'last_update': res['date']}
                    with open(f'{base_path}/forex_rates.json', 'a') as outfile:
                        json.dump(outdata, outfile)
                        outfile.write('\n')
                else:
                    print(f"Erro na API para {base}: {res}")
    except Exception as e:
        print(f"Erro no processamento: {e}")
        raise

with DAG(
    dag_id="forex_data_pipeline", 
    start_date=datetime(2026, 4, 2), #data fixa
    schedule="@daily", #roda todo dia     
    default_args=default_args,
    catchup=True #ativa o catchup para rodar os dias anteriores 
) as dag:
    
    # Verifica se a API de moedas está online
    is_forex_rates_available = HttpSensor(
        task_id="is_forex_rates_available",
        method="GET",
        http_conn_id="forex_api",
        endpoint="latest",
        response_check=lambda response: "rates" in response.text,
        poke_interval=5,
        timeout=20
    )

    # Verifica se o arquivo CSV existe na pasta dags/files
    is_forex_currencies_file_available = FileSensor(
        task_id="is_forex_currencies_file_available",
        fs_conn_id="forex_path",
        filepath="forex_currencies.csv",
        poke_interval=5,
        timeout=20 
    )

    # Executa a função Python para baixar os dados
    downloading_rates = PythonOperator(
        task_id="download_forex_rates",
        python_callable=download_rates
    )

    # Salva o JSON no HDFS (Simulado no curso)
    saving_rates = BashOperator(
        task_id="saving_rates",
        bash_command="""
            hdfs dfs -mkdir -p /forex_data && \
            hdfs dfs -put -f /usr/local/airflow/dags/files/forex_rates.json /forex_data
        """
    )

    # Cria a tabela no Hive
    creating_table = BashOperator(
        task_id="creating_forex_rates_table",
        bash_command="""
            hive -e "
                CREATE EXTERNAL TABLE IF NOT EXISTS forex_rates(
                    base STRING, last_update DATE, eur DOUBLE, usd DOUBLE, 
                    nzd DOUBLE, gbp DOUBLE, jpy DOUBLE, cad DOUBLE
                )
                ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' STORED AS TEXTFILE
            "
        """
    )
    
    # load_forex_rates_table = HiveOperator(  # Commented out - provider not installed
    # task_id="load_forex_rates_table",
    # hive_cli_conn_id="hive_conn",
    # hql="""
    #     LOAD DATA LOCAL INPATH '/opt/airflow/dags/files/forex_rates.csv'
    #     OVERWRITE INTO TABLE forex_rates;
    # """
    # )

    load_forex_rates_table = BashOperator(
        task_id="load_forex_rates_table",
        bash_command="""
            echo "Loading data into Hive table (simulated)"
        """,
    )

    #Processamento Spark
    #forex_processing = SparkSubmitOperator(
     #   task_id="forex_processing",
      #  conn_id="spark_conn",
       # application="/usr/local/airflow/dags/scripts/forex_processing.py", 
        #verbose=False 
    #)

    # Notificação de Sucesso
    sending_email_notification = EmailOperator(
        task_id="sending_email",
        to="airflow_course@yopmail.com",
        subject="forex_data_pipeline",
        html_content="<h3>forex_data_pipeline succeeded</h3>"
    )

    sending_slack_notification = SlackWebhookOperator(
        task_id="sending_slack",
        slack_webhook_conn_id="slack_conn", # Nome da conexão
        message="DAG forex_data_pipeline: Done", 
        channel="#airflow-exploit",
        username="airflow"
    )


    
    is_forex_rates_available >> is_forex_currencies_file_available >> downloading_rates >> saving_rates >> creating_table >> load_forex_rates_table >> [sending_email_notification, sending_slack_notification]
