from dotenv import dotenv_values
from snowflake.connector import connect
from prefect import get_run_logger


def get_connection():
    """
    this task establishes connection via snowflake connector module (JDBC analogue)
    :return: cursor with established connection to Snowflake
    """
    # load dotenv values
    doten = dotenv_values()
    snowflake_connection = connect(
        user=doten['USER'],
        password=doten['PASSWORD'],
        account=doten['ACCOUNT'],
        database=doten['DATABASE'],
        schema=doten['SCHEMA'],
        warehouse=doten['WAREHOUSE']
    )
    cursor = snowflake_connection.cursor()
    return cursor


conn = get_connection()


def log_info(task_result):
    """
    function to call prefect-specific logs to show the state of the tasks
    :param task_result:
    :return: None
    """
    logger = get_run_logger()
    logger.info(f'   Query executed with the {task_result}')
