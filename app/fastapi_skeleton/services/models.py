

from typing import List

# import joblib
import numpy as np
from loguru import logger

from app.core.messages import NOT_VALID_ANSWER
from app.models.answer import AnswerTranscription
from app.models.prediction import AnswerCategory


import re
import unicodedata
import numpy as np
import pickle



class AnswerClassifierModel(object):

    # RESULT_UNIT_FACTOR = 100000

    def __init__(self, model_path, pre_proc_model_path):
        self.model_path = model_path
        self.pre_proc_model_path = pre_proc_model_path
        self._load_local_predict_model()
        self._load_local_prec_proc_model()

    def _load_local_predict_model(self):
        with open(self.model_path, "rb") as f:
            unpickler = pickle.Unpickler(f)
            self.predict_model = unpickler.load()

    def _load_local_prec_proc_model(self):
        with open(self.pre_proc_model_path, "rb") as f:
            unpickler = pickle.Unpickler(f)
            self.pre_proc_model = unpickler.load()
        # self.model = joblib.load(self.path)

    def _pre_process(self, answer: AnswerTranscription) -> str:
        logger.debug("Pre-processing payload.")
        
        def remove_special_chars(x):
            x = re.sub(r'[^\w ]+', "", x)
            x = ' '.join(x.split())
            x = ''.join([i for i in x if not i.isdigit()])
            return x

        def remove_accented_chars(x):
            x = unicodedata.normalize('NFKD', x).encode('ascii', 'ignore').decode('utf-8', 'ignore')
            return x
        
        def get_clean(x):
            x = str(x).lower()
            x = remove_accented_chars(x)
            x = remove_special_chars(x)
            return x
        
        answer = get_clean(answer.answer)
        logger.info(answer)
        features = self.pre_proc_model.transform([answer])

        return features


    def _post_process(self, result: float, result_proba:float) -> AnswerCategory:
        logger.debug("Post-processing prediction.")
        
        category = result
        category_proba = result_proba
        result_categ = AnswerCategory(
                categ=category,
                categ_prob=category_proba
                )
        return result_categ


    def _predict(self, features: str) -> tuple:
        logger.debug("Predicting.")
        prediction_result = self.predict_model.predict(features)
        prediction_proba = self.predict_model.predict_proba(features).max(axis=1)
        
        return prediction_result, prediction_proba


    def predict(self, answer: AnswerTranscription) -> AnswerCategory:
        if answer is None:
            raise ValueError(NOT_VALID_ANSWER.format(answer))

        pre_processed_answer = self._pre_process(answer)
        prediction, prediction_proba = self._predict(pre_processed_answer)
        logger.info(prediction)
        post_processed_result = self._post_process(prediction, prediction_proba)
        
        logger.log("SAVE", (answer.answer, prediction[0]))
        
        return post_processed_result
