import os
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
from pathlib import Path
from src.DataScience.utils.common import *
from mlflow.models.signature import infer_signature
from src.DataScience.entity.config_entity import ModelEvaluationConfig


os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/sahilsiddharth/DataScienceProject.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"]="sahilsiddharth"
os.environ["MLFLOW_TRACKING_PASSWORD"]="65a3e985f82ad56f551a6c1e7b4eeaa226c76d7c"

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self,actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2
    
    def log_into_mlflow(self):

        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]


        #mlflow.set_registry_uri(self.config.mlflow_uri)
        mlflow.set_tracking_uri(uri="http://127.0.0.1:5000")
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        input_example = test_x.iloc[:5]
        signature = infer_signature(input_example)

        with mlflow.start_run():

            predicted_qualities = model.predict(test_x)

            (rmse, mae, r2) = self.eval_metrics(test_y, predicted_qualities)
            
            # Saving metrics as local
            scores = {"rmse": rmse, "mae": mae, "r2": r2}
            save_json(path=Path(self.config.metric_file_name), data=scores)

            mlflow.log_params(self.config.all_params)

            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("r2", r2)
            mlflow.log_metric("mae", mae)


            # Model registry does not work with file store
            if tracking_url_type_store != "file":

                mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticnetModel")
            else:
                mlflow.sklearn.log_model(model, "model",
                                         signature=signature,input_example=input_example)
