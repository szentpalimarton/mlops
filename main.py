from MLops.utils import logger
from MLops.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from MLops.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

stage_name = "Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {stage_name} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {stage_name} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

stage_name = "Data Validation stage"
try:
    logger.info(f">>>>>> stage {stage_name} started <<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {stage_name} completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e