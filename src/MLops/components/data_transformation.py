import os
from MLops.utils import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from MLops.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path)
        train_data, test_data = train_test_split(
            data, 
            test_size=self.config.test_size, 
            random_state=self.config.random_state
        )
        train_data.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test_data.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info("Data is splitted")
        logger.info(f"Train data shape: {train_data.shape}")
        logger.info(f"Test data shape: {test_data.shape}")

        print(train_data.shape)
        print(test_data.shape)   