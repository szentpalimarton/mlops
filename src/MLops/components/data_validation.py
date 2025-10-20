import os
from MLops.utils import logger
from MLops.entity.config_entity import DataValidationConfig
import pandas as pd

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)

            all_schema = self.config.all_schema
            missing_cols = []
            
            # Check all columns first
            for col in all_cols:
                if col not in all_schema:
                    missing_cols.append(col)
            
            # Set validation status based on whether any columns are missing
            validation_status = len(missing_cols) == 0
            
            # Write status file once at the end
            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation status: {validation_status}")
            
            if missing_cols:
                logger.error(f"Missing columns: {missing_cols}")
            else:
                logger.info("All columns are present in the schema")

            return validation_status
        except Exception as e:
            raise e
