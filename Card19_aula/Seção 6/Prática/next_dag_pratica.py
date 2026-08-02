from airflow import DAG
from airflow.operators.bash_operator import BashOperator     # import estilo Airflow 1.x
from airflow.operators.python_operator import PythonOperator 

from datetime import datetime

default_args = {
    'start_date': datetime(2019, 1, 1),
    'owner': 'Airflow',
    'email': 'owner@test.com'   # e-mail para alertas 
}

def process(p1):
    print(p1)
    return 'done'

with DAG(dag_id='next_dag_aula', schedule_interval='0 0 * * *', default_args=default_args, catchup=False) as dag:
    # schedule_interval='0 0 * * *' = cron, roda todo dia à meia-noite

    tasks = [BashOperator(task_id='task_{0}'.format(t), bash_command='sleep 5'.format(t)) for t in range(1, 4)]
    # cria 3 tasks: task_1, task_2, task_3

    task_4 = PythonOperator(task_id='task_4', python_callable=process, op_args=['my super parameter'])
    # op_args passa argumentos posicionais pra função proces

    task_5 = BashOperator(task_id='task_5', bash_command='echo "pipeline done"')

    tasks >> task_4 >> task_5                                 # as 3 tasks devem terminar antes de task_4
