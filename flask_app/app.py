# This below code is to get the model from the model registry. 

import mlflow
from mlflow.tracking import MlflowClient

# Set mlflow tracking URI if hosted remotely. 
mlflow.set_tracking_uri("Enter my tracking uri")

# Load model from the model registry. 
def load_model_from_registry(model_name, model_version):
    model_uri = f"models:/{model_name, model_version}"
    model = mlflow.pyfunc.load_model(model_uri)
    return model 

# Example usage. 
model = load_model_from_registry("yt_chrome_plugin_model", "2")
print("Model loaded successfully.!")