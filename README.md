# task_6-prefect

* the whole task execution with task dataset took over 25 minutes since the size of the file. For the test purposes I've used data sapmle file called valera.csv

## Repo logic

* The flow code (analogue of DAG in airflow) is stated in the `flow.py` file
* Tasks (analogue of airflow tasks) can be found in `prefect_tasks.py` file 
* SQL queries needed to perform Snowflake transformations are listed in `queries.py` file
* Configs and JDBC connections are stored in `utils.py` file 
* YAML manifest to create a deployment (analogue of running DAG remotely in Airflow) is in 'snowflake_lte_process-deployment.yaml` file

## Nice to mention

* Prefect has a specific mechanism to track the state of tasks being executed hence I've used prefect logger in order to get better understanding
of what's going on. Example:
<img width="1105" alt="Снимок экрана 2022-09-21 в 20 51 18" src="https://user-images.githubusercontent.com/113433059/191575728-98dbcf83-df55-4c23-9192-fa5d638eb9e2.png">

* Deployed Flow looks like this 
<img width="1136" alt="Снимок экрана 2022-09-21 в 20 51 57" src="https://user-images.githubusercontent.com/113433059/191575837-b70cae4b-9e4d-42e8-a1a1-cf3dbe22875a.png">

* Task logs look like this 
<img width="882" alt="Снимок экрана 2022-09-21 в 20 52 38" src="https://user-images.githubusercontent.com/113433059/191575962-25f4ced3-42de-411c-9cb0-a17a2a681c8d.png">

* Deployed flows can be triggered via UI like this
<img width="1137" alt="Снимок экрана 2022-09-21 в 20 53 28" src="https://user-images.githubusercontent.com/113433059/191576096-3d485865-2ca9-4a98-9c39-5aa3c98b9345.png">

* Finally: Say no to airflow connections!!! 
