from prefect import task
from dotenv import dotenv_values
import pandas as pd
from sqlalchemy import create_engine
from utils import log_info


@task(retries=2, retry_delay_seconds=60)
def create_tables(cursor, *queries):
    """

    :param cursor: accepts cursor with connection from get_connection() task
    :param queries: SQL queries to execute
    :return: None
    """
    for query in queries:
        cursor.execute(query)
        result = cursor.fetchone()
        log_info(result)


@task(retries=2, retry_delay_seconds=60)
def create_streams(cursor, *queries):
    """

    :param cursor: accepts cursor with connection from get_connection() task
    :param queries: query: SQL queries to execute
    :return: None
    """
    for query in queries:
        cursor.execute(query)
        result = cursor.fetchone()
        log_info(result)


@task(retries=2, retry_delay_seconds=60)
def extract_dataframe(path: str) -> pd.DataFrame:
    """

    :param path:
    :return: None
    """
    df = pd.read_csv(path)
    result = df.describe()
    log_info(result)
    return df


@task(retries=2, retry_delay_seconds=60)
def load_dataframe(df: pd.DataFrame):
    """

    :param df:
    :return:
    """
    engine = create_engine(
        dotenv_values()['ENGINE']
    )
    connection = engine.connect().execution_options(autocommit=True)
    df.to_sql("raw_table", index=False, chunksize=16000, if_exists='append', con=connection)
    connection.close()
    engine.dispose()
    log_info('DataFrame loaded successfully')


@task(retries=2, retry_delay_seconds=60)
def insert_data(cursor, *queries):
    """

    :param cursor:
    :param queries:
    :return:
    """
    for query in queries:
        cursor.execute(query)
        result = cursor.fetchone()
        log_info(result)
