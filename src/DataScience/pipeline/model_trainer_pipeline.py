from src.DataScience.config.configuration import ConfigurationManager
from src.DataScience.components.model_trainer import ModelTrainer
from src.DataScience import logger


STAGE="Data Ingestion"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_trainer(self):
        config=ConfigurationManager()
        model_trainer_config=config.get_model_trainer_config()
        model_trainer=ModelTrainer(config=model_trainer_config)
        model_trainer.train()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.initiate_model_trainer()
        logger.info(f">>>>>> stage {STAGE} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e