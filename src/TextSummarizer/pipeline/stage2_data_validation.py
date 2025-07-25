from TextSummarizer.components.data_validation import DataValidation
from TextSummarizer.config.configuration import ConfigurationManager


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validaiton_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validaiton_config)
        data_validation.validate_all_files_exist()
