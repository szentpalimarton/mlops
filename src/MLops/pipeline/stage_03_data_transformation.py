from MLops.utils import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from pathlib import Path
from MLops.entity.config_entity import DataTransformationConfig
from MLops.components.data_transformation import DataTransformation
from MLops.config.configuration import ConfigurationManager

STAGE_NAME = "Data Transformation Stage"

class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().strip()
            
            if "True" in status:
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_splitting()

            else:
                raise Exception("Data validation failed")
        except Exception as e:
            raise e

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e