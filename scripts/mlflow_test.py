import mlflow
import random 

# set the mlflow tracking uri. 
mlflow.set_tracking_uri("....")

# start an mlflow run. 
with mlflow.start_run():
    # Log some random parameters. 
    mlflow.log_param("param1", random.randint(1, 100))
    mlflow.log_param("param2", random.random())

    # Log some random metrics. 
    mlflow.log_metric("metric1", random.random())
    mlflow.log_metric("metric2", random.uniform(0.5, 1.5))