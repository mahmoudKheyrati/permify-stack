from airflow import DAG,utils
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
from os import path
from datetime import  date
from airflow.operators.dummy_operator import DummyOperator



default_args = {
    "owner": "yasin",
    "depends_on_past": False,
    "start_date": datetime(2023, 8, 1), 
    "email": ["yasinrezaei058@gmail.com"],
    "retries": 3,
    "retry_delay": timedelta(minutes=1),
}

dag = DAG("fn-dag", default_args=default_args, schedule_interval="*/5 * * * *" , catchup=False );

fn_create_schema1 = BashOperator(
    task_id='fn_create_schema1',
    bash_command='curl -X POST http://192.168.43.2:8080/invoke/01H9BRE0GJNG8G00GZJ0000002', 
    dag=dag
)

fn_create_schema2 = BashOperator(
    task_id='fn_create_schema2',
    bash_command='curl -X POST http://192.168.43.2:8080/invoke/01H9BRE0GJNG8G00GZJ0000002', 
    dag=dag
)

fn_create_schema3 = BashOperator(
    task_id='fn_create_schema3',
    bash_command='curl -X POST http://192.168.43.2:8080/invoke/01H9BRE0GJNG8G00GZJ0000002', 
    dag=dag
)
fn_create_schema4 = BashOperator(
    task_id='fn_create_schema4',
    bash_command='curl -X POST http://192.168.43.2:8080/invoke/01H9BRE0GJNG8G00GZJ0000002', 
    dag=dag
)


task_dummy = DummyOperator(task_id="Dummy-Operator", dag=dag)

fn_create_schema1 >> fn_create_schema2 >> fn_create_schema3 >> fn_create_schema4 >>  task_dummy
