from src.DataScience.config.configuration import ConfigurationManager
from src.DataScience.components.model_evaluation import ModelEvaluation
from src.DataScience import logger


STAGE="Model Evaluation"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        config=ConfigurationManager()
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE} started <<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.initiate_model_evaluation()
        logger.info(f">>>>>> stage {STAGE} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e