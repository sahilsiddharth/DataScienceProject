import os
import pandas as pd
from src.DataScience import logger
from src.DataScience.entity.config_entity import (DataValidationConfig)




class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config=config
    

    def validate_columns(self) ->bool:
        try:
            vailidation_status=None
            data=pd.read_csv(self.config.unzip_data_dir)
            all_columns=list(data.columns)
            schema_cols=self.config.all_schema.keys()

            for col in all_columns:
                if col not in schema_cols:
                    vailidation_status=False
                    with open(self. config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation Status: {vailidation_status}")
                else:
                    vailidation_status=True
                    with open(self. config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation Status: {vailidation_status}")
            return vailidation_status


            
        except Exception as e :
            raise e
