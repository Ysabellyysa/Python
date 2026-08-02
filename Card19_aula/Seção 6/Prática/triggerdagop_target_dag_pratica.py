#Importando as biblioteas utilizadas 
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
from datetime import datetime

# Dono da DAG, data a parit da qual a DAG pode rodas
default_args = {
    'owner': 'Marya',
    'start_date': datetime(2019, 1, 1),
}

#Dá acesso a dados da execução
def processar_pedido(**context):
    conf = context['dag_run'].conf # pega o dicionário 'conf' passado ao disparar a DAg
    pedido_id = conf.get('pedido_id', 'desconhecido') # busca 'pedido_id' com o valor padrão se não existir 
    valor     = conf.get('valor', 0) 
    cliente   = conf.get('cliente', 'desconhecido')

    print(f"Processando pedido {pedido_id} do cliente {cliente}")
    print(f"Valor total: R$ {valor:.2f}") #formata valor com 2 casas decimais 

    if valor >= 300: # regra de negócio simples
        print("Pedido aprovado, cupom frete grátis!")
    else:
        print("Frete será calculado!")

def registrar_no_banco(**context):
    conf = context['dag_run'].conf
    pedido_id = conf.get('pedido_id', 'desconhecido')
    print(f"Pedido {pedido_id} registrado no banco de dados com sucesso.")

# Identificador único da DAG 
with DAG(
    dag_id='triggerdagop_pratica', 
    default_args=default_args,
    schedule=None, # não roda automaticamente, só via trigger externo
    catchup=False, # não tenta rodar execuções passadas perdidas 
    tags=['teste', 'trigger_dagrun'] # tags só para organização visual
) as dag:

    processar = PythonOperator(
        task_id='processar_pedido',
        python_callable=processar_pedido # associa a função acima a esta task 
    )

    registrar = PythonOperator(
        task_id='registrar_banco',
        python_callable=registrar_banco 
    )

    confirmar = BashOperator(
        task_id='confirmar_processamento',
        bash_command='echo "Pedido {{ dag_run.conf[\"pedido_id\"] if dag_run.conf else \"\" }} confirmado!"'
        
    )

    fim = EmptyOperator(task_id='fim') # marca fim do pipeline, não faz nada

    processar >> registrar >> confirmar >> fim # define a ordem de execução 
