from TextSummarizer.components.model_trainer import ModelTrainer
from TextSummarizer.config.configuration import ConfigurationManager
from TextSummarizer.config.configuration import ConfigurationManager


class DataModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(model_trainer_config)
        model_trainer.train()