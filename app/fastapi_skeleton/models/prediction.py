

from pydantic import BaseModel


class AnswerCategory(BaseModel):
    categ:float
    categ_prob:float
