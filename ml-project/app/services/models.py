

from typing import List

import joblib
import pickle
import numpy as np
######
from app.logging import logger
# Gets or creates a logger
logger = logger.getChild(__name__)      

from app.core.messages import NOT_VALID_ANSWER
from app.templates.input import InputTemplate
from app.templates.output import OutputTemplate


THRESHOLD=0.95

CATEGORY_MAP = {
    0.0: 'negativo',
    1.0: 'positivo',
    2.0: 'neutral'
}

class Model(object):

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

    def _pre_process(self, input: InputTemplate) -> str:
        logger.debug("Pre-processing input.")
        
        def get_clean(x):
            # some code
            return x

        interim = get_clean(input.answer)
        logger.info(interim)
        features = self.pre_proc_model.transform([interim])

        return features


    def _post_process(self, out1, out2) -> OutputTemplate:
        logger.debug("Post-processing prediction.")
        
        if out2 < THRESHOLD:
            out1 = 2.0

        category = CATEGORY_MAP[out1]
        category_proba = out2

        output = OutputTemplate(
                categ=category,
                categ_prob=category_proba
                )
        return output


    def _predict(self, features: str) -> tuple:
        logger.debug("Predicting.")
        out1 = self.predict_model.predict(features)[0]
        out2 = self.predict_model.predict_proba(features).max(axis=1)[0]
        
        return out1, out2


    def predict(self, input: InputTemplate) -> OutputTemplate:
        if input is None:
            raise ValueError(NOT_VALID_ANSWER.format(input))

        interim = self._pre_process(input)
        out1, out2 = self._predict(interim)
        # logger.info((out1, out2))
        output = self._post_process(out1, out2)
        
        return output
