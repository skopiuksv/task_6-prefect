from prefect import flow
from queries import *
from utils import conn
from prefect_tasks import *


@flow
def snowflake_lte_process():
    """
    final description of the flow.
    The code of tasks can be found in prefect_tasks
    :return: None
    """
    create_tables(conn, query_create_tables1, query_create_tables2, query_create_tables3)
    create_streams(conn, query_create_streams1, query_create_streams2)
    df = extract_dataframe('valeratest.csv')
    load_dataframe(df)
    insert_data(conn, query_insert_data_1, query_insert_data_2)
