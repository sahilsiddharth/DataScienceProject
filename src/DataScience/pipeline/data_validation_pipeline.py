from src.DataScience.config.configuration import ConfigurationManager
from src.DataScience.components.data_validation import DataValidation
from src.DataScience import logger


STAGE="Data Validation"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_validate(self):
        config=ConfigurationManager()
        data_validation_config=config.get_data_validation_config()
        data_validation=DataValidation(config=data_validation_config)
        data_validation.validate_columns()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE} started <<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.initiate_data_validate()
        logger.info(f">>>>>> stage {STAGE} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e