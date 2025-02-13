import os 
import mlflow

# promoting the models. 
def promote_model():
    # Set up AWS MLFlow tracking URI. 
    mlflow.set_tracking_uri("....")

    client = mlflow.MlflowClient()

    # setting the model name. 
    model_name = "yt_chrome_plugin_model"

    # Get the latest version production model. 
    latest_version_staging = client.get_latest_versions(model_name, stages=["Staging"])[0].version

    # Archive the current production model. 
    prod_versions = client.get_latest_versions(model_name, stages=["Production"])

    for version in prod_versions:
        client.transition_model_version_stage(
            name=model_name, 
            version=version.version,
            stage="Arhived"
        )

