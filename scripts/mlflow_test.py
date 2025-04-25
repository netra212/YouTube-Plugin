import mlflow
import random 

# set the mlflow tracking uri.
# my ec2 instance name is: mlflow-ec2-server1

mlflow.set_tracking_uri("http://ec2-3-92-195-59.compute-1.amazonaws.com:5000/")

# start an mlflow run. 
with mlflow.start_run():
    # Log some random parameters. 
    mlflow.log_param("param1", random.randint(1, 100))
    mlflow.log_param("param2", random.random())

    # Log some random metrics. 
    mlflow.log_metric("metric1", random.random())
    mlflow.log_metric("metric2", random.uniform(0.5, 1.5))