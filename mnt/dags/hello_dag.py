from airflow import DAG
from airflow.utils import timezone
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator


default_args = {
    "owner": "atb",
}


with DAG(
    "hello_dag",
    default_args=default_args,
    schedule_interval=None,
    start_date=timezone.datetime(2022, 9, 26),
    catchup=False,
) as dag:
    start = EmptyOperator(task_id="start")

    say_hello = BashOperator(
        task_id="say_hello",
        bash_command="echo hola",
    )

    end = EmptyOperator(task_id="end")

    start >> say_hello >> end
