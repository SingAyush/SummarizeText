from TextSummarizer.pipeline.stage1_data_ingestion import DataIngestionTrainingPipeline
from TextSummarizer.logging import logger
from TextSummarizer.pipeline.stage2_data_validation import DataValidationTrainingPipeline
from TextSummarizer.pipeline.stage3_data_transformation import DataTransformationTrainingPipeline
from TextSummarizer.pipeline.stage4_model_trainer import DataModelTrainerPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">> stage {STAGE_NAME} started")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">> stage {STAGE_NAME} started")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f"stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f">> stage {STAGE_NAME} started")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f"stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Trainer Stage"

try:
    logger.info(f">> stage {STAGE_NAME} started")
    data_model_trainer = DataModelTrainerPipeline()
    data_model_trainer.main()
    logger.info(f"stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e

