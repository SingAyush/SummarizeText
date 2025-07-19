from TextSummarizer.components.model_evaluation import ModelEvaluation
from TextSummarizer.config.configuration import ConfigurationManager


class DataModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_ModelEvaluationConfig()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.evaluate()