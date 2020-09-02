# Airflow-Workflows
This is a template repository for the DAGs, scripts, and other resources associated with an [Apache Airflow](https://airflow.apache.org/) project within the context of the [Airflow-Platorm](https://github.com/stlrda/Airflow-Platform) module and Saint Louis Regional Data Alliance Airflow Project Management Framework (outlined below). This module is designed to serve as a template; create a separate repository for each Airflow project.

# How STLRDA Manages Airflow Projects
The Saint Louis Regional Data Alliance's Airflow projects are managed using multiple Github repositories. Each repository is linked to and described below; see individual repositories for more information about their place in our ecosystem.

[Airflow-Platorm](https://github.com/stlrda/Airflow-Platform) sets up and configures our Airflow cluster.
         
[Airflow-Admin Tools](https://github.com/stlrda/Airflow-AdminTools) is put into the Airflow/dags folder of each server in the cluster, and provides basic dags that facilitate the administration of the cluster.

[Airflow-Infrastructure](https://github.com/stlrda/Airflow-Infrastructure) is a template repository for creating new Airflow projects. It spins up the non-Airflow AWS resources needed to do data integration work.

[Airflow-Workflows](https://github.com/stlrda/Airflow-Workflows) is a template repository for the DAGs, scripts,and other resources associated with a single Airflow-based ELT project.

## Replicating the STLRDA Workflow
1. Fork [Airflow-Admin Tools](https://github.com/stlrda/Airflow-AdminTools).
2. Modify your version of [clone_and_link.py](https://github.com/stlrda/Airflow-AdminTools/blob/master/scripts/clone_and_link.py) to look at your copy of [projects.csv](https://github.com/stlrda/Airflow-AdminTools/blob/master/resources/projects.csv)   
3. Clone or fork [Airflow-Platorm](https://github.com/stlrda/Airflow-Platform) and follow the provided instructions for setting up your Airflow cluster. Point the github variables in the .tfvars files to your fork of [Airflow-Admin Tools](https://github.com/stlrda/Airflow-AdminTools).
4. For each Airflow project you would like to manage separately, create a separate copy of [Airflow-Infrastructure](https://github.com/stlrda/Airflow-Infrastructure) and run it to spin up an S3 bucket and PostGreSQL database to serve as the ELT target.
5. For each Airflow project you would like to manage separately, create a separate copy of [Airflow-Workflows](https://github.com/stlrda/Airflow-Workflows) to manage the works and scripts associated with the project. Add this repository to your copy of [projects.csv](https://github.com/stlrda/Airflow-AdminTools/blob/master/resources/projects.csv).
6. Run the ImportDags Dag from your Airflow instance to pull in and update all your projects.