from cnnClassifier.config import ConfigurationManager
from cnnClassifier.components import Evaluation
from cnnClassifier import logger


class EvaluationPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validatation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()
